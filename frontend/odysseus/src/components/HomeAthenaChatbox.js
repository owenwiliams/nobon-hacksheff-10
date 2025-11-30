import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';


export default function HomeAthenaChatbox() {
  return (
    <Box
      component="form"
      sx={{ '& .MuiTextField-root': { m: 1, width: '25ch' } }}
      noValidate
      autoComplete="off"
    >
        <div>
            <TextField
                id="outlined-multiline-flexible"
                placeholder="Ask Athena...."
                multiline
                maxRows={4}
            />
        </div>
    </Box>
  );
}



