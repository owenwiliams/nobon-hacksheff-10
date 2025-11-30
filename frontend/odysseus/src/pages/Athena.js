import React, { useState, useRef, useEffect } from 'react';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import CircularProgress from '@mui/material/CircularProgress';
import { athenaChat } from '../services/geminiApi';
import '../styles/Title.css';
import { useLocation } from 'react-router-dom'; // ← ADDED: Import useLocation

function AthenaTitle() {
  return (
    <div>
        <div class="titleContainer">
            <p class="athenaTitle">ATHENA</p>
        </div>
        <div class = "titleBanner"></div>
    </div>
  );
}

function Athena() {
  const location = useLocation();
  const [messages, setMessages] = useState([
    { id: 1, sender: 'ai', text: 'Hello, I am Athena. I am here to help you along your Odyssey... What do you need help with?' }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);
  const hasProcessedInitialMessage = useRef(false); // ← ADD THIS LINE

  // ADDED: Effect to handle initial message from home page
  useEffect(() => {
    if (location.state?.initialMessage && !hasProcessedInitialMessage.current) {
      hasProcessedInitialMessage.current = true; // ← PREVENT DUPLICATES
      handleSendInitialMessage(location.state.initialMessage);
    }
  }, [location.state?.initialMessage]); // ← FIXED DEPENDENCY

  // ADDED: Function to handle initial message from home page
  const handleSendInitialMessage = async (initialMessage) => {
    // Add user message
    const userMessage = {
      id: messages.length + 1,
      sender: 'user',
      text: initialMessage,
    };
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
      // Call the AI endpoint
      const aiResponse = await athenaChat({ prompt: initialMessage });
      
      // Add AI response
      const aiMessage = {
        id: messages.length + 2,
        sender: 'ai',
        text: aiResponse,
      };
      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      console.error('Error calling Athena:', error);
      const errorMessage = {
        id: messages.length + 2,
        sender: 'ai',
        text: 'Sorry, something went wrong. Please try again.',
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  // Auto-scroll to bottom when new messages arrive
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async () => {
    if (!input.trim()) return;

    // Add user message
    const userMessage = {
      id: messages.length + 1,
      sender: 'user',
      text: input,
    };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      // Call the AI endpoint
      const aiResponse = await athenaChat({ prompt: input });
      
      // Add AI response
      const aiMessage = {
        id: messages.length + 2,
        sender: 'ai',
        text: aiResponse,
      };
      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      console.error('Error calling Athena:', error);
      const errorMessage = {
        id: messages.length + 2,
        sender: 'ai',
        text: 'Sorry, something went wrong. Please try again.',
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const downloadConversation = () => {
    const conversationText = messages
      .map((msg) => `${msg.sender.toUpperCase()}: ${msg.text}`)
      .join('\n\n');

    const element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(conversationText));
    element.setAttribute('download', `athena-conversation-${new Date().toISOString().slice(0, 10)}.txt`);
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
  };

  return (
    <div>
      <AthenaTitle />
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
        <Button variant="outlined" size="small" onClick={downloadConversation}>
          Download Conversation
        </Button>
      </Box>

      <Box sx={{ height: '500px', display: 'flex', flexDirection: 'column', border: '1px solid #ccc', p: 2 }}>
        {/* Messages Area */}
        <Box sx={{ flexGrow: 1, overflow: 'auto', mb: 2 }}>
          {messages.map((message) => (
            <Box
              key={message.id}
              sx={{
                display: 'flex',
                justifyContent: message.sender === 'ai' ? 'flex-start' : 'flex-end',
                mb: 1,
              }}
            >
              <Paper
                sx={{
                  p: 2,
                  maxWidth: '70%',
                  bgcolor: message.sender === 'ai' ? 'grey.100' : 'primary.main',
                  color: message.sender === 'ai' ? 'text.primary' : 'white',
                }}
              >
                <Typography>{message.text}</Typography>
              </Paper>
            </Box>
          ))}
          {loading && (
            <Box sx={{ display: 'flex', justifyContent: 'flex-start', mb: 1 }}>
              <CircularProgress size={30} />
            </Box>
          )}
          <div ref={messagesEndRef} />
        </Box>

        {/* Input Area */}
        <Box sx={{ display: 'flex', gap: 1, flexShrink: 0 }}>
          <TextField
            fullWidth
            placeholder="Type your message..."
            variant="outlined"
            size="small"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            disabled={loading}
          />
          <Button
            variant="contained"
            onClick={handleSendMessage}
            disabled={loading || !input.trim()}
          >
            {loading ? 'Sending...' : 'Send'}
          </Button>
        </Box>
      </Box>
    </div>
  );
}

export default Athena;