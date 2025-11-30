import React, { useState, useEffect } from 'react';
import { 
  getAllJourneys, 
  createJourney, 
  updateJourney, 
  getQuestsByJourney 
} from '../services/journeysApi';
import {
  createQuest,
  updateQuest,
  getTasksByQuest
} from '../services/questsApi';
import {
  createTask,
  updateTask
} from '../services/tasksApi';

const Journeys = () => {
  const [journeys, setJourneys] = useState([]);
  const [quests, setQuests] = useState({});
  const [tasks, setTasks] = useState({});
  const [loading, setLoading] = useState(true);
  const [expandedJourneys, setExpandedJourneys] = useState(new Set());
  const [expandedQuests, setExpandedQuests] = useState(new Set());
  
  // Modal states
  const [showJourneyModal, setShowJourneyModal] = useState(false);
  const [showQuestModal, setShowQuestModal] = useState(false);
  const [showTaskModal, setShowTaskModal] = useState(false);
  const [selectedJourneyId, setSelectedJourneyId] = useState(null);
  const [selectedQuestId, setSelectedQuestId] = useState(null);

  // Form data
  const [journeyForm, setJourneyForm] = useState({
    title: '',
    start_date: new Date().toISOString().split('T')[0]
  });
  const [questForm, setQuestForm] = useState({
    title: '',
    start_date: new Date().toISOString().split('T')[0],
    due_date: '',
    journey_id: null
  });
  const [taskForm, setTaskForm] = useState({
    body: '',
    quest_id: null,
    is_completed: false
  });

  useEffect(() => {
    loadJourneys();
  }, []);

  const loadJourneys = async () => {
    try {
      setLoading(true);
      const data = await getAllJourneys();
      setJourneys(data);
    } catch (err) {
      console.error('Error loading journeys:', err);
    } finally {
      setLoading(false);
    }
  };

  const loadQuests = async (journeyId) => {
    try {
      const data = await getQuestsByJourney(journeyId);
      setQuests(prev => ({...prev, [journeyId]: data}));
    } catch (err) {
      console.error('Error loading quests:', err);
    }
  };

  const loadTasks = async (questId) => {
    try {
      const data = await getTasksByQuest(questId);
      setTasks(prev => ({...prev, [questId]: data}));
    } catch (err) {
      console.error('Error loading tasks:', err);
    }
  };

  const toggleJourney = async (journeyId) => {
    const newExpanded = new Set(expandedJourneys);
    if (newExpanded.has(journeyId)) {
      newExpanded.delete(journeyId);
    } else {
      newExpanded.add(journeyId);
      if (!quests[journeyId]) {
        await loadQuests(journeyId);
      }
    }
    setExpandedJourneys(newExpanded);
  };

  const toggleQuest = async (questId) => {
    const newExpanded = new Set(expandedQuests);
    if (newExpanded.has(questId)) {
      newExpanded.delete(questId);
    } else {
      newExpanded.add(questId);
      if (!tasks[questId]) {
        await loadTasks(questId);
      }
    }
    setExpandedQuests(newExpanded);
  };

  // Journey handlers
  const handleCreateJourney = async (e) => {
    e.preventDefault();
    try {
      const journeyData = {
        title: journeyForm.title,
        start_date: journeyForm.start_date,
        end_date: null
      };
      await createJourney(journeyData);
      setJourneyForm({
        title: '',
        start_date: new Date().toISOString().split('T')[0]
      });
      setShowJourneyModal(false);
      loadJourneys();
    } catch (err) {
      console.error('Error creating journey:', err);
      alert('Failed to create journey');
    }
  };

  const handleCompleteJourney = async (journeyId) => {
    if (window.confirm('Mark this journey as complete?')) {
      try {
        await updateJourney(journeyId, {
          end_date: new Date().toISOString().split('T')[0]
        });
        loadJourneys();
      } catch (err) {
        console.error('Error completing journey:', err);
        alert('Failed to complete journey');
      }
    }
  };

  // Quest handlers
  const handleCreateQuest = async (e) => {
    e.preventDefault();
    try {
      const questData = {
        title: questForm.title,
        start_date: questForm.start_date,
        due_date: questForm.due_date || null,
        end_date: null,
        journey_id: selectedJourneyId
      };
      await createQuest(questData);
      setQuestForm({
        title: '',
        start_date: new Date().toISOString().split('T')[0],
        due_date: '',
        journey_id: null
      });
      setShowQuestModal(false);
      loadQuests(selectedJourneyId);
    } catch (err) {
      console.error('Error creating quest:', err);
      alert('Failed to create quest');
    }
  };

  const handleCompleteQuest = async (questId, journeyId) => {
    if (window.confirm('Mark this quest as complete?')) {
      try {
        await updateQuest(questId, {
          end_date: new Date().toISOString().split('T')[0]
        });
        loadQuests(journeyId);
      } catch (err) {
        console.error('Error completing quest:', err);
        alert('Failed to complete quest');
      }
    }
  };

  // Task handlers
  const handleCreateTask = async (e) => {
    e.preventDefault();
    try {
      await createTask({...taskForm, quest_id: selectedQuestId});
      setTaskForm({
        body: '',
        quest_id: null,
        is_completed: false
      });
      setShowTaskModal(false);
      loadTasks(selectedQuestId);
    } catch (err) {
      console.error('Error creating task:', err);
      alert('Failed to create task');
    }
  };

  const handleToggleTask = async (taskId, currentStatus, questId) => {
    try {
      await updateTask(taskId, {
        is_completed: !currentStatus
      });
      loadTasks(questId);
    } catch (err) {
      console.error('Error updating task:', err);
      alert('Failed to update task');
    }
  };

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString();
  };

  const isOverdue = (dueDateString) => {
    if (!dueDateString) return false;
    return new Date(dueDateString) < new Date();
  };

  const isComplete = (endDate) => {
    return endDate !== null && endDate !== undefined;
  };

  if (loading) {
    return (
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '50vh' }}>
        <div>Loading...</div>
      </div>
    );
  }

  return (
    <div style={{ padding: '20px', maxWidth: '1200px', margin: '0 auto' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '24px' }}>
        <h1>Life Journeys</h1>
        <button 
          onClick={() => setShowJourneyModal(true)}
          style={{
            backgroundColor: '#007bff',
            color: 'white',
            border: 'none',
            borderRadius: '6px',
            padding: '8px 16px',
            cursor: 'pointer'
          }}
        >
          + New Journey
        </button>
      </div>

      {/* Journeys List */}
      {journeys.length === 0 ? (
        <div style={{ textAlign: 'center', padding: '40px', color: '#666' }}>
          <h3>No journeys yet</h3>
          <p>Create your first life journey to start achieving your goals!</p>
        </div>
      ) : (
        <div>
          {journeys.map(journey => (
            <div key={journey.id} style={{
              border: '1px solid #ddd',
              borderRadius: '8px',
              marginBottom: '16px',
              backgroundColor: '#fff'
            }}>
              <div 
                style={{
                  padding: '16px',
                  borderBottom: expandedJourneys.has(journey.id) ? '1px solid #eee' : 'none',
                  cursor: 'pointer',
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center'
                }}
                onClick={() => toggleJourney(journey.id)}
              >
                <div>
                  <h3 style={{ margin: 0 }}>{journey.title}</h3>
                  <small style={{ color: '#666' }}>
                    Started: {formatDate(journey.start_date)}
                    {journey.end_date && ` • Completed: ${formatDate(journey.end_date)}`}
                  </small>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <span style={{
                    padding: '4px 8px',
                    borderRadius: '4px',
                    fontSize: '12px',
                    backgroundColor: journey.end_date ? '#d4edda' : '#cce5ff',
                    color: journey.end_date ? '#155724' : '#004085'
                  }}>
                    {journey.end_date ? 'Completed' : 'Active'}
                  </span>
                  <span>{expandedJourneys.has(journey.id) ? '▼' : '▶'}</span>
                </div>
              </div>
              
              {expandedJourneys.has(journey.id) && (
                <div style={{ padding: '16px' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px' }}>
                    <h4>Quests</h4>
                    <div>
                      {!isComplete(journey.end_date) && (
                        <button 
                          onClick={() => {
                            setSelectedJourneyId(journey.id);
                            setShowQuestModal(true);
                          }}
                          style={{
                            backgroundColor: '#28a745',
                            color: 'white',
                            border: 'none',
                            borderRadius: '4px',
                            padding: '4px 8px',
                            cursor: 'pointer',
                            marginRight: '8px'
                          }}
                        >
                          + Add Quest
                        </button>
                      )}
                      {isComplete(journey.end_date) && (
                        <span style={{ 
                          color: '#666', 
                          fontSize: '12px', 
                          fontStyle: 'italic',
                          marginRight: '8px' 
                        }}>
                          Journey completed - no new quests can be added
                        </span>
                      )}
                      {!journey.end_date && (
                        <button 
                          onClick={() => handleCompleteJourney(journey.id)}
                          style={{
                            backgroundColor: '#ffc107',
                            color: 'black',
                            border: 'none',
                            borderRadius: '4px',
                            padding: '4px 8px',
                            cursor: 'pointer'
                          }}
                        >
                          Complete Journey
                        </button>
                      )}
                    </div>
                  </div>

                  {/* Quests */}
                  {quests[journey.id]?.map(quest => (
                    <div key={quest.id} style={{
                      border: '1px solid #eee',
                      borderRadius: '6px',
                      marginBottom: '8px',
                      backgroundColor: '#f8f9fa'
                    }}>
                      <div style={{
                        padding: '12px',
                        display: 'flex',
                        justifyContent: 'space-between',
                        alignItems: 'center',
                        cursor: 'pointer'
                      }}
                      onClick={() => toggleQuest(quest.id)}
                      >
                        <div>
                          <h5 style={{ margin: 0 }}>{quest.title}</h5>
                          <small style={{ color: '#666' }}>
                            Due: {quest.due_date ? formatDate(quest.due_date) : 'No deadline'}
                            {isOverdue(quest.due_date) && <span style={{ color: 'red' }}> (Overdue)</span>}
                          </small>
                        </div>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                          <span style={{
                            padding: '2px 6px',
                            borderRadius: '3px',
                            fontSize: '11px',
                            backgroundColor: quest.end_date ? '#d4edda' : 
                                          isOverdue(quest.due_date) ? '#f8d7da' : '#fff3cd',
                            color: quest.end_date ? '#155724' : 
                                  isOverdue(quest.due_date) ? '#721c24' : '#856404'
                          }}>
                            {quest.end_date ? 'Done' : isOverdue(quest.due_date) ? 'Overdue' : 'In Progress'}
                          </span>
                          {!quest.end_date && (
                            <button 
                              onClick={(e) => {
                                e.stopPropagation();
                                handleCompleteQuest(quest.id, journey.id);
                              }}
                              style={{
                                backgroundColor: '#28a745',
                                color: 'white',
                                border: 'none',
                                borderRadius: '3px',
                                padding: '2px 6px',
                                cursor: 'pointer',
                                fontSize: '11px'
                              }}
                            >
                              Complete
                            </button>
                          )}
                          <span>{expandedQuests.has(quest.id) ? '▼' : '▶'}</span>
                        </div>
                      </div>

                      {/* Tasks */}
                      {expandedQuests.has(quest.id) && (
                        <div style={{ padding: '0 12px 12px' }}>
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                            <small style={{ color: '#666' }}>Tasks:</small>
                            {!isComplete(quest.end_date) && !isComplete(journey.end_date) && (
                              <button 
                                onClick={() => {
                                  setSelectedQuestId(quest.id);
                                  setShowTaskModal(true);
                                }}
                                style={{
                                  backgroundColor: '#17a2b8',
                                  color: 'white',
                                  border: 'none',
                                  borderRadius: '3px',
                                  padding: '2px 6px',
                                  cursor: 'pointer',
                                  fontSize: '11px'
                                }}
                              >
                                + Add Task
                              </button>
                            )}
                            {(isComplete(quest.end_date) || isComplete(journey.end_date)) && (
                              <span style={{ 
                                color: '#666', 
                                fontSize: '10px', 
                                fontStyle: 'italic' 
                              }}>
                                {isComplete(journey.end_date) ? 'Journey completed' : 'Quest completed'}
                              </span>
                            )}
                          </div>
                          
                          {tasks[quest.id]?.map(task => (
                            <div key={task.id} style={{ display: 'flex', alignItems: 'center', marginBottom: '4px' }}>
                              <input 
                                type="checkbox" 
                                checked={task.is_completed}
                                onChange={() => handleToggleTask(task.id, task.is_completed, quest.id)}
                                disabled={isComplete(quest.end_date) || isComplete(journey.end_date)}
                                style={{ 
                                  marginRight: '8px',
                                  opacity: (isComplete(quest.end_date) || isComplete(journey.end_date)) ? 0.5 : 1,
                                  cursor: (isComplete(quest.end_date) || isComplete(journey.end_date)) ? 'not-allowed' : 'pointer'
                                }}
                              />
                              <span style={{
                                textDecoration: task.is_completed ? 'line-through' : 'none',
                                color: task.is_completed ? '#666' : (isComplete(quest.end_date) || isComplete(journey.end_date)) ? '#999' : '#000',
                                opacity: (isComplete(quest.end_date) || isComplete(journey.end_date)) ? 0.7 : 1
                              }}>
                                {task.body}
                              </span>
                              {(isComplete(quest.end_date) || isComplete(journey.end_date)) && !task.is_completed && (
                                <span style={{ 
                                  marginLeft: '8px', 
                                  fontSize: '10px', 
                                  color: '#999', 
                                  fontStyle: 'italic' 
                                }}>
                                  ({isComplete(journey.end_date) ? 'journey completed' : 'quest completed'})
                                </span>
                              )}
                            </div>
                          ))}
                          
                          {(!tasks[quest.id] || tasks[quest.id].length === 0) && (
                            <small style={{ color: '#999' }}>
                              {(isComplete(quest.end_date) || isComplete(journey.end_date))
                                ? `This ${isComplete(journey.end_date) ? 'journey' : 'quest'} is completed.` 
                                : "No tasks yet. Add some tasks to break this quest down!"
                              }
                            </small>
                          )}
                        </div>
                      )}
                    </div>
                  ))}
                  
                  {(!quests[journey.id] || quests[journey.id].length === 0) && (
                    <p style={{ color: '#999' }}>No quests yet. Add some quests to break down this journey!</p>
                  )}
                </div>
              )}
            </div>
          ))}
        </div>
      )}

      {/* Journey Modal */}
      {showJourneyModal && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          backgroundColor: 'rgba(0,0,0,0.5)',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          zIndex: 1000
        }}>
          <div style={{
            backgroundColor: 'white',
            padding: '24px',
            borderRadius: '8px',
            width: '400px',
            maxWidth: '90vw'
          }}>
            <h3>Create New Journey</h3>
            <form onSubmit={handleCreateJourney}>
              <div style={{ marginBottom: '16px' }}>
                <label>Journey Title *</label>
                <input
                  type="text"
                  placeholder="e.g., Get Fit, Learn Guitar, Read More Books"
                  value={journeyForm.title}
                  onChange={(e) => setJourneyForm({...journeyForm, title: e.target.value})}
                  required
                  style={{
                    width: '100%',
                    padding: '8px',
                    border: '1px solid #ddd',
                    borderRadius: '4px',
                    marginTop: '4px'
                  }}
                />
              </div>
              <div style={{ marginBottom: '16px' }}>
                <label>Start Date</label>
                <input
                  type="date"
                  value={journeyForm.start_date}
                  onChange={(e) => setJourneyForm({...journeyForm, start_date: e.target.value})}
                  style={{
                    width: '100%',
                    padding: '8px',
                    border: '1px solid #ddd',
                    borderRadius: '4px',
                    marginTop: '4px'
                  }}
                />
              </div>
              <div style={{ display: 'flex', gap: '8px' }}>
                <button type="button" onClick={() => setShowJourneyModal(false)} style={{
                  flex: 1,
                  padding: '8px',
                  border: '1px solid #ddd',
                  borderRadius: '4px',
                  backgroundColor: 'white',
                  cursor: 'pointer'
                }}>
                  Cancel
                </button>
                <button type="submit" style={{
                  flex: 1,
                  padding: '8px',
                  border: 'none',
                  borderRadius: '4px',
                  backgroundColor: '#007bff',
                  color: 'white',
                  cursor: 'pointer'
                }}>
                  Create Journey
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Quest Modal */}
      {showQuestModal && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          backgroundColor: 'rgba(0,0,0,0.5)',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          zIndex: 1000
        }}>
          <div style={{
            backgroundColor: 'white',
            padding: '24px',
            borderRadius: '8px',
            width: '400px',
            maxWidth: '90vw'
          }}>
            <h3>Create New Quest</h3>
            <form onSubmit={handleCreateQuest}>
              <div style={{ marginBottom: '16px' }}>
                <label>Quest Title *</label>
                <input
                  type="text"
                  placeholder="e.g., Go to gym 3 times, Read 5 books"
                  value={questForm.title}
                  onChange={(e) => setQuestForm({...questForm, title: e.target.value})}
                  required
                  style={{
                    width: '100%',
                    padding: '8px',
                    border: '1px solid #ddd',
                    borderRadius: '4px',
                    marginTop: '4px'
                  }}
                />
              </div>
              <div style={{ display: 'flex', gap: '8px', marginBottom: '16px' }}>
                <div style={{ flex: 1 }}>
                  <label>Start Date</label>
                  <input
                    type="date"
                    value={questForm.start_date}
                    onChange={(e) => setQuestForm({...questForm, start_date: e.target.value})}
                    style={{
                      width: '100%',
                      padding: '8px',
                      border: '1px solid #ddd',
                      borderRadius: '4px',
                      marginTop: '4px'
                    }}
                  />
                </div>
                <div style={{ flex: 1 }}>
                  <label>Due Date (Optional)</label>
                  <input
                    type="date"
                    value={questForm.due_date}
                    onChange={(e) => setQuestForm({...questForm, due_date: e.target.value})}
                    style={{
                      width: '100%',
                      padding: '8px',
                      border: '1px solid #ddd',
                      borderRadius: '4px',
                      marginTop: '4px'
                    }}
                  />
                </div>
              </div>
              <div style={{ display: 'flex', gap: '8px' }}>
                <button type="button" onClick={() => setShowQuestModal(false)} style={{
                  flex: 1,
                  padding: '8px',
                  border: '1px solid #ddd',
                  borderRadius: '4px',
                  backgroundColor: 'white',
                  cursor: 'pointer'
                }}>
                  Cancel
                </button>
                <button type="submit" style={{
                  flex: 1,
                  padding: '8px',
                  border: 'none',
                  borderRadius: '4px',
                  backgroundColor: '#007bff',
                  color: 'white',
                  cursor: 'pointer'
                }}>
                  Create Quest
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Task Modal */}
      {showTaskModal && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          backgroundColor: 'rgba(0,0,0,0.5)',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          zIndex: 1000
        }}>
          <div style={{
            backgroundColor: 'white',
            padding: '24px',
            borderRadius: '8px',
            width: '400px',
            maxWidth: '90vw'
          }}>
            <h3>Create New Task</h3>
            <form onSubmit={handleCreateTask}>
              <div style={{ marginBottom: '16px' }}>
                <label>Task Description *</label>
                <input
                  type="text"
                  placeholder="e.g., Do 30 push-ups, Read chapter 1"
                  value={taskForm.body}
                  onChange={(e) => setTaskForm({...taskForm, body: e.target.value})}
                  required
                  style={{
                    width: '100%',
                    padding: '8px',
                    border: '1px solid #ddd',
                    borderRadius: '4px',
                    marginTop: '4px'
                  }}
                />
              </div>
              <div style={{ display: 'flex', gap: '8px' }}>
                <button type="button" onClick={() => setShowTaskModal(false)} style={{
                  flex: 1,
                  padding: '8px',
                  border: '1px solid #ddd',
                  borderRadius: '4px',
                  backgroundColor: 'white',
                  cursor: 'pointer'
                }}>
                  Cancel
                </button>
                <button type="submit" style={{
                  flex: 1,
                  padding: '8px',
                  border: 'none',
                  borderRadius: '4px',
                  backgroundColor: '#007bff',
                  color: 'white',
                  cursor: 'pointer'
                }}>
                  Create Task
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default Journeys;