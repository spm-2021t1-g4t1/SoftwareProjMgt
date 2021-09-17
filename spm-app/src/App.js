import MainSidebar from './component/MainSidebar.jsx';
import Home from './pages/Home.jsx';
import Course from './pages/Course.jsx';
import CourseInfo from './pages/CourseInfo.jsx';

import { BrowserRouter ,Route } from "react-router-dom"

import './App.css';

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <MainSidebar />
        <Route path = '/' component = {Home} exact/>
        <Route path = '/course' component = {Course} exact/>
        <Route path = '/course/:courseid' component = {CourseInfo} exact/>
      </div>
    </BrowserRouter>
    
  );
}

export default App;
