import React from 'react';
import axios from "axios";
import { useState, useEffect } from 'react';

// import "../App.css";

import CourseCard from '../component/CourseCard';


const Catalog = () => {
    const endpoint = "http://127.0.0.1:5000/course";
    const [courses, setCourses] = useState([])

    useEffect(() => {axios.get(endpoint, {
        headers:
        {
            'content-type': 'application/json',
            'x-hasura-admin-secret': 'VzdZJkGQnpf3LdOqSq19hpvM6cCgL6OuwC0YYBxO72TYyLUFpsyBAp5uDC6kg5pQ'
        }
    })
        .then(res => {
            console.log(res.data.data)
            setCourses(res.data.data)
        })}, [])
    

    return (
        <div>
            <h1>Course catalog</h1>
            {courses.map(course => <CourseCard courseSchema={course} key={course.course_id}/>)}
        </div>
    )
}


export default Catalog