import React from 'react'
import { Link } from "react-router-dom"


const Course = () => {
    return (
        <div style={{textAlign: "center"}}>
            <p>Course Page</p>
            <div>
                <Link to = '/course/ENG101'><button> Click here to ENG101</button></Link>
            </div>
            <div>
                <Link to = '/course/ENG102'><button> Click here to ENG102</button></Link>
            </div>
            <div>
                <Link to = '/course/ENG103'><button> Click here to ENG103</button></Link>
            </div>
        </div>
    )
}

export default Course
