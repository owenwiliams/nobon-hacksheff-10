import React from 'react';
import '../styles/Title.css';

function AthenaTitle()
{
  return (
    <div>
        <div class="titleContainer">
            <p class="athenaTitle">ATHENA</p>
        </div>
        <div class = "titleBanner"></div>
    </div>
  );
}

function Athena() {
  return (
    <div>
      <AthenaTitle />
    </div>
  );
}

export default Athena;