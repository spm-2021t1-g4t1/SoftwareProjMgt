import MainSidebar from './component/MainSidebar.jsx';
import Home from './pages/Home.jsx';
import CourseList from './pages/CourseList.jsx';
import Account from './pages/Account.jsx';
import Course from './pages/Course.jsx';
import Catalog from './pages/Catalog.jsx';

import { BrowserRouter ,Route } from "react-router-dom"

import './App.css';

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <MainSidebar />
        <Route path = '/' component = {Home} exact/>
        <Route path = '/course' component = {CourseList} exact/>
        <Route path = '/catalog' component = {Catalog} exact/>
        <Route path = '/course/:courseid' component = {Course} />
        <Route path = '/account' component = {Account} exact/>
      </div>
    </BrowserRouter>
    
  );
}

export default App;
