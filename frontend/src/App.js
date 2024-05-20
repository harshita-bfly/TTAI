import logo from './logo.svg';
import './App.css';
import Navbar from './components/Navbar/Navbar';
import Sidebar from './components/Sidebar/Sidebar';
import Journey from './components/Journey/Journey';
import Upcoming from './components/Upcoming/Upcoming';
import Question from './pages/Questions/Question';

function App() {
  return (
    <div className="App">
      <Question></Question>
    </div>
  );
}

export default App;
