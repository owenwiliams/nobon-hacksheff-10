import React from 'react';
import ReactDOM from 'react-dom/client';

import App from './App.jsx'; 

import '/public/index.css'; 
import '/public/athena.css';

const rootElement = document.getElementById('root');

ReactDOM.createRoot(rootElement).render(
    <App />
);