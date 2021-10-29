import React, { useState, useEffect } from 'react'
import { OverlayTrigger, Popover, Button } from 'react-bootstrap';

import ClassCard from './ClassCard';

const CourseCard = (prop) => {

    // console.log('prop')

    const courseSchema = prop.courseSchema
    const prerequisiteCourse = courseSchema.prerequisite_courses

    console.log(courseSchema.prerequisite_courses)

    const [stateChange, setStateChange] = useState(0)
    const [inQueue, setInQueue] = useState([])
    const hasPrerequisites = courseSchema.prerequisite_courses.length > 0
    // console.log(hasPrerequisites)
    function classChange() {
        setStateChange(stateChange+1)
    }

    const endpoint = `http://127.0.0.1:5000/queue/darrelwilde/${courseSchema.course_id}`

    useEffect(() => {
        fetch(endpoint)
        .then((res) => res.json()) 
        .then((result) => {
        // console.log(result)
        setInQueue(result)
        })
    },[stateChange])
        
    const popover = (
        <Popover id="popover-basic">
          <Popover.Header as="h3">Prerequisites Course</Popover.Header>
          <Popover.Body>
            {prerequisiteCourse.map((course,index) => <p key={index}>{course.prerequisite_course_id}. {course.prerequisite_course_name}</p>)}
          </Popover.Body>
        </Popover>
      );
      

    return(
        <div className= 'my-4' > 
            <div class Name="border border-info container-fluid container-bg">    
                <h2 className="p-1">{courseSchema.course_id} - {courseSchema.course_name}
                    {hasPrerequisites 
                    ?   <OverlayTrigger trigger="click" placement="bottom" overlay={popover}>
                            <Button className = 'mx-2 'variant = 'outline-secondary'>Prerequisites</Button>
                        </OverlayTrigger>
                    : ""
                    }
                    

                </h2>
                <p className="p-2">Description: {courseSchema.description}</p>
            </div>
            {courseSchema.classes.map(classes => <ClassCard 
                                                    classChange = {classChange} classSchema={classes} inQueue = {inQueue} hasPrereq = {hasPrerequisites}
                                                    key={courseSchema.course_id-classes.class_no}/>)}
        
        </div>
        
    )
}


export default CourseCard