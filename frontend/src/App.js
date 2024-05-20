import logo from './logo.svg';
import './App.css';
import Navbar from './components/Navbar/Navbar';
import Sidebar from './components/Sidebar/Sidebar';
import Question from './pages/Questions/Question';

function App() {
  return (
    <div className="App">
      <Question></Question>
    </div>
  );
}

export default App;
