import React, { useState } from "react";
import './styles/App.css';
import SidebarButton from './components/SidebarButton';
import SidebarContent from './components/SidebarBody';
import Homepage from './pages/Home';
import CustomCalendar from './components/CustomCalendar';


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
        
        <Homepage />
		
      </div>
    </div>
  );
}

export default App;