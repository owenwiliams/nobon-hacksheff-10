import React from 'react';
import '../styles/Sidebar.css';
import { BrowserRouter, Link } from 'react-router-dom';

// Component receives the state and width from the parent App
function SidebarContent({ isOpen, sidebarWidth }) {


  

  return (
    <nav 
      id="mySidebar" 
      className="sidebar"
      style={{
        // Sets width based on the isOpen prop: 200px or 0
        width: isOpen ? sidebarWidth : '0',
        transition: 'width 0.5s', // Smooth transition effect
      }}
    >

        <Link to="/" className="nav-item">
          Home
        </Link>

        <Link to="/athena" className="nav-item">
          Athena
        </Link>
      
        <Link to="/journeys" className="nav-item">
          Journeys
        </Link>
            
        <Link to="/odyssey" className="nav-item">
          Odyssey
        </Link>
            
        <Link to="/journal" className="nav-item">
          Journal
        </Link>
      
    </nav>
  );
}

export default SidebarContent;