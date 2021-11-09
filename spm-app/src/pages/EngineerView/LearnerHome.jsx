import MainSidebar from '../../component/MainSidebar.jsx';
import Home from '../Home.jsx';
import CourseList from './CourseList.jsx';
import Account from '../Account.jsx';
import Course from './Course.jsx';
import Catalog from './Catalog.jsx';
import Header from '../../component/Header.jsx';
import IndividualQuiz from '../../component/IndividualQuiz.jsx';
import TrainerCourseList from './TrainerCourseList.jsx';
import TakeQuiz from '../../component/TakeQuiz.jsx';
import React, { useEffect, useState } from 'react'
import { BrowserRouter ,Route, useHistory } from "react-router-dom"
import { CSSTransition } from 'react-transition-group' 


import '../../App.css';

function LearnerHome({handleLogout}) {
  const history = useHistory();
  const[showMenu, setShowMenu] = useState(true);

  function toggleSide() {
      if (showMenu == true) {
          setShowMenu(false)
      }
      else {
          setShowMenu(true)
      }
      console.log(showMenu)
  }

  useEffect(() => {
    const role = JSON.parse(localStorage.getItem("user")).role;
    // console.log(JSON.parse(localStorage.getItem("user")));
  });

  return (
      <div className="App">
        <Header func = {toggleSide} handleLogout={handleLogout}/>
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
            <main className = 'App-body'>
            {/* <Route path = '/' component = {Home} exact/>
              <Route path = '/course' component = {CourseList} exact/>
              <Route path = '/catalog' component = {Catalog} exact/>
              <Route path = '/course/:courseid/:classno/' component = {Course} />
              <Route path = '/account' component = {Account} exact/>
              <Route path = '/IndividualQuiz' component = {IndividualQuiz} exact/>
              <Route path = '/TakeQuiz' component = {TakeQuiz} exact/> */}
              <Route path = '/Engineer' component = {Home} exact/>
              <Route path = '/Engineer/course' component = {CourseList} exact/>
              <Route path = '/Engineer/trainer' component = {TrainerCourseList} exact/>
              <Route path = '/Engineer/catalog' component = {Catalog} exact/>
              <Route path = '/Engineer/course/:courseid/:classno/' component = {Course} />
              <Route path = '/Engineer/account' component = {Account} exact/>
              <Route path = '/Engineer/IndividualQuiz' component = {IndividualQuiz} exact/>
              <Route path = '/Engineer/TakeQuiz' component = {TakeQuiz} exact/>
            </main>
          </CSSTransition>
      </div>
  );
}

export default LearnerHome;
