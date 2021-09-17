//Imports
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUser, faHome, faBookReader, faComment, faCommentDots } from '@fortawesome/free-solid-svg-icons'
import { Link } from "react-router-dom"

// Modules
import React from 'react'

const MainSidebar = () => {
    return (
        <div className = "sidebar">
            <div className = 'sidebar-banner'>
                <img className ='sideImg' src ='/images/logo.png' />
            </div>
            <Link  to = '/'> 
                <div className = 'sidebar-link'>
                    <FontAwesomeIcon icon ={faHome} /> Home
                </div>
            </Link>
            <Link to = '/course'>
                <div className = 'sidebar-link'>
                 <FontAwesomeIcon icon ={faBookReader} />  Course
                </div>
            </Link>
            <Link to = '/'> 
                <div className = 'sidebar-link'>
                    <FontAwesomeIcon icon ={faComment} />  Forum
                </div>
            </Link>
            <Link to = '/account'>
                <div className = 'sidebar-link'>
                <FontAwesomeIcon icon ={faUser} /> Account
                </div>
            </Link>
            <Link to = '/'>
                <div className = 'sidebar-link'>
                    <FontAwesomeIcon icon ={faCommentDots} /> Mesages
                </div>
            </Link>
        </div>
    )
}

export default MainSidebar
