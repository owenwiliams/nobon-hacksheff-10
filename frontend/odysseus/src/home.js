import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import './greeting.css';

function GetGreetingText() {
  const currentHour = new Date().getHours();
  let greetingMessage = '';

  if (currentHour >= 5 && currentHour < 12) {
    greetingMessage = "GOOD MORNING,";
  }
  else if (currentHour >= 12 && currentHour < 18) {
    greetingMessage = "GOOD AFTERNOON,";
  }
  else if (currentHour >= 18 && currentHour < 22) {
    greetingMessage = "GOOD EVENING,";
  }
  else {
    // 9 PM (22) to 4 AM (4)
    greetingMessage = "GOOD NIGHT,";
  }
  return <div class="greetingText">{greetingMessage}</div>;
}

function DisplaySectionSeparation() {
  return (
      <div className="separationWaveContainer">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 200">
          <path
            fill="#1f2484"
            fillOpacity="1"
            d="M0,192L60,208C120,224,240,256,360,261.3C480,267,600,245,720,208C840,171,960,117,1080,106.7C1200,96,1320,128,1380,144L1440,160L1440,0L1380,0C1320,0,1200,0,1080,0C960,0,840,0,720,0C600,0,480,0,360,0C240,0,120,0,60,0L0,0Z"
            transform="scale(1, 0.4)"
          ></path>
        </svg>
      </div>
  )
}

const DisplayGreeting = () => {
  return (
    <>
      <div className="welcomeContainer">
        <GetGreetingText />
        <br />
        <p className="greetingName">ODYSSEUS</p>
        <br />
        <textarea
          id="userInput"
          name="userInput"
          className="userInput"
          style={{ backgroundColor: 'white' }}
          placeholder="Talk with Athena"
        ></textarea>
      </div>

      <DisplaySectionSeparation />
    </>
  );
};

function Homepage() {
    return (
    <DisplayGreeting />
    )   
}

export default Homepage;