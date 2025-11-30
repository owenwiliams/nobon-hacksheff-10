import React from 'react';
import IndeterminateCheckbox from '/IndeterminateCheckbox';

const Journeys = () => {
  return (
    <div>
      <h1>Task Selection</h1>
      
      <IndeterminateCheckbox /> 

      <p>This component demonstrates how a parent checkbox can reflect the state of its children.</p>
    </div>
  );
};

export default Journeys;