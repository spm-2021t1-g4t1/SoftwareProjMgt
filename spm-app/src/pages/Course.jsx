import React, { useState, useEffect } from 'react'
import { useParams } from "react-router-dom"
import { BrowserRouter, Route } from "react-router-dom"

import CourseInfo from './CourseInfo'
import CourseSidebar from '../component/CourseSidebar'
import CourseDetail from '../component/CourseDetail'
import Section from './Section'

const Course = () => {
    // pull courseId from url
    const courseid = useParams().courseid
    const classno = useParams().classno
    const staffusername = 'darrelwilde'
    //useState
    const [courseDetailArr, setCourseDetailArr] = useState({
        course_code: null,
        course_description: null,
        course_name: null,
        end_date: null,
        start_date: null,
        instructor: null,
        learning_objective: [],
        classes: [{
            trainer_name: null,
            start_date: null,
            end_date: null
        }]
    })
    // pull api only once
    useEffect(() => {
        fetch(`http://127.0.0.1:5000/course/${courseid}/${classno}`)
            .then(res => res.json())
            .then(
                (result) => {
                    // console.log(result.data)
                    setCourseDetailArr(result.data)
                    console.log(courseDetailArr)
                }
            )
    }, [courseid,classno])



    const [lessonDetailArr, setLessonDetailArr] = useState({
        course_code: null,
        course_description: null,
        course_name: null,
        end_date: null,
        start_date: null,
        instructor: null,
        learning_objective: [],
        classes: [{
            trainer_name: null,
            start_date: null,
            end_date: null
        }]
    })
    // pull api only once
    useEffect(() => {
        fetch(`http://127.0.0.1:5000/lesson/${courseid}/${classno}/${staffusername}`)
            .then(res => res.json())
            .then(
                (result) => {
                    // console.log(result.data)
                    setLessonDetailArr(result.data)
                    console.log(lessonDetailArr)
                }
            )
    }, [courseid,classno])
    
    return (
        <BrowserRouter>

            <div>
                <div className='courseInfo-Banner'>
                    <h2 className='courseName-Banner'>{courseDetailArr['course_name']}</h2>
                </div>
                <div className= 'd-flex justify-content-between row'>
                    <Route path='/course/:courseid/:classno/overview' exact>
                        <CourseInfo data={courseDetailArr} />
                    </Route>
                    <Route path='/course/:courseid/:classno/curriculum' exact>
                        <Section data={lessonDetailArr} />
                    </Route>
                    <Route path='/course/:courseid/:classno/forum' exact>
                        <CourseInfo data={courseDetailArr} />
                    </Route>
                    <Route path='/course/:courseid/:classno/quiz' exact>
                        <CourseInfo data={courseDetailArr} />
                    </Route>

                    <div className='col col-lg-auto'>
                        <CourseSidebar />
                        <CourseDetail data={courseDetailArr.classes[0]} />
                    </div>
                </div>
            </div>

        </BrowserRouter>

    )
}

export default Course
