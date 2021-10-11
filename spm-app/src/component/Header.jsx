import React, { useEffect, useState } from 'react'
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
                    <FontAwesomeIcon className = 'header-icon' icon={faInbox} />
                    <FontAwesomeIcon className = 'header-icon' icon={faBell} />
                    <img className ='profile-pic' src ='/images/feAvatar.jpg' />
                </div>
            </header>

    )
}

export default Header
