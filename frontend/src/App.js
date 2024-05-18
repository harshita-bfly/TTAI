import logo from './logo.svg';
import './App.css';
import Navbar from './components/Navbar/Navbar';
import Sidebar from './components/Sidebar/Sidebar';
import Journey from './components/Journey/Journey';
import Upcoming from './components/Upcoming/Upcoming';

function App() {
  return (
    <div className="App">
      <Navbar/>
      <div className='content'>
        <div className='side'>
        <Sidebar/>
        </div>
        <div className='jour'>
          <Journey/>
        </div>
        <div className='up'>
          <Upcoming/>
        </div>
      </div>
    </div>
  );
}

export default App;
