import React from 'react';
import { useState, useEffect } from 'react';
import { Button, Table, Tooltip, OverlayTrigger, Modal} from 'react-bootstrap';
import { BrowserRouter, Route ,Link } from "react-router-dom"
import { FaClipboardList} from "react-icons/fa";
import { MdPersonRemoveAlt1, MdAssignment, MdPersonSearch } from "react-icons/md";

import SearchBox from '../../component/SearchBox';
import AssignEngineerForm from './AssignEngineerForm';
import CourseClassList from './CourseClassList'
import AssignEnrol from './AssignEnrol';

function AvaliableCourse() {
    // Minor bug for now, assigning trainer > click on unassigned course at the side bar. 
    // lmao why is there a second BrowserRouter here this is really weird

    const endpoint = 'http://127.0.0.1:5000/course/getList';
    const [courseList, setCourseList] = useState([])
    const [searchTerm, setSearchTerm] = useState('')
    const [stateChange, setStateChange] = useState(0)
    const options = { year: 'numeric', month: 'short', day: 'numeric' };

    function classChange() {
        setStateChange(stateChange+1)
    }


    useEffect(() => {fetch(endpoint).then(
        response => response.json()
        .then(data => {
            console.log(data)
            const ERArr = data.data
            setCourseList(ERArr)
            
        })
    ).catch()
    }, [stateChange])


    function removeTrainer(courseid,classno) {
        const endpoint = `http://127.0.0.1:5000/class/trainer/modify`
        const data = {
            course_id : courseid,
            class_no : classno,
            staff_username: null
        }
        console.log(data)
        fetch(endpoint,{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then((res) => res.json()) 
        .then((result) => {
            setStateChange(stateChange+1)
        })
    }

    const classListTooltip = (props) => (
        <Tooltip id="button-tooltip" {...props}>
          ClassList
        </Tooltip>
    );
    const assignTooltip = (props) => (
        <Tooltip id="button-tooltip" {...props}>
          Assign Trainer
        </Tooltip>
    );
    const removeTooltip = (props) => (
        <Tooltip id="button-tooltip" {...props}>
          Remove Trainer
        </Tooltip>
    );

    const enrolTooltip = (props) => (
        <Tooltip id="button-tooltip" {...props}>
            Assign Learners
        </Tooltip>
    );

    return (
        <BrowserRouter>
        <Route path='/Administrator/Course/list' exact>
            <div>
                <h1>List of avaliable courses</h1>
                <SearchBox placeholder = 'Enter Name' handleChange = {(e) => setSearchTerm(e.target.value)}/>

                <Table hover responsive hover variant="light" className = 'admin-table' >
                    <thead>
                        <tr>
                            <th>Class No.</th>
                            <th className = 'text-center'>Start Date</th>
                            <th className = 'text-center'>End Date</th>
                            <th className = 'text-center'>Start Time</th>
                            <th className = 'text-center'>End Time</th>
                            <th className = 'text-center'>Trainer</th>
                            <th className = 'text-center'>Class Size</th>
                            <th className = 'text-center'>Actions</th>
                        </tr>
                    </thead>

                    <tbody>

                        {courseList.filter((val) => {
                            if (searchTerm === "") {
                                return val
                            } else if (val.course_name.toLowerCase().includes(searchTerm.toLowerCase())) {
                                return val
                            }
                            return null
                        }).map((val) => {
                            console.log(val)
                            // const start_time = val.start_time.substring(0, (val.start_time.length - 3))
                            // const end_time = val.end_time.substring(0, (val.end_time.length - 3))
                            const classList = val.classes
                            // console.log(classList)
                            return (
                                <React.Fragment>
                                    <tr className = 'table-secondary'>
                                        <td className = 'text-center' colSpan="8"><h4>{val.course_name}</h4></td>
                                    </tr>
                                    {classList.map((classesObj) => {
                                       return (
                                            <tr className = "align-middle" >
                                                <td className = 'text-center'>{classesObj.class_no}</td>
                                                <td className = 'text-center'>
                                                    {(new Date(classesObj.start_date)).toLocaleDateString("en-US", options)}
                                                </td>
                                                <td className = 'text-center'>
                                                    {(new Date(classesObj.end_date)).toLocaleDateString("en-US", options)}
                                                </td>
                                                <td className = 'text-center mx-2'>
                                                    {classesObj.start_time}
                                                </td>
                                                <td className = 'text-center mx-2'>
                                                    {classesObj.end_time}
                                                </td>
                                                <td>
                                                    {classesObj.trainer_name
                                                    ?classesObj.trainer_name
                                                    :"Not Assigned"}
                                                </td>
                                                <td className = 'text-center'>
                                                    {classesObj.class_size}
                                                </td>
                                                <td>
                                                <OverlayTrigger
                                                        placement="left"
                                                        delay={{ show: 100, hide: 400 }}
                                                        overlay={classListTooltip}
                                                    >
                                                        <Link to={`/Administrator/${classesObj.course_id}/${classesObj.class_no}/classlist`}><Button className ='mx-1' size="sm" variant = 'outline-dark'>
                                                            <FaClipboardList />
                                                        </Button></Link>
                                                </OverlayTrigger>
                                                {classesObj.trainer_name
                                                    ?<OverlayTrigger
                                                    placement="left"
                                                    delay={{ show: 100, hide: 400 }}
                                                    overlay={removeTooltip}
                                                    >
                                                        <Button onClick = {() => removeTrainer(classesObj.course_id,classesObj.class_no)}className ='mx-1' size="sm" variant = 'outline-danger'>
                                                            <MdPersonRemoveAlt1 />
                                                        </Button>
                                                    </OverlayTrigger>
                                                    :<OverlayTrigger
                                                    placement="left"
                                                    delay={{ show: 100, hide: 400 }}
                                                    overlay={assignTooltip}
                                                    >
                                                        <Link to={`/Administrator/${classesObj.course_id}/${classesObj.class_no}/assign`}><Button className ='mx-1' size="sm" variant = 'outline-primary'>
                                                            <MdAssignment />
                                                        </Button></Link>
                                                    </OverlayTrigger>}
                                                    <OverlayTrigger
                                                        placement="left"
                                                        delay={{ show: 100, hide: 400 }}
                                                        overlay={enrolTooltip}
                                                    >
                                                        <Link to={`/Administrator/${classesObj.course_id}/${classesObj.class_no}/assignEnrol`}><Button className ='mx-1' size="sm" variant = 'outline-primary'>
                                                            <MdPersonSearch />
                                                        </Button></Link>
                                                </OverlayTrigger>
                                                </td>
                                            </tr>   
                                       )} 

                                    )}
                                </React.Fragment>  
                            )
                        })}
                    </tbody>
                </Table>
            </div>
        </Route>
        <Route path='/Administrator/:courseid/:classno/assign' exact>
            <AssignEngineerForm statechange = {classChange}/>
        </Route>
        <Route path='/Administrator/:courseid/:classno/classlist' exact>
            <CourseClassList />
        </Route>
        <Route path = '/Administrator/:courseid/:classno/assignEnrol/' exact>
            <AssignEnrol />
        </Route>
        
        </BrowserRouter>                 
        
    );
}

export default AvaliableCourse
