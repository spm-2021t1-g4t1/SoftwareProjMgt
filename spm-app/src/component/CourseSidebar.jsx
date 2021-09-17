import React from 'react'

const CourseSidebar = () => {

    // console.log(props)
    return (
        <div className = 'coursebar'>
            <div className = 'coursebar-header'>
                Resource
            </div>
            <div>
                <div className ='coursebar-link'>
                    Overview
                </div>
                <div className ='coursebar-link'>
                    Curriculum
                </div>
                <div className ='coursebar-link'>
                    Course Forum
                </div>
                <div className ='coursebar-link'>
                    Take Quiz
                </div>
            </div>
        </div>
    )
}

export default CourseSidebar
