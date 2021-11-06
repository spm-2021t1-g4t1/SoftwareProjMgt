import React, { useState, useEffect } from 'react'
import { Route, useParams, useHistory } from "react-router-dom"
import { Button } from 'react-bootstrap';
import {  MdArrowBack} from "react-icons/md";

import CourseInfo from './CourseInfo'
import CourseSidebar from '../../component/CourseSidebar'
import CourseDetail from '../../component/CourseDetail'
import Section from './Section'
import TrainerClassResult from './TrainerClassResult'


function TrainerCourse() {
    const history = useHistory()
    const courseid = useParams().courseid
    const classno = useParams().classno

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
                    console.log(result.data)
                    setCourseDetailArr(result.data)
                    // console.log(courseDetailArr)
                }
            )
    }, [courseid,classno])

    
    return (

            <div>
                <Button onClick = {() => history.replace('/Engineer/trainer')} variant ="outline-primary" >
                    <MdArrowBack />
                </Button>
                <div className='container-fluid my-3'>
                    <h1 className='courseName-Banner'>{courseDetailArr['course_name']}</h1>
                </div>
                <div className= 'd-flex justify-content-between row'>
                    <Route path='/Engineer/teaching/:courseid/:classno/overview' exact>
                        <CourseInfo data={courseDetailArr} />
                    </Route>
                    <Route path='/Engineer/teaching/:courseid/:classno/curriculum' exact>
                        <Section/>
                    </Route>
                    <Route path='/Engineer/teaching/:courseid/:classno/forum' exact>
                        <CourseInfo data={courseDetailArr} />
                    </Route>
                    <Route path='/Engineer/teaching/:courseid/:classno/quiz' exact>
                        <CourseInfo data={courseDetailArr} />
                    </Route>
                    <Route path='/Engineer/teaching/:courseid/:classno/result' exact>
                        <TrainerClassResult />
                    </Route>

                    <div className='col col-lg-auto'>
                        <CourseSidebar />
                        <CourseDetail data={courseDetailArr.classes[0]} />
                    </div>
                </div>
            </div>


    )
}

export default TrainerCourse
