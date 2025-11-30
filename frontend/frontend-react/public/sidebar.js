let navbarOpen;

/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
function toggleNav() {
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


