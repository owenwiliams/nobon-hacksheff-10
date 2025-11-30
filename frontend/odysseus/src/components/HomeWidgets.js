import React, { useState } from "react";
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { DateCalendar } from '@mui/x-date-pickers/DateCalendar';

function WidgetCardStreak(props) {
  const { streakValue, iconPath } = props;

  const cardStyle = { 
    width: '400px', 
    border: 'none',
  };
  
  const titleStyle = {
    color: '#ffaa00ff',
    textShadow: '0 0 20px rgba(255, 196, 0, 0.55)',
    fontSize: '3em',
    fontWeight: 'bolder',
    fontFamily: 'Greek Dalek',
    marginTop: -10, 
  };

  const textStyle = {
    color: '#000000ff',
    fontSize: '2.2em',
    fontFamily: 'Segoe UI',
    fontStyle: 'italic',
    fontWeight: '600',
    marginTop: '-10px', 
    marginBottom: 0, 
  };
  
  const bodyStyle = {
    display: 'flex',      
    alignItems: 'center', 
    gap: '20px',          
  };

  const imageStyle = {
    width: '240px',
    height: '240px',
  };

  const divStyle = {
    marginLeft: '-80px',
    marginRight: '80px',
  };

  return (
    <div className="widgetContainer">
      <div className="card" style={cardStyle}>
        <div className="card-body" style={bodyStyle}>
          
          <img 
            src={iconPath} // changes based on the streak
            alt="Streak Icon" 
            style={imageStyle} 
          />
          
          <div style={divStyle}> 
            <p className="card-title" style={titleStyle}>{streakValue}</p> 
            <p className="card-text" style={textStyle}>divine favour</p>
          </div>
          
        </div>
      </div>
    </div>
  );
}

// Define image paths (replace these with your actual image files)
const ICON_PATHS = {
  NONE: 'images/streakicon.png',
  SMALL: 'images/streakiconLow.png',
  MEDIUM: 'images/streakiconMed.png',
  LARGE: 'images/streakiconHigh.png',
};

function StreakCounter() {
  // Use useState to manage the streak number. Start it at 42.
  const [streak, setStreak] = useState(0); 

  let currentIconPath;

  if (streak >= 30) {
    currentIconPath = ICON_PATHS.LARGE;
  } else if (streak >= 10) {
    currentIconPath = ICON_PATHS.MEDIUM;
  } else if (streak > 0){
    currentIconPath = ICON_PATHS.SMALL;
  }
  else{
    currentIconPath = ICON_PATHS.NONE;
  }

  // Example function to update the streak (for testing/future interaction)
  // You can call this from a button click, for instance.
  const incrementStreak = () => {
    setStreak(prevStreak => prevStreak + 1);
  };
  const incrementStreak10 = () => {
    setStreak(10);
  };
  const incrementStreak30 = () => {
    setStreak(30);
  };
  
  return (
    <div>
      <WidgetCardStreak 
        streakValue={streak} 
        iconPath={currentIconPath} 
      />

      <button onClick={incrementStreak}>+1</button>
      <button onClick={incrementStreak10}>10</button>
      <button onClick={incrementStreak30}>30</button>
    </div>
  );
}

function WidgetCardCalendar() {
  const cardStyle = { 
    width: '400px', 
  };

  const titleStyle = {
    color: 'red',
    fontSize: '1.5em',
    fontWeight: 'bold',
  };

  const textStyle = {
    color: 'red',
    fontSize: '1.5em',
    fontWeight: 'bold',
  };
  
  return (
    <div className="widgetContainer">
      <br /> 
      <div className="card" style={cardStyle}>
        <div className="card-body">
          <p className="card-title" style={titleStyle}>abc</p> 
          <p className="card-text" style={textStyle}>abcdef</p>
        </div>
      </div>
    </div>
  );
}

function CustomCalendar() {
    return (
      <div>
        <LocalizationProvider dateAdapter={AdapterDayjs}>
            <DateCalendar />
        </LocalizationProvider>
      </div>
    );
}

function CardLayout() {
  const layoutStyle = {
    display: 'flex',
    gap: '100px',
    justifyContent: 'center',
    padding: '20px'
  };

return (
    <div style={layoutStyle}>
      <StreakCounter /> 
      <CustomCalendar /> 
    </div>
  );
}

export default function DisplayWidgets() {
  return <CardLayout />;
}
