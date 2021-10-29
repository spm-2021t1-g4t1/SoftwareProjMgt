import React from 'react'
import { Image } from 'react-bootstrap';



const CourseDetail = (prop) => {
    // console.log(prop.data)
    
    return (
         <div className = 'border border-info container-bg text-center my-3'>
            <div className = 'courseDetail-instructor'>
                <Image className = 'instructor-image'src="/images/logo.png" roundedCircle />
                <p>{prop.data.trainer_name}</p>
            </div>
            <div className= 'courseDetail-others'>
                <div className= 'my-2'>
                    <div>Course Start Date:</div>
                    <div>{prop.data.start_date}</div>
                    <div>Course End Date:</div>
                    <div>{prop.data.end_date}</div>
                </div>
                <div className= 'my-2'>
                    <div>Course Start Time</div>
                    <div>{prop.data.start_time}</div>
                    <div>Course End Time:</div>
                    <div>{prop.data.end_time}</div>
                </div>
            </div>
        </div>
    )
}

export default CourseDetail
