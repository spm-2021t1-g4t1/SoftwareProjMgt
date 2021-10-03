import MainSidebar from './component/MainSidebar.jsx';
import Home from './pages/Home.jsx';
import CourseList from './pages/CourseList.jsx';
import Account from './pages/Account.jsx';
import Course from './pages/Course.jsx';
import Catalog from './pages/Catalog.jsx';
import Header from './component/Header.jsx';

import React, { useEffect, useState } from 'react'
import { BrowserRouter ,Route } from "react-router-dom"
import { CSSTransition } from 'react-transition-group' 


import './App.css';

function App() {

  const[showMenu, setShowMenu] = useState(true)

  function toggleSide() {
      if (showMenu == true) {
          setShowMenu(false)
      }
      else {
          setShowMenu(true)
      }
      console.log(showMenu)
  }

  return (
    <BrowserRouter>
      <div className="App">
        <Header func = {toggleSide}/>
          <CSSTransition 
              in= {showMenu}
              classNames="slider-sidebar"
              timeout={{ enter: 1000, exit: 1000 }}
              >
              <MainSidebar />
          </CSSTransition>
          <CSSTransition 
              in= {showMenu}
              classNames="slider-body"
              timeout={{ enter: 1000, exit: 1000 }}
              >
            <div className = 'App-body'>
              <Route path = '/' component = {Home} exact/>
              <Route path = '/course' component = {CourseList} exact/>
              <Route path = '/catalog' component = {Catalog} exact/>
              <Route path = '/course/:courseid/:classno/' component = {Course} />
              <Route path = '/account' component = {Account} exact/>
            </div>
          </CSSTransition>
      </div>
    </BrowserRouter>
    
    
  );
}

export default App;
