import React, { useState, useEffect } from 'react'

import CourseCard from '../component/CourseCard';


const CourseList = () => {
    let endpoint = 'http://127.0.0.1:5000/enrolment/darrelwilde'
    
    const [coursesDetail, setCoursesDetail] = useState([])
    console.log(coursesDetail)
    useEffect(() => {    
        fetch(endpoint)
        .then((res) => res.json())
        
        .then((result) => {
        // console.log(result.data)
        
        setCoursesDetail(result.data)
        // console.log(coursesDetail)
        })

    }, [])

    return (
        <div>
            <h1>Course catalog</h1>
            {coursesDetail.map(course => <CourseCard courseSchema={course} key={coursesDetail.course_code}/>)}
        </div>
    )
}

export default CourseList
