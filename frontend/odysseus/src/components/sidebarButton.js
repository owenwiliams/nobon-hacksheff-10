import React from 'react';
import '../sidebar.css';


// Make sure it accepts the prop (we called it toggleNav in App.jsx)
function SidebarButton({ toggleNav }) {
  return (
    <div className="buttonContainer">
      <button 
        className="openbtn" 
        onClick={toggleNav}
      >
        &#9776; 
      </button>
    </div>
  );
}

export default SidebarButton;