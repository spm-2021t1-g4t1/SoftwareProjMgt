import React from 'react';
import { Link } from "react-router-dom";
import axios from "axios";
import { useState, useEffect } from 'react';
import "../App.css";

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
            // console.log(res.data.data)
            setCourses(res.data.data)
        })}, [])

    return (
        <div>
            <h1>Course catalog</h1>
            {courses.map(course => <CourseCard courseSchema={course} key={course.course_code}/>)}
        </div>
    )
}

const CourseCard = ({courseSchema}) => {

    // console.log(courseSchema)

    return(
        <div> 
            <div className="Catalog-Section">    
                <h2>{courseSchema.course_id} - {courseSchema.course_name}</h2>
                <p>Description: {courseSchema.description}</p>
            </div>
            {courseSchema.classes.map(classes => <ClassCard classSchema={classes} key={courseSchema.course_code - classes.class_no}/>)}
        </div>
        
    )
}

const ClassCard = ({classSchema}) => {
    console.log(classSchema)

    return(
        <div className="class-Section">
            <h2>Class {classSchema.class_no}</h2>
            <p className = 'class-text'>Slot: {classSchema.class_size}</p>
            <div className = 'class-timing'>
                <div className = 'class-text'>
                    <p>Start date: {classSchema.start_date}</p>
                    <p>End date: {classSchema.end_date}</p>
                </div>
                <div className = 'class-text'>
                    <p>Start Time: {classSchema.start_time}</p>
                    <p>End Time: {classSchema.end_time}</p>
                </div>
            </div>
        </div>
    )
}

export default Catalog