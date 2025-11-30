import './App.css';
import CustomCalendar from './components/CustomCalendar';
import CustomSidebar from './components/CustomSidebar';
import HomeAthenaChatbox from './components/HomeAthenaChatbox';

function App() {

  return (
    <div className="App">
        <h1>Odysseus</h1>

        <h2>Calendar</h2>
        <CustomCalendar />
        <h2>button</h2>
        <HomeAthenaChatbox />   
    </div>
  );
}

export default App;