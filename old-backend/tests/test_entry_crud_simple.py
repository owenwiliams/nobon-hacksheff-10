#!/usr/bin/env python3
"""
Simple test runner for Entry CRUD operations without pytest dependency.
Run this file directly to test the entry_crud functions.
"""

import sys
import os
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from backend.database.db import Base
from backend.models.entry import Entry
from backend.models.progress import Progress
from backend.schema.entry_schema import EntryCreate, EntryUpdate
from backend.crud import entry_crud

# Test database setup
TEST_DATABASE_URL = "sqlite:///./test_entry_crud.db"
test_engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

def setup_test_db():
    """Create test database tables"""
    Base.metadata.create_all(bind=test_engine)
    print("✓ Test database created")

def cleanup_test_db():
    """Drop test database tables"""
    Base.metadata.drop_all(bind=test_engine)
    print("✓ Test database cleaned up")

def get_test_db():
    """Get test database session"""
    db = TestSessionLocal()
    try:
        return db
    except Exception as e:
        db.close()
        raise e

def create_test_progress(db):
    """Create a test progress record"""
    progress = Progress()
    db.add(progress)
    db.commit()
    db.refresh(progress)
    return progress

def test_create_entry():
    """Test creating an entry"""
    print("\n--- Testing Entry Creation ---")
    db = get_test_db()
    try:
        # Create test progress
        progress = create_test_progress(db)
        print(f"✓ Created test progress with ID: {progress.id}")
        
        # Create entry
        entry_data = EntryCreate(
            title="Test Entry",
            body="This is a test entry",
            entry_date=date.today(),
            progress_id=progress.id
        )
        
        created_entry = entry_crud.create_entry(db, entry_data)
        
        assert created_entry.id is not None
        assert created_entry.title == "Test Entry"
        assert created_entry.body == "This is a test entry"
        assert created_entry.progress_id == progress.id
        
        print(f"✓ Successfully created entry with ID: {created_entry.id}")
        print(f"  Title: {created_entry.title}")
        print(f"  Body: {created_entry.body}")
        print(f"  Progress ID: {created_entry.progress_id}")
        
        return created_entry
        
    except Exception as e:
        print(f"✗ Error creating entry: {e}")
        return None
    finally:
        db.close()

def test_get_entry():
    """Test retrieving an entry"""
    print("\n--- Testing Entry Retrieval ---")
    db = get_test_db()
    try:
        # First create an entry to retrieve
        progress = create_test_progress(db)
        entry_data = EntryCreate(
            title="Get Test Entry",
            body="This entry will be retrieved",
            entry_date=date.today(),
            progress_id=progress.id
        )
        created_entry = entry_crud.create_entry(db, entry_data)
        
        # Now retrieve it
        retrieved_entry = entry_crud.get_entry(db, created_entry.id)
        
        assert retrieved_entry is not None
        assert retrieved_entry.id == created_entry.id
        assert retrieved_entry.title == "Get Test Entry"
        
        print(f"✓ Successfully retrieved entry with ID: {retrieved_entry.id}")
        print(f"  Title: {retrieved_entry.title}")
        
        # Test retrieving non-existent entry
        non_existent = entry_crud.get_entry(db, 99999)
        assert non_existent is None
        print("✓ Correctly returned None for non-existent entry")
        
    except Exception as e:
        print(f"✗ Error retrieving entry: {e}")
    finally:
        db.close()

def test_update_entry():
    """Test updating an entry"""
    print("\n--- Testing Entry Update ---")
    db = get_test_db()
    try:
        # Create entry to update
        progress = create_test_progress(db)
        entry_data = EntryCreate(
            title="Original Title",
            body="Original body",
            entry_date=date.today(),
            progress_id=progress.id
        )
        created_entry = entry_crud.create_entry(db, entry_data)
        
        # Update the entry
        update_data = EntryUpdate(
            title="Updated Title",
            body="Updated body"
        )
        updated_entry = entry_crud.update_entry(db, created_entry.id, update_data)
        
        assert updated_entry is not None
        assert updated_entry.title == "Updated Title"
        assert updated_entry.body == "Updated body"
        assert updated_entry.progress_id == progress.id  # Should remain unchanged
        
        print(f"✓ Successfully updated entry with ID: {updated_entry.id}")
        print(f"  New Title: {updated_entry.title}")
        print(f"  New Body: {updated_entry.body}")
        
        # Test updating non-existent entry
        non_existent_update = entry_crud.update_entry(db, 99999, update_data)
        assert non_existent_update is None
        print("✓ Correctly returned None when updating non-existent entry")
        
    except Exception as e:
        print(f"✗ Error updating entry: {e}")
    finally:
        db.close()

