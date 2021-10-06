import React, { useEffect, useState } from 'react'
import { useHistory } from 'react-router'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faBars, faInbox, faBell } from '@fortawesome/free-solid-svg-icons'


const Header = (prop) => {
    return (
            <header>
                <div className = 'left-header'>
                    <button onClick = {prop.func} className = 'header-icon collapse-menu '><FontAwesomeIcon className = 'header-icon' icon={faBars} /></button>
                    <img className ='sideImg' src ='/images/logo.png' alt = 'logo'/>
                </div>

                <div className = 'right-header'>
                    <button onClick={prop.handleLogout}>Logout</button>
                    <FontAwesomeIcon className = 'header-icon' icon={faInbox} />
                    <FontAwesomeIcon className = 'header-icon' icon={faBell} />
                    <img className ='profile-pic' src ='/images/feAvatar.jpg' />
                </div>
            </header>

    )
}

export default Header
