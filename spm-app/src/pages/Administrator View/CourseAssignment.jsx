import React from 'react';
import { useState, useEffect } from 'react';
import { Button, Table, Tooltip, OverlayTrigger, Modal} from 'react-bootstrap';
import { BrowserRouter, Route ,Link } from "react-router-dom"
import { FaTrash} from "react-icons/fa";
import { MdAssignment} from "react-icons/md";

import SearchBox from '../../component/SearchBox';
import AssignEngineerForm from './AssignEngineerForm';

function CourseAssignment() {
        // Minor bug for now, assigning trainer > click on unassigned course at the side bar. 

    const endpoint = 'http://127.0.0.1:5000/class/get_unassignedClass';
    const [enrollmentRequest, setEnrollmentRequest] = useState([])
    const [searchTerm, setSearchTerm] = useState('')
    const [stateChange, setStateChange] = useState(0)
    const [classesByCourse, setClassesByCourse] = useState([])
    const options = { year: 'numeric', month: 'short', day: 'numeric' };


    const groupBy = key => array =>
        array.reduce((objectsByKeyValue, obj) => {
            const value = obj[key];
            objectsByKeyValue[value] = (objectsByKeyValue[value] || []).concat(obj);
            return objectsByKeyValue;
        }, {});
    
    const groupByCourseid = groupBy('course_id')
    
    function classChange() {
        setStateChange(stateChange+1)
    }


    useEffect(() => {fetch(endpoint).then(
        response => response.json()
        .then(data => {
            // console.log(data)
            const ERArr = data.data
            setEnrollmentRequest(ERArr)

            // group classes by course_id
            const classesArr = []
            const groupedclasses = groupByCourseid(ERArr)

            // foreach object in groupedClasses, push to classesArr
            Object.keys(groupedclasses).map(function(key) {
                classesArr.push(groupedclasses[key])
            })
            // console.log(classesArr)
            setClassesByCourse(classesArr)
            
        })
    ).catch()
    }, [stateChange])


    const assignTooltip = (props) => (
        <Tooltip id="button-tooltip" {...props}>
          Assign
        </Tooltip>
    );

    

    return (
        <BrowserRouter>
        <Route path='/Administrator/Course/unassigned' exact>
            <div>
                <h1>Courses Without Trainers</h1>
                <SearchBox placeholder = 'Enter Name' handleChange = {(e) => setSearchTerm(e.target.value)}/>

                <Table hover responsive hover variant="light" className = 'admin-table' >
                    <thead>
                        <tr>
                            <th className = 'text-center'>Class No.</th>
                            <th className = 'text-center'>Start Date</th>
                            <th className = 'text-center'>End Date</th>
                            <th className = 'text-center'>Start Time</th>
                            <th className = 'text-center'>End Time</th>
                            <th className = 'text-center'>Class Size</th>
                            <th className = 'text-center'>Actions</th>
                        </tr>
                    </thead>

                    <tbody>

                        
                        
                        {classesByCourse.filter((val) => {
                                console.log(val[0]['course_name'])
                                if (searchTerm === "") {

                                    console.log(val)
                                    return val
                                } else if (val[0]['course_name'].toLowerCase().includes(searchTerm.toLowerCase())) {
                                    console.log(val)

                                    return val
                                }
                                return null
                            }).map((val) => {
                                return (
                                    <React.Fragment>
                                    <tr className = 'table-secondary'>
                                        <td className = 'text-center' colSpan="7"><h4>{val[0]['course_name']}</h4></td>
                                    </tr>
                                    {val.map(classinfo => {

                                    return(
                                        <tr>
                                            <td className = 'text-center'>{classinfo['class_no']}</td>
                                            <td className = 'text-center'>
                                                {(new Date(classinfo['start_date'])).toLocaleDateString("en-US", options)}
                                            </td>
                                            <td className = 'text-center'>
                                                {(new Date(classinfo['end_date'])).toLocaleDateString("en-US", options)}
                                            </td>
                                            <td className = 'text-center mx-2'>
                                                {classinfo['start_time']}
                                            </td>
                                            <td className = 'text-center mx-2'>
                                                {classinfo['end_time']}
                                            </td>
                                            <td className = 'text-center'>
                                                {classinfo['class_size']}
                                            </td>
                                        <td className = 'align-middle' >
                                        <OverlayTrigger
                                            placement="left"
                                            delay={{ show: 100, hide: 400 }}
                                            overlay={assignTooltip}
                                        >
                                            <Link to={`/Administrator/${classinfo['course_id']}/${classinfo['class_no']}/assign`}><Button className ='mx-1' size="sm" variant = 'outline-primary'>
                                                <MdAssignment />
                                            </Button></Link>
                                        </OverlayTrigger>
                                        </td>
                                    </tr>
                                    )
                            })}
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
        
        
        </BrowserRouter>                 
        
    );
}

export default CourseAssignment