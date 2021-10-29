import React, { useState, useEffect } from 'react'

import CourseCard from '../../component/CourseCard';
import SearchBox from '../../component/SearchBox';



const CourseList = () => {
    let endpoint = 'http://127.0.0.1:5000/enrolment/darrelwilde'

    const [course_backup, setcourse_backup] = useState([])
    const [coursesDetail, setCoursesDetail] = useState([])
    const [searchTerm, setSearchTerm] = useState('')
    // console.log(coursesDetail)
    useEffect(() => {    
        fetch(endpoint)
        .then((res) => res.json())
        
        .then((result) => {
        // console.log(result.data)
        
        setCoursesDetail(result.data)
        setcourse_backup(result.data)
        // console.log(coursesDetail)
        })

    }, [endpoint])

    useEffect(() => {
        const courselist = []
        course_backup.filter((val) =>{
            if (searchTerm === "") {
                // setCourses(val)
                courselist.push(val)
                console.log(val)

            } else if (val.course_name.toLowerCase().includes(searchTerm.toLowerCase())) {
                courselist.push(val)
                console.log(val)
                // setCourses([val])
            }
            return null
        })
        setCoursesDetail(courselist)
    },[searchTerm,course_backup])

    return (
        <div>
            <h1>My Course</h1>
            <SearchBox placeholder = 'Enter Name' handleChange = {(e) => setSearchTerm(e.target.value)}/>
            {coursesDetail.map(course => <CourseCard courseSchema={course} key={course.course_id}/>)}
        </div>
    )
}

export default CourseList
