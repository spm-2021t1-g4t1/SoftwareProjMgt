import MainSidebarAdmin from '../component/MainSidebarAdmin.jsx';
import Home from './Home.jsx';
import Header from '../component/Header.jsx';
import '../App.css';

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
                <Route path = '/Administrator/EngineerList' component = {Home} exact/>
              </main>
            </CSSTransition>
        </div>
    );


}

export default AdminHome;