def test_delete_entry():
    """Test deleting an entry"""
    print("\n--- Testing Entry Deletion ---")
    db = get_test_db()
    try:
        # Create entry to delete
        progress = create_test_progress(db)
        entry_data = EntryCreate(
            title="Entry to Delete",
            body="This entry will be deleted",
            entry_date=date.today(),
            progress_id=progress.id
        )
        created_entry = entry_crud.create_entry(db, entry_data)
        entry_id = created_entry.id
        
        # Delete the entry
        deleted_entry = entry_crud.delete_entry(db, entry_id)
        
        assert deleted_entry is not None
        assert deleted_entry.id == entry_id
        
        # Verify it's actually deleted
        check_deleted = entry_crud.get_entry(db, entry_id)
        assert check_deleted is None
        
        print(f"✓ Successfully deleted entry with ID: {deleted_entry.id}")
        print("✓ Verified entry no longer exists in database")
        
        # Test deleting non-existent entry
        non_existent_delete = entry_crud.delete_entry(db, 99999)
        assert non_existent_delete is None
        print("✓ Correctly returned None when deleting non-existent entry")
        
    except Exception as e:
        print(f"✗ Error deleting entry: {e}")
    finally:
        db.close()

def test_get_entries_by_progress():
    """Test retrieving entries by progress ID"""
    print("\n--- Testing Get Entries by Progress ---")
    db = get_test_db()
    try:
        # Create two progress records
        progress1 = create_test_progress(db)
        progress2 = create_test_progress(db)
        
        # Create entries for both progress records
        for i in range(3):
            entry_data1 = EntryCreate(
                title=f"Progress1 Entry {i+1}",
                body=f"Body for progress 1, entry {i+1}",
                entry_date=date.today(),
                progress_id=progress1.id
            )
            entry_crud.create_entry(db, entry_data1)
            
            entry_data2 = EntryCreate(
                title=f"Progress2 Entry {i+1}",
                body=f"Body for progress 2, entry {i+1}",
                entry_date=date.today(),
                progress_id=progress2.id
            )
            entry_crud.create_entry(db, entry_data2)
        
        # Get entries for progress1 only
        progress1_entries = entry_crud.get_entries_by_progress(db, progress1.id)
        
        assert len(progress1_entries) == 3
        for entry in progress1_entries:
            assert entry.progress_id == progress1.id
            assert "Progress1" in entry.title
        
        print(f"✓ Successfully retrieved {len(progress1_entries)} entries for progress {progress1.id}")
        
        # Get entries for progress2 only
        progress2_entries = entry_crud.get_entries_by_progress(db, progress2.id)
        
        assert len(progress2_entries) == 3
        for entry in progress2_entries:
            assert entry.progress_id == progress2.id
            assert "Progress2" in entry.title
        
        print(f"✓ Successfully retrieved {len(progress2_entries)} entries for progress {progress2.id}")
        
    except Exception as e:
        print(f"✗ Error testing get entries by progress: {e}")
    finally:
        db.close()

def test_error_conditions():
    """Test error conditions"""
    print("\n--- Testing Error Conditions ---")
    db = get_test_db()
    try:
        # Test creating entry with invalid progress_id
        entry_data = EntryCreate(
            title="Invalid Progress Entry",
            body="This should fail",
            entry_date=date.today(),
            progress_id=99999  # Non-existent progress_id
        )
        
        try:
            entry_crud.create_entry(db, entry_data)
            print("✗ Should have raised HTTPException for invalid progress_id")
        except Exception as e:
            print("✓ Correctly raised exception for invalid progress_id")
            print(f"  Error: {e}")
        
        # Test updating entry with invalid progress_id
        progress = create_test_progress(db)
        entry_data = EntryCreate(
            title="Valid Entry",
            body="This will be created successfully",
            entry_date=date.today(),
            progress_id=progress.id
        )
        created_entry = entry_crud.create_entry(db, entry_data)
        
        update_data = EntryUpdate(progress_id=99999)  # Invalid progress_id
        
        try:
            entry_crud.update_entry(db, created_entry.id, update_data)
            print("✗ Should have raised ValueError for invalid progress_id update")
        except ValueError as e:
            print("✓ Correctly raised ValueError for invalid progress_id update")
            print(f"  Error: {e}")
        
    except Exception as e:
        print(f"✗ Unexpected error in error condition testing: {e}")
    finally:
        db.close()

def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("ENTRY CRUD TESTING SUITE")
    print("=" * 60)
    
    try:
        # Setup
        setup_test_db()
        
        # Run tests
        test_create_entry()
        test_get_entry()
        test_update_entry()
        test_delete_entry()
        test_get_entries_by_progress()
        test_error_conditions()
        
        print("\n" + "=" * 60)
        print("ALL TESTS COMPLETED!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ CRITICAL ERROR: {e}")
    finally:
        # Cleanup
        cleanup_test_db()

if __name__ == "__main__":
    run_all_tests()