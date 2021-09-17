import React from 'react'

const CourseDetail = (prop) => {

    console.log(prop.data)
    return (
         <div className = 'courseDetail'>
            <div className = 'courseDetail-instructor'>
                <img className = 'Portait'src = '/images/logo.png' />
                <p>{prop.data.instructor}</p>
            </div>
            <div className= 'courseDetail-others'>
                <p>Course Start Date:</p>
                <p>{prop.data.start_date}</p>
                <p>Course End Date:</p>
                <p>{prop.data.end_date}</p>
            </div>
        </div>
    )
}

export default CourseDetail
