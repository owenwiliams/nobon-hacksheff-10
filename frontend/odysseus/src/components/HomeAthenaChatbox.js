import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';

export default function HomeAthenaChatbox() {
  const navigate = useNavigate();
  const [inputValue, setInputValue] = useState('');

  const handleSubmit = (e) => {
    if (e) {
      e.preventDefault();
    }
    
    if (inputValue.trim()) {
      // Navigate to Athena page with the message as state
      navigate('/athena', { 
        state: { 
          initialMessage: inputValue.trim() 
        } 
      });
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  return (
    <Box
      component="form"
      onSubmit={handleSubmit}
      sx={{ '& .MuiTextField-root': { m: 1, width: '50vw', borderRadius: 5,} }}
      noValidate
      autoComplete="off"
    >
        <div>
            <TextField
                id="outlined-multiline-flexible"
                placeholder="Ask Athena..."
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                onKeyPress={handleKeyPress}
                multiline
                maxRows={4}
                sx={{ 
                  backgroundColor: 'white', 
                  "& fieldset": { border: 'none' },
                  '& .MuiOutlinedInput-root':
                  {
                    transition: 'all 0.5s ease-in-out'
                  },
                  '& .MuiInputBase-root.Mui-focused':
                  {
                    borderRadius: 5,
                    boxShadow: '0 0 40px rgba(127, 187, 251, 0.673)',
                    transition: '0.5s',
                  },
                  '& .MuiOutlinedInput-root:focus-within':
                  {
                    outline: 'none',
                  },
                }}
            />
        </div>
    </Box>
  );
}