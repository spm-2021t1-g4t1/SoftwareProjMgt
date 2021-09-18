import React, { useState, useEffect } from 'react'
import { useParams } from "react-router-dom"
import {  Link, BrowserRouter ,Route } from "react-router-dom"

import CourseInfo from './CourseInfo'
import CourseSidebar from '../component/CourseSidebar'
import CourseDetail from '../component/CourseDetail'
import Section from './Section'


const Course = () => {
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
                        // console.log(courseDetailArr)

                    }
                }
            }
        )
    }, [courseid])
    // console.log(courseDetailArr)

    return (
        <BrowserRouter>
        
        <div>
            <div className ='courseInfo-Banner'>
                <h2 className = 'courseName-Banner'>{courseDetailArr['course_name']}</h2>
            </div>
            <div className = 'course'>
                <Route path = '/course/:courseid/overview' exact>
                    <CourseInfo data = {courseDetailArr} />
                </Route>
                <Route path = '/course/:courseid/curriculum' exact>
                    <Section data = {courseid} />
                </Route>
                <Route path = '/course/:courseid/forum' exact>
                    <CourseInfo data = {courseDetailArr} />
                </Route>
                <Route path = '/course/:courseid/quiz' exact>
                    <CourseInfo data = {courseDetailArr} />
                </Route>
                
                <div className = 'rightSection'>
                    <CourseSidebar  />
                    <CourseDetail data = {courseDetailArr} />
                </div>
            </div>
        </div>
        
        </BrowserRouter>
        
    )
}

export default Course