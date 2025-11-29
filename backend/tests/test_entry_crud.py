import pytest
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException

from backend.database.db import Base
from backend.crud import entry_crud
from backend.models.entry import Entry
from backend.models.progress import Progress
from backend.schema.entry_schema import EntryCreate, EntryUpdate


# Test database setup
TEST_DATABASE_URL = "sqlite:///./test_entry_crud.db"
test_engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


@pytest.fixture(scope="function")
def db_session():
    """Create a fresh database for each test"""
    Base.metadata.create_all(bind=test_engine)
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=test_engine)


@pytest.fixture
def sample_progress(db_session):
    """Create a sample progress record for testing"""
    progress = Progress()
    db_session.add(progress)
    db_session.commit()
    db_session.refresh(progress)
    return progress


@pytest.fixture
def sample_entry_data():
    """Sample entry data for testing"""
    return {
        "title": "Test Entry",
        "body": "This is a test entry body",
        "entry_date": date.today()
    }


class TestCreateEntry:
    def test_create_entry_success(self, db_session, sample_progress, sample_entry_data):
        """Test successful entry creation"""
        entry_data = EntryCreate(
            progress_id=sample_progress.id,
            **sample_entry_data
        )
        
        created_entry = entry_crud.create_entry(db_session, entry_data)
        
        assert created_entry.id is not None
        assert created_entry.title == sample_entry_data["title"]
        assert created_entry.body == sample_entry_data["body"]
        assert created_entry.entry_date == sample_entry_data["entry_date"]
        assert created_entry.progress_id == sample_progress.id
        
        # Verify it's actually in the database
        db_entry = db_session.query(Entry).filter(Entry.id == created_entry.id).first()
        assert db_entry is not None
        assert db_entry.title == sample_entry_data["title"]

    def test_create_entry_invalid_progress_id(self, db_session, sample_entry_data):
        """Test entry creation with non-existent progress_id"""
        entry_data = EntryCreate(
            progress_id=999,  # Non-existent progress_id
            **sample_entry_data
        )
        
        with pytest.raises(HTTPException) as exc_info:
            entry_crud.create_entry(db_session, entry_data)
        
        assert exc_info.value.status_code == 404
        assert "Progress id 999 not found" in str(exc_info.value.detail)


class TestGetEntry:
    def test_get_existing_entry(self, db_session, sample_progress, sample_entry_data):
        """Test retrieving an existing entry"""
        # Create an entry first
        entry_data = EntryCreate(
            progress_id=sample_progress.id,
            **sample_entry_data
        )
        created_entry = entry_crud.create_entry(db_session, entry_data)
        
        # Retrieve the entry
        retrieved_entry = entry_crud.get_entry(db_session, created_entry.id)
        
        assert retrieved_entry is not None
        assert retrieved_entry.id == created_entry.id
        assert retrieved_entry.title == sample_entry_data["title"]
        assert retrieved_entry.body == sample_entry_data["body"]

    def test_get_nonexistent_entry(self, db_session):
        """Test retrieving a non-existent entry"""
        retrieved_entry = entry_crud.get_entry(db_session, 999)
        assert retrieved_entry is None


class TestGetEntries:
    def test_get_entries_empty_database(self, db_session):
        """Test retrieving entries from empty database"""
        entries = entry_crud.get_entries(db_session)
        assert entries == []

    def test_get_entries_with_data(self, db_session, sample_progress, sample_entry_data):
        """Test retrieving entries with data in database"""
        # Create multiple entries
        for i in range(3):
            entry_data = EntryCreate(
                progress_id=sample_progress.id,
                title=f"Entry {i+1}",
                body=f"Body {i+1}",
                entry_date=date.today()
            )
            entry_crud.create_entry(db_session, entry_data)
        
        entries = entry_crud.get_entries(db_session)
        assert len(entries) == 3
        assert all(isinstance(entry, Entry) for entry in entries)

    def test_get_entries_with_pagination(self, db_session, sample_progress):
        """Test retrieving entries with pagination"""
        # Create 5 entries
        for i in range(5):
            entry_data = EntryCreate(
                progress_id=sample_progress.id,
                title=f"Entry {i+1}",
                body=f"Body {i+1}",
                entry_date=date.today()
            )
            entry_crud.create_entry(db_session, entry_data)
        
        # Test pagination
        entries_page1 = entry_crud.get_entries(db_session, skip=0, limit=2)
        assert len(entries_page1) == 2
        
        entries_page2 = entry_crud.get_entries(db_session, skip=2, limit=2)
        assert len(entries_page2) == 2
        
        entries_page3 = entry_crud.get_entries(db_session, skip=4, limit=2)
        assert len(entries_page3) == 1


class TestGetEntriesByProgress:
    def test_get_entries_by_progress_empty(self, db_session, sample_progress):
        """Test retrieving entries by progress_id when none exist"""
        entries = entry_crud.get_entries_by_progress(db_session, sample_progress.id)
        assert entries == []

    def test_get_entries_by_progress_with_data(self, db_session):
        """Test retrieving entries by specific progress_id"""
        # Create two progress records
        progress1 = Progress()
        progress2 = Progress()
        db_session.add_all([progress1, progress2])
        db_session.commit()
        db_session.refresh(progress1)
        db_session.refresh(progress2)
        
        # Create entries for both progress records
        for i in range(2):
            entry_data1 = EntryCreate(
                progress_id=progress1.id,
                title=f"Progress1 Entry {i+1}",
                body=f"Body {i+1}",
                entry_date=date.today()
            )
            entry_crud.create_entry(db_session, entry_data1)
            
            entry_data2 = EntryCreate(
                progress_id=progress2.id,
                title=f"Progress2 Entry {i+1}",
                body=f"Body {i+1}",
                entry_date=date.today()
            )
            entry_crud.create_entry(db_session, entry_data2)
        
        # Get entries for progress1 only
        progress1_entries = entry_crud.get_entries_by_progress(db_session, progress1.id)
        assert len(progress1_entries) == 2
        assert all(entry.progress_id == progress1.id for entry in progress1_entries)
        assert all("Progress1" in entry.title for entry in progress1_entries)


