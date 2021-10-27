import React from 'react';
import axios from "axios";
import { useState, useEffect } from 'react';

// import "../App.css";

import CourseCard from '../component/CourseCard';
import SearchBox from '../component/SearchBox';


const Catalog = () => {
    const endpoint = "http://127.0.0.1:5000/catalog/darrelwilde";
    const [course_backup, setcourse_backup] = useState([])
    const [courses, setCourses] = useState([])
    const [searchTerm, setSearchTerm] = useState('')
    
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
            setcourse_backup(res.data.data)
        })}, [])
    
        
    useEffect(() => {
        const courselist = []
        course_backup.filter((val) =>{
            if (searchTerm === "") {
                // setCourses(val)
                courselist.push(val)
                // console.log(val)

            } else if (val.course_name.toLowerCase().includes(searchTerm.toLowerCase())) {
                courselist.push(val)
                // console.log(val)
                // setCourses([val])
            }
            return null
        })
        setCourses(courselist)
    },[searchTerm,course_backup])
    

    return (
        <div>
            <h1>Course catalog</h1>
            <SearchBox placeholder = 'Enter Name' handleChange = {(e) => setSearchTerm(e.target.value)}/>
            {courses.map(course => <CourseCard courseSchema={course} key={course.course_id}/>)}
        </div>
    )
}


export default Catalog