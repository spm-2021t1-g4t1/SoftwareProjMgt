import React, { useState, useEffect } from 'react'

import CourseCard from '../component/CourseCard';


const CourseList = () => {
    let endpoint = 'http://127.0.0.1:5000/enrolment/darrelwilde'
    const [courses, setCourses] = useState([])

    useEffect(() => {    
        fetch(endpoint)
        .then((res) => res.json())
        
        .then((result) => {
        console.log(result.data)
        
        setCourses(result.data)
        })

    }, [])

    return (
        <div>
            <h1>Course catalog</h1>
            {courses.map(course => <CourseCard courseSchema={course} key={course.course_code}/>)}
        </div>
    )
}

export default CourseList
