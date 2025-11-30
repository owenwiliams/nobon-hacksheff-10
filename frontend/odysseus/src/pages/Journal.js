import React, { useState } from 'react';
import { DateCalendar } from '@mui/x-date-pickers/DateCalendar';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import dayjs from 'dayjs'; // Recommended date library
import '../styles/Title.css';
import '../styles/Journal.css';

function JournalTitle()
{
  return (
    <div>
        <div class="titleContainer">
            <p class="athenaTitle">JOURNAL</p>
        </div>
        <div class = "titleBanner"></div>
    </div>
  );
}

const CustomCalendar = () => {
  // 1. Initialize state with a Dayjs object or null/undefined
  const [selectedDate, setSelectedDate] = useState(dayjs()); 

  // 2. Handler to retrieve and process the new date
  const handleDateChange = (newDate) => {
    setSelectedDate(newDate);
    
    // The newDate argument is a Dayjs object. 
    // You can access the underlying JavaScript Date object like this:
    const jsDate = newDate.toDate(); 
    
    console.log("Selected Dayjs Object:", newDate);
    console.log("Selected JS Date:", jsDate);
  };

  return (
    // The LocalizationProvider is essential for the calendar to work.
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <div style={{ padding: 20, maxWidth: '100%', maxHeight: 800, }}>
        
        <DateCalendar 
          value={selectedDate} 
          onChange={handleDateChange} 
sx={{
  // 1. Overall Calendar Container Sizing
  width: '90%',          // Keeps the large, wide appearance
  maxWidth: 900,         // Slightly reduced max width
  
  // Adjusted height: Slightly reduced from 80vh and removed overflow setting
  // This height should now be comfortably larger than the content.
  height: '75vh',       
  maxHeight: 900,        
  margin: '0 auto',     
  
  // Ensure the internal layout fills the container
  '& .MuiPickersLayout-root, & .MuiDateCalendar-root': {
    width: '100%',
    height: '100%',
  },

  // 2. Responsive and Large Sizing for Individual Day Cells
  '& .MuiPickersDay-root': {
    // Slight reduction in base cell size (from 4.5vw)
    width: '4vw',    
    height: '4vw',   
    minWidth: 45,      
    minHeight: 45,     
    fontSize: '1.4rem', 
    
    '@media (min-width: 600px)': {
      width: '4.5vw', // Max cell size on wider screens
      height: '4.5vw',
      minWidth: 55,
      minHeight: 55,
      fontSize: '1.7rem',
    },
    
    // Maintain vertical spacing
    margin: '3px',
  },
  
  // 3. Header/Title and Spacing (Slightly Reduced Padding)
  '& .MuiPickersCalendarHeader-root': {
    fontSize: '2.2rem',
    padding: '20px 0', // Slightly reduced vertical padding
  },

  '& .MuiDayCalendar-weekDayLabel': {
    fontSize: '1.4rem',
  },
  
  '& .MuiDayCalendar-weekContainer': {
    margin: '8px 0', // Slightly reduced margin between weeks
  }
}}
        />
        
        <h3>Selected Date</h3>
        {/* Display the formatted date */}
        <p>{selectedDate.format('dddd, MMMM D, YYYY')}</p>
        
      </div>
    </LocalizationProvider>
  );
};


function Journal() {
  return (
    <div>
      <JournalTitle />
      <div  >
        <CustomCalendar />
      </div>
    </div>
  );
}


export default Journal;