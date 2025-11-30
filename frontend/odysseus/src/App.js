import React, { useState } from "react";
import './App.css';
import Calendar from './components/calendar';
import SidebarButton from './components/sidebarButton';
import SidebarContent from './components/sidebarBody';
import Homepage from './home';
import CustomCalendar from './components/CustomCalendar';
import HomeAthenaChatbox from './components/HomeAthenaChatbox';

// Define the width of the open sidebar for use in styling the main content
const SIDEBAR_WIDTH = '200px';


function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  // toggles sidebar depending on state
  const toggleSidebar = () => {
    setIsSidebarOpen(prev => !prev);
  };

  return (
    <div className="App">      
      <SidebarContent isOpen={isSidebarOpen} sidebarWidth={SIDEBAR_WIDTH} />
      
      <div 
        className="main"
        style={{
          marginLeft: isSidebarOpen ? SIDEBAR_WIDTH : '0',
          transition: 'margin-left 0.5s'
        }}
      >
        {/* -------- content ----------*/}
        <SidebarButton toggleNav={toggleSidebar} />
        
		<h1>Odysseus</h1>
        <Homepage />

        <h2>Calendar</h2>
        <CustomCalendar />
        <h2>button</h2>
        <HomeAthenaChatbox /> 
		
      </div>
    </div>
  );
}

export default App;