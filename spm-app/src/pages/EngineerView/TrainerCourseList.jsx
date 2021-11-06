import React from 'react';
import { useState, useEffect } from 'react';
import { Button, Table, Tooltip, OverlayTrigger, Modal} from 'react-bootstrap';
import { BrowserRouter, Route ,Link } from "react-router-dom"
import { FaClipboardList} from "react-icons/fa";


import SearchBox from '../../component/SearchBox';
import CourseClassList from '../Administrator View/CourseClassList'
import TrainerCourse from './TrainerCourse.jsx';


function TrainerCourseList() {
    const user = JSON.parse(localStorage.getItem('user')).staff_username
    console.log(user)
    const endpoint = `http://127.0.0.1:5000/class/${user}/get_assignedClass`;
    const [courseList, setCourseList] = useState([])
    const [searchTerm, setSearchTerm] = useState('')
    const [stateChange, setStateChange] = useState(0)
    function classChange() {
        setStateChange(stateChange+1)
    }


    useEffect(() => {fetch(endpoint).then(
        response => response.json()
        .then(data => {
            console.log(data.data)
            const ERArr = data.data
            setCourseList(ERArr)
            
        })
    ).catch()
    }, [stateChange])
    
    const classListTooltip = (props) => (
        <Tooltip id="button-tooltip" {...props}>
          ClassList
        </Tooltip>
    );

    return (
        <BrowserRouter>
            <Route path='/Engineer/trainer' exact>
            <div>
                <h1>Teaching Course</h1>
                <SearchBox placeholder = 'Enter Name' handleChange = {(e) => setSearchTerm(e.target.value)}/>
                <Table hover responsive hover variant="light" className = 'admin-table' >
                        <thead>
                            <tr>
                                <th className = 'text-center'>Class No</th>
                                <th className = 'text-center' >Dates</th>
                                <th className = 'text-center'>Timing</th>
                                <th className = 'text-center'>Total Capacity</th>
                                <th></th>
                            </tr>
                        </thead>

                        <tbody>
                        {courseList.filter((val) => {
                            if (searchTerm === "") {
                                return val
                            } else if (Object.keys(val)[0].toLowerCase().includes(searchTerm.toLowerCase())) {
                                return val
                            }
                            return null
                        }).map((val) => {
                            const classList = Object.values(val)[0]
                            
                            return (
                                <React.Fragment>
                                    <tr className = 'table-secondary'>
                                        <td className = 'text-center' colSpan="5"><h4>{Object.keys(val)}</h4></td>
                                    </tr>
                                    {classList.map((classesObj) => {
                                        return (
                                            <tr className = "align-middle" >
                                                <td className = 'text-center'>{classesObj.class_no}</td>
                                                <td className = 'text-center'>
                                                    {classesObj.start_date} <br /> - <br /> {classesObj.end_date}
                                                </td>
                                                <td className = 'text-center'>
                                                    {classesObj.start_time} <br /> - <br /> {classesObj.end_time}
                                                </td>
                                                <td className = 'text-center'>
                                                    {classesObj.class_size}
                                                </td>
                                                <td>
                                                <Link to={`/Engineer/teaching/${classesObj.course_id}/${classesObj.class_no}/overview`}>
                                                    <Button className ='mx-1' size="sm" >Enter Course</Button>
                                                </Link>
                                                <OverlayTrigger
                                                            placement="left"
                                                            delay={{ show: 100, hide: 400 }}
                                                            overlay={classListTooltip}
                                                        >
                                                <Link to={`/Engineer/${classesObj.course_id}/${classesObj.class_no}/classlist`}><Button className ='mx-1' size="sm" variant = 'outline-dark'>
                                                    <FaClipboardList />
                                                </Button></Link>
                                                </OverlayTrigger>
                                                </td>
                                            </tr>   
                                        )} 

                                    )}
                                </React.Fragment>  
                            )
                        })
                        }
                            
                        </tbody>
                </Table>
                
            </div>
            </Route>
            <Route path='/Engineer/:courseid/:classno/classlist' component = {CourseClassList} exact />
            <Route path = '/Engineer/teaching/:courseid/:classno/' component = {TrainerCourse} />

        </BrowserRouter>          
    )
}

export default TrainerCourseList
