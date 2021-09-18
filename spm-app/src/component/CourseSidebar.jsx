import React from 'react'
import { Link } from "react-router-dom"


const CourseSidebar = () => {

    // console.log(props)
    return (
        <div className = 'coursebar'>
            <div className = 'coursebar-header'>
                Resource
            </div>
            <div>
                <Link to = "./overview"> 
                    <div className ='coursebar-link'>
                        Overview
                    </div>
                </Link>
                <Link to = "./curriculum"> 
                    <div className ='coursebar-link'>
                        Curriculum
                    </div>
                </Link>
                <Link to = "./forum"> 
                    <div className ='coursebar-link'>
                        Course Forum
                    </div>
                </Link>
                <Link to = "./quiz"> 
                    <div className ='coursebar-link'>
                        Take Quiz
                    </div>
                </Link>
            </div>
        </div>
    )
}

export default CourseSidebar
