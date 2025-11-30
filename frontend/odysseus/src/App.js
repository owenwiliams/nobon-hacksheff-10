import React, { useState } from "react";
import './styles/App.css';
import SidebarButton from './components/SidebarButton';
import SidebarContent from './components/SidebarBody';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Homepage from './pages/Home';
import Athena from './pages/Athena';
import Journeys from './pages/Journeys';
import Odyssey from './pages/Odyssey';
import Journal from './pages/Journal';


// Define the width of the open sidebar for use in styling the main content
const SIDEBAR_WIDTH = '200px';


function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  // toggles sidebar depending on state
  const toggleSidebar = () => {
    setIsSidebarOpen(prev => !prev);
  };

  return (
    <Router>
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
          
              <Routes>
                <Route
                  path="/" 
                  element={<Homepage />} 
                />
                <Route 
                  path="/athena" 
                  element={<Athena />} 
                />
                <Route 
                  path="/journeys" 
                  element={<Journeys />} 
                />
                <Route 
                  path="/odyssey" 
                  element={<Odyssey />} 
                />
                <Route 
                  path="/journal" 
                  element={<Journal />} 
                />
              </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;