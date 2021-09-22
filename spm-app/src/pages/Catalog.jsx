import React from 'react';
// import { Link } from "react-router-dom";
import axios from "axios";
import { useState, useEffect } from 'react';
import "../App.css";

const Catalog = () => {
    const endpoint = "https://spm-g4t1.hasura.app/v1/graphql";
    // const endpoint = "http://localhost:4000/get_course";        // TODO: update URL when microservices are hosted properly somewhere

    const [courses, setCourses] = useState([])
    
    // CALL MICROSERVICE - use if you're running microservice locally 
    // useEffect(() => {axios.get(endpoint)
    //     .then(res => {
    //         // console.log(res)
    //         setCourses(res.data.course_schema_course)
    //     })}, [])

    // return (
    //     <div style={{ margin: "auto", width: "75vw" }}>
    //         <h1>Course catalog</h1>
    //         {courses.map(course => <CourseCard courseSchema={course} key={course.course_code}/>)}
    //     </div>
    // )

    //  ----------------------- 

    // CALL DB DIRECTLY
    useEffect(() => {axios.post(endpoint, {
        query: `query getAllCourses {
            course_schema_course {
                course_code
                course_description
                course_name
                end_date
                start_date
            }
        }`
    }, {
        headers:
        {
            'content-type': 'application/json',
            'x-hasura-admin-secret': 'VzdZJkGQnpf3LdOqSq19hpvM6cCgL6OuwC0YYBxO72TYyLUFpsyBAp5uDC6kg5pQ'
        }
    })
        .then(res => {
            setCourses(res.data.data.course_schema_course)
        })}, [])

    return (
        <div style={{ margin: "auto", width: "75vw" }}>
            <h1>Course catalog</h1>
            {courses.map(course => <CourseCard courseSchema={course} key={course.course_code}/>)}
        </div>
    )
}

const CourseCard = ({courseSchema}) => {

    return(
        <div className="courseInfo-Section">
            <h2>{courseSchema.course_code} - {courseSchema.course_name}</h2>
            <p>Description: {courseSchema.course_description}</p>
            <p>Start date: {courseSchema.start_date}</p>
            <p>End date: {courseSchema.end_date}</p>
        </div>
    )
}

export default Catalog