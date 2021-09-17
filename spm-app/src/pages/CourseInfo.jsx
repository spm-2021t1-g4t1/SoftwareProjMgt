import React, { useState, useEffect } from 'react'
import { useParams } from "react-router-dom"
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faAward } from '@fortawesome/free-solid-svg-icons'


import CourseSidebar from '../component/CourseSidebar'
import CourseDetail from '../component/CourseDetail'

const CourseInfo = () => {
    // pull courseId from url
    const  courseid  = useParams().courseid
    
    //useState
    const[courseDetailArr, setCourseDetailArr] = useState({
        course_code: null,
        course_description: null,
        course_name: null,
        end_date: null,
        start_date: null,
        instructor: null,
        learning_objective : []})


    // pull api only once
    useEffect(() => {
        fetch('/jsonfiles/coursedata.json')
        .then(res => res.json()) 
        .then (
            (result) => {
                let course_Array = result.data.course_schema_course
                for ( let i of course_Array) {
                    if (i.course_code === courseid) {              
                        setCourseDetailArr({
                            course_code: i.course_code,
                            course_description: i.course_description,
                            course_name: i.course_name,
                            end_date: i.end_date,
                            start_date: i.start_date,
                            instructor: i.instructor,
                            learning_objective : i.learning_objective
                        })
                        console.log(courseDetailArr)

                    }
                }
            }
        )
    }, [courseid])
    
    
    
    return (
        <div>
            <div className ='courseInfo-Banner'>
                <h2 className = 'courseName-Banner'>{courseDetailArr['course_name']}</h2>
            </div>
            <div className = 'courseInfo'> 
                <div className = 'leftSection'>
                    <div className = 'courseDetail-Section'>
                        <h2>About this course</h2>
                        {courseDetailArr['course_description']}
                    </div>
                    <div className = 'courseInfo-Section'>
                        <h2>Training Objective</h2>
                        <ul>
                        {courseDetailArr['learning_objective'].map((objective,index) => 
                            <li key ={index}><FontAwesomeIcon icon ={faAward} />  {objective}</li>
                        )}
                        </ul>
                    </div>
                </div>
                <div className = 'rightSection'>
                    <CourseSidebar />
                    <CourseDetail data = {courseDetailArr} />
                </div>
            </div>
        </div>
        
    )
}

export default CourseInfo
