import React, { useState, useEffect } from 'react'

import ClassCard from './ClassCard';

const CourseCard = (prop) => {

    // console.log('prop')

    const courseSchema = prop.courseSchema

    const [stateChange, setStateChange] = useState(false)
    const [inQueue, setInQueue] = useState([])

    function classChange() {
        setStateChange(true)
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
        
    

    return(
        <div> 
            <div className="Catalog-Section">    
                <h2>{courseSchema.course_id} - {courseSchema.course_name}</h2>
                <p>Description: {courseSchema.description}</p>
            </div>
            {courseSchema.classes.map(classes => <ClassCard 
                                                    classChange = {classChange} classSchema={classes} inQueue = {inQueue}
                                                    key={courseSchema.course_id-classes.class_no}/>)}

        </div>
        
    )
}


export default CourseCard