class TestUpdateEntry:
    def test_update_entry_success(self, db_session, sample_progress, sample_entry_data):
        """Test successful entry update"""
        # Create an entry
        entry_data = EntryCreate(
            progress_id=sample_progress.id,
            **sample_entry_data
        )
        created_entry = entry_crud.create_entry(db_session, entry_data)
        
        # Update the entry
        update_data = EntryUpdate(
            title="Updated Title",
            body="Updated Body"
        )
        updated_entry = entry_crud.update_entry(db_session, created_entry.id, update_data)
        
        assert updated_entry is not None
        assert updated_entry.id == created_entry.id
        assert updated_entry.title == "Updated Title"
        assert updated_entry.body == "Updated Body"
        assert updated_entry.entry_date == sample_entry_data["entry_date"]  # Unchanged
        assert updated_entry.progress_id == sample_progress.id  # Unchanged

    def test_update_entry_partial(self, db_session, sample_progress, sample_entry_data):
        """Test partial entry update"""
        # Create an entry
        entry_data = EntryCreate(
            progress_id=sample_progress.id,
            **sample_entry_data
        )
        created_entry = entry_crud.create_entry(db_session, entry_data)
        
        # Update only the title
        update_data = EntryUpdate(title="Only Title Updated")
        updated_entry = entry_crud.update_entry(db_session, created_entry.id, update_data)
        
        assert updated_entry.title == "Only Title Updated"
        assert updated_entry.body == sample_entry_data["body"]  # Unchanged

    def test_update_entry_progress_id_valid(self, db_session, sample_progress, sample_entry_data):
        """Test updating entry with valid new progress_id"""
        # Create second progress
        progress2 = Progress()
        db_session.add(progress2)
        db_session.commit()
        db_session.refresh(progress2)
        
        # Create an entry
        entry_data = EntryCreate(
            progress_id=sample_progress.id,
            **sample_entry_data
        )
        created_entry = entry_crud.create_entry(db_session, entry_data)
        
        # Update progress_id
        update_data = EntryUpdate(progress_id=progress2.id)
        updated_entry = entry_crud.update_entry(db_session, created_entry.id, update_data)
        
        assert updated_entry.progress_id == progress2.id

    def test_update_entry_progress_id_invalid(self, db_session, sample_progress, sample_entry_data):
        """Test updating entry with invalid progress_id"""
        # Create an entry
        entry_data = EntryCreate(
            progress_id=sample_progress.id,
            **sample_entry_data
        )
        created_entry = entry_crud.create_entry(db_session, entry_data)
        
        # Try to update with invalid progress_id
        update_data = EntryUpdate(progress_id=999)
        
        with pytest.raises(ValueError) as exc_info:
            entry_crud.update_entry(db_session, created_entry.id, update_data)
        
        assert "Progress id 999 not found" in str(exc_info.value)

    def test_update_nonexistent_entry(self, db_session):
        """Test updating a non-existent entry"""
        update_data = EntryUpdate(title="Updated Title")
        updated_entry = entry_crud.update_entry(db_session, 999, update_data)
        assert updated_entry is None


class TestDeleteEntry:
    def test_delete_entry_success(self, db_session, sample_progress, sample_entry_data):
        """Test successful entry deletion"""
        # Create an entry
        entry_data = EntryCreate(
            progress_id=sample_progress.id,
            **sample_entry_data
        )
        created_entry = entry_crud.create_entry(db_session, entry_data)
        entry_id = created_entry.id
        
        # Delete the entry
        deleted_entry = entry_crud.delete_entry(db_session, entry_id)
        
        assert deleted_entry is not None
        assert deleted_entry.id == entry_id
        
        # Verify it's actually deleted from database
        db_entry = db_session.query(Entry).filter(Entry.id == entry_id).first()
        assert db_entry is None

    def test_delete_nonexistent_entry(self, db_session):
        """Test deleting a non-existent entry"""
        deleted_entry = entry_crud.delete_entry(db_session, 999)
        assert deleted_entry is None


class TestIntegration:
    def test_full_crud_workflow(self, db_session, sample_progress, sample_entry_data):
        """Test complete CRUD workflow"""
        # Create
        entry_data = EntryCreate(
            progress_id=sample_progress.id,
            **sample_entry_data
        )
        created_entry = entry_crud.create_entry(db_session, entry_data)
        assert created_entry.id is not None
        
        # Read
        retrieved_entry = entry_crud.get_entry(db_session, created_entry.id)
        assert retrieved_entry.title == sample_entry_data["title"]
        
        # Update
        update_data = EntryUpdate(title="Updated in Workflow")
        updated_entry = entry_crud.update_entry(db_session, created_entry.id, update_data)
        assert updated_entry.title == "Updated in Workflow"
        
        # Delete
        deleted_entry = entry_crud.delete_entry(db_session, created_entry.id)
        assert deleted_entry is not None
        
        # Verify deletion
        final_check = entry_crud.get_entry(db_session, created_entry.id)
        assert final_check is None