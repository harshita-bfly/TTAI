import logo from './logo.svg';
import './App.css';
import Navbar from './components/Navbar/Navbar';
import Sidebar from './components/Sidebar/Sidebar';

function App() {
  return (
    <div className="App">
      <Navbar/>
      <div className='content'>
        <div className='side'>
        <Sidebar/>
        </div>
        <div className='hello'>
          Hello
        </div>
      </div>
    </div>
  );
}

export default App;
