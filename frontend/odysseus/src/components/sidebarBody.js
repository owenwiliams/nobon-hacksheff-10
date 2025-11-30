import React from 'react';
import '../styles/Sidebar.css';

// Component receives the state and width from the parent App
function SidebarContent({ isOpen, sidebarWidth }) {
  return (
    <div 
      id="mySidebar" 
      className="sidebar"
      style={{
        // Sets width based on the isOpen prop: 200px or 0
        width: isOpen ? sidebarWidth : '0',
        transition: 'width 0.5s', // Smooth transition effect
      }}
    >
      <a href="#">Home</a>
      <a href="#">Athena</a>
      <a href="#">Quests</a>
      <a href="#">Odyssey</a>
      <a href="#">Journal</a>
    </div>
  );
}

export default SidebarContent;