import React from 'react';
import { useState, useEffect } from 'react';
import { Button, Table, Tooltip, OverlayTrigger} from 'react-bootstrap';
import { FaTrash} from "react-icons/fa";
import { MdAssignment} from "react-icons/md";

import SearchBox from '../../component/SearchBox';

function CourseAssignment() {
    const endpoint = 'http://127.0.0.1:5000/class/get_unassignedClass';
    const [enrollmentRequest, setEnrollmentRequest] = useState([])
    const [searchTerm, setSearchTerm] = useState('')
    const [stateChange, setStateChange] = useState(0)
    
    useEffect(() => {fetch(endpoint).then(
        response => response.json()
        .then(data => {
            console.log(data)
            const ERArr = data.data
            setEnrollmentRequest(ERArr)
            
        })
    ).catch()
    }, [stateChange])

    const assignTooltip = (props) => (
        <Tooltip id="button-tooltip" {...props}>
          Assign
        </Tooltip>
    );

    const removeTooltip = (props) => (
        <Tooltip id="button-tooltip" {...props}>
          Remove
        </Tooltip>
    );


    return (
        <div>
            <h1>Unassigned Course</h1>
            <SearchBox placeholder = 'Enter Name' handleChange = {(e) => setSearchTerm(e.target.value)}/>

            <Table hover responsive hover variant="light" className = 'admin-table' >
                <thead>
                    <tr>
                        <th>Course Name</th>
                        <th>Class No</th>
                        <th className = 'text-center' >Dates</th>
                        <th className = 'text-center'>Timing</th>
                        <th></th>
                    </tr>
                </thead>

                <tbody>

                    {enrollmentRequest.filter((val) => {
                        if (searchTerm === "") {
                            return val
                        } else if (val.course_name.toLowerCase().includes(searchTerm.toLowerCase())) {
                            return val
                        }
                        return null
                    }).map((val) => {
                        
                        const start_time = val.start_time.substring(0, (val.start_time.length - 3))
                        const end_time = val.end_time.substring(0, (val.end_time.length - 3))

                        return (
                            // <div>{val.staff_name}</div>

                                <tr>
                                    <td className = 'align-middle' >{val.course_name}</td>
                                    <td className = 'align-middle text-center' >{val.class_no}</td>
                                    <td className = 'text-center'>
                                        {val.start_date} <br /> - <br /> {val.end_date}
                                    </td>
                                    <td className = 'text-center mx-2'>
                                        {start_time} <br /> - <br /> {end_time}
                                    </td>
                                    <td className = 'align-middle' >
                                    <OverlayTrigger
                                        placement="left"
                                        delay={{ show: 100, hide: 400 }}
                                        overlay={assignTooltip}
                                    >
                                        <Button className ='mx-1' size="sm" variant = 'outline-primary'>
                                            <MdAssignment />
                                        </Button>
                                    </OverlayTrigger>
                                    <OverlayTrigger
                                        placement="left"
                                        delay={{ show: 100, hide: 400 }}
                                        overlay={removeTooltip}
                                    >
                                        <Button className ='mx-1'size="sm" variant = 'outline-danger'>
                                            <FaTrash />
                                        </Button>
                                    </OverlayTrigger>
                                    </td>
                                </tr>
                        )
                    })}
                </tbody>
            </Table>
        </div>
    );
}

export default CourseAssignment
