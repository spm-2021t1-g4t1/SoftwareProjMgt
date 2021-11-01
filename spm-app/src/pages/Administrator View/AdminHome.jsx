import MainSidebarAdmin from '../../component/MainSidebarAdmin.jsx';
import EngineerDetails from './EngineerDetails.jsx';
import Header from '../../component/Header.jsx';
import ApprovalList from './ApprovalList.jsx';
import CourseAssignment from './CourseAssignment.jsx';
import CourseListAdmin from './CourseListAdmin.jsx';
// import '../App.css';

import React, { useEffect, useState } from 'react'
import { BrowserRouter ,Route } from "react-router-dom"
import { CSSTransition } from 'react-transition-group' 


const AdminHome = ({handleLogout}) => {
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
        <div className="App">
          <Header func = {toggleSide} handleLogout={handleLogout}/>
            <CSSTransition 
                in= {showMenu}
                classNames="slider-sidebar"
                timeout={{ enter: 1000, exit: 1000 }}
                >
                <MainSidebarAdmin />
            </CSSTransition>
            <CSSTransition 
                in= {showMenu}
                classNames="slider-body"
                timeout={{ enter: 1000, exit: 1000 }}
                >
              <main className = 'App-body'>
                {/* <Route path= "/Administrator/Dashboard" compents={Home} exact /> */}
                <Route path = '/Administrator/Course/unassigned' component = {CourseAssignment} exact/>
                <Route path = '/Administrator/Course/list' component = {CourseListAdmin} exact/>
                <Route path = '/Administrator/EngineerList' component = {EngineerDetails} exact/>
                <Route path = '/Administrator/Enrollment' component = {ApprovalList} exact />
              </main>
            </CSSTransition>
        </div>
    );


}

export default AdminHome;