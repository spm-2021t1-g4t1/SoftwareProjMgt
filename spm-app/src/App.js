import MainSidebar from './component/MainSidebar.jsx';
import Home from './pages/Home.jsx';
import CourseList from './pages/CourseList.jsx';
import Account from './pages/Account.jsx';
import Course from './pages/Course.jsx';
import Catalog from './pages/Catalog.jsx';
import Header from './component/Header.jsx';
import IndividualQuiz from './component/IndividualQuiz.jsx';

import React, { useState } from 'react'
import { BrowserRouter ,Route } from "react-router-dom"


import './App.css';

function App() {

  const[showMenu, setShowMenu] = useState(true)

  function toggleSide() {
      if (showMenu === true) {
          setShowMenu(false)
      }
      else {
          setShowMenu(true)
      }
      console.log(showMenu)
  }

  return (
    <BrowserRouter>
    <Header func = {toggleSide}/>
      <div className="App">
        <MainSidebar />
        <main>
              <Route path = '/' component = {Home} exact/>
              <Route path = '/course' component = {CourseList} exact/>
              <Route path = '/catalog' component = {Catalog} exact/>
              <Route path = '/course/:courseid/:classno/' component = {Course} />
              <Route path = '/account' component = {Account} exact/>
              <Route path = '/IndividualQuiz' component = {IndividualQuiz} exact/>
        </main>
      </div>
    </BrowserRouter>
    
    
  );
}

export default App;
