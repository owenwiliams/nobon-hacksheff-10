import React from 'react';
import '../styles/Title.css';

function OdysseyTitle()
{
  return (
    <div>
        <div class="titleContainer">
            <p>Odyssey</p>
        </div>
        <div class = "titleBanner"></div>
    </div>
  );
}

function Odyssey() {
  return (
    <div>
      <OdysseyTitle />
      <p>Odyssey will be here</p>
    </div>
  );
}

export default Odyssey;