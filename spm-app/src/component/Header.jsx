import React, { useEffect, useState } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faBars, faInbox, faBell } from '@fortawesome/free-solid-svg-icons'
import { Navbar, Container } from 'react-bootstrap';

const Header = (prop) => {
    return (

        <Navbar fixed="top" bg="dark" variant="dark">
            <Container>
                <Navbar.Brand href="/">
                    <img
                    alt=""
                    src="/images/logo.png"
                    width="30"
                    height="30"
                    className="d-inline-block align-top"
                    />{' '}
                Owl Learning Management System
                </Navbar.Brand>
                <Navbar.Collapse className="justify-content-end">
                    <Navbar.Text className = 'mx-1'>
                        <FontAwesomeIcon icon={faInbox} />
                    </Navbar.Text>
                    <Navbar.Text className = 'mx-1'>
                        <FontAwesomeIcon icon={faBell} />
                    </Navbar.Text>
                    <Navbar.Text>
                        Signed in as: <a href="#login">David Wilde</a>
                    </Navbar.Text>
                </Navbar.Collapse>
            </Container>
        </Navbar>

    )
}

export default Header
