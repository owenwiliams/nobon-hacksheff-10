#!/usr/bin/env python3
"""
Minimal test to check basic Entry model functionality.
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

# Test database setup
TEST_DATABASE_URL = "sqlite:///./test_minimal.db"
test_engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

def test_basic_models():
    """Test basic model creation without CRUD functions"""
    print("Testing basic model creation...")
    
    # Create all tables
    Base.metadata.create_all(bind=test_engine)
    
    db = TestSessionLocal()
    try:
        # Create progress first
        progress = Progress()
        db.add(progress)
        db.commit()
        db.refresh(progress)
        print(f"✓ Created progress with ID: {progress.id}")
        
        # Create entry
        entry = Entry(
            title="Test Entry",
            body="Test body",
            entry_date=date.today(),
            progress_id=progress.id
        )
        db.add(entry)
        db.commit()
        db.refresh(entry)
        print(f"✓ Created entry with ID: {entry.id}")
        
        # Query entry back
        retrieved_entry = db.query(Entry).filter(Entry.id == entry.id).first()
        print(f"✓ Retrieved entry: {retrieved_entry.title}")
        
        print("✓ Basic model test passed!")
        
    except Exception as e:
        print(f"✗ Error in basic model test: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()
        Base.metadata.drop_all(bind=test_engine)

if __name__ == "__main__":
    test_basic_models()