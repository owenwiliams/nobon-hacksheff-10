import React from 'react';
import EntryForm from '../components/EntryForm';

const TestEntryForm = () => {
  const handleEntrySubmit = (newEntry) => {
    console.log('New entry created:', newEntry);
    alert(`Entry "${newEntry.title}" saved successfully!`);
  };

  return (
    <div className="container mt-4">
      <h2>Test Entry Form</h2>
      <EntryForm onSubmit={handleEntrySubmit} />
      
      <div className="mt-4">
        <h5>Instructions:</h5>
        <ul>
          <li>Fill in the title and content fields</li>
          <li>Click "Save Entry" to test the form</li>
          <li>Check the browser console for the API response</li>
          <li>Check your backend terminal for API requests</li>
        </ul>
      </div>
    </div>
  );
};

export default TestEntryForm;