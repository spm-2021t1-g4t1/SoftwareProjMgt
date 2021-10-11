import React from 'react'


const CourseDetail = (prop) => {
    // console.log(prop.data)
    
    return (
         <div className = 'courseDetail'>
            <div className = 'courseDetail-instructor'>
                <img className = 'Portait'src = '/images/logo.png' alt = 'Trainer Pic' />
                <p>{prop.data.trainer_name}</p>
            </div>
            <div className= 'courseDetail-others'>
                <div>
                    <p>Course Start Date:</p>
                    <p>{prop.data.start_date}</p>
                    <p>Course End Date:</p>
                    <p>{prop.data.end_date}</p>
                </div>
                <div>
                    <p>Course Start Time</p>
                    <p>{prop.data.start_time}</p>
                    <p>Course End Time:</p>
                    <p>{prop.data.end_time}</p>
                </div>
            </div>
        </div>
    )
}

export default CourseDetail
