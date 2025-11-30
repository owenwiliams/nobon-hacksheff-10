import React from 'react';

let navbarOpen;

function toggleSidebar() {
  if (!navbarOpen)
  {
    document.getElementById("mySidebar").style.width = "200px";
    document.getElementById("main").style.marginLeft = "200px";
    navbarOpen = true;
  }
  else
  {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    navbarOpen = false;
  }
}

function SidebarButton() {
  return (
    <div className="buttonContainer">
      <button 
        className="openbtn" 
        onClick={toggleSidebar}
      >
        &#9776; 
      </button>
    </div>
  );
}

export default SidebarButton;