import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';

export default function HomeAthenaChatbox() {
  return (
    <Box
      component="form"
      sx={{ '& .MuiTextField-root': { m: 1, width: '50vw', borderRadius: 5,} }}
      noValidate
      autoComplete="off"
    >
        <div>
            <TextField
                id="outlined-multiline-flexible"
                placeholder="Ask Athena..."
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



