import React, { useState } from 'react';
import { entryAPI } from '../services/api';

const EntryForm = ({ onSubmit }) => {
  const [title, setTitle] = useState('');
  const [body, setBody] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!title.trim() || !body.trim()) {
      alert('Please fill in both title and content');
      return;
    }

    setIsSubmitting(true);

    try {
      const entryData = {
        title: title.trim(),
        body: body.trim(),
        entry_date: new Date().toISOString().split('T')[0]
      };

      const result = await entryAPI.create(entryData);
      
      if (onSubmit) {
        onSubmit(result);
      }

      // Reset form
      setTitle('');
      setBody('');
      
    } catch (error) {
      console.error('Error saving entry:', error);
      alert('Failed to save entry. Please try again.');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="mb-4">
      <div className="mb-3">
        <input
          type="text"
          className="form-control"
          placeholder="Entry title..."
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          disabled={isSubmitting}
        />
      </div>
      
      <div className="mb-3">
        <textarea
          className="form-control"
          rows="6"
          placeholder="Write your thoughts..."
          value={body}
          onChange={(e) => setBody(e.target.value)}
          disabled={isSubmitting}
        />
      </div>
      
      <button 
        type="submit" 
        className="btn btn-primary"
        disabled={isSubmitting || !title.trim() || !body.trim()}
      >
        {isSubmitting ? 'Saving...' : 'Save Entry'}
      </button>
    </form>
  );
};

export default EntryForm;
