import React from 'react';
import { useState, useEffect } from 'react';
import { Button, Table, Tooltip, OverlayTrigger} from 'react-bootstrap';
import { TiTick, TiCancel} from "react-icons/ti";

import SearchBox from '../../component/SearchBox';

function ApprovalList() {
    const endpoint = 'http://127.0.0.1:5000/queue/getList';
    const [enrollmentRequest, setEnrollmentRequest] = useState([])
    const [searchTerm, setSearchTerm] = useState('')
    const [stateChange, setStateChange] = useState(0)
    
    useEffect(() => {fetch(endpoint).then(
        response => response.json()
        .then(data => {
            // console.log(data)
            const ERArr = data.data
            setEnrollmentRequest(ERArr)
            
        })
    ).catch()
    }, [stateChange])




    const enrollTooltip = (props) => (
        <Tooltip id="button-tooltip" {...props}>
          Enroll
        </Tooltip>
      );

      const rejectTooltip = (props) => (
        <Tooltip id="button-tooltip" {...props}>
          Reject
        </Tooltip>
      );


    return (
        <div>
            <h1>Engineer Details</h1>
            <SearchBox placeholder = 'Enter Name' handleChange = {(e) => setSearchTerm(e.target.value)}/>

            <Table hover responsive hover variant="light" className = 'admin-table' >
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Course ID</th>
                        <th>Course Name</th>
                        <th>Class No</th>
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
                        
                        function approveEnrollment() {
                            const endpoint1 = 'http://127.0.0.1:5000/enrolment/approve';
                            const data = {
                                staff_username: val.staff_username,
                                course_id: val.course_id,
                                class_no: val.class_no
                            }
                            console.log(data)
                            fetch(endpoint1,{
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json'
                                },
                                body: JSON.stringify(data)
                            })
                            .then((res) => res.json()) 
                            .then((result) => {
                            console.log(result)
                            setStateChange( stateChange + 1)
                            })
                        }

                        return (
                            // <div>{val.staff_name}</div>

                                <tr>
                                    <td>{val.staff_name}</td>
                                    <td>{val.course_id}</td>
                                    <td>{val.course_name}</td>
                                    <td>{val.class_no}</td>
                                    <td>
                                    <OverlayTrigger
                                        placement="left"
                                        delay={{ show: 100, hide: 400 }}
                                        overlay={enrollTooltip}
                                    >
                                        <Button onClick = {approveEnrollment} className ='mx-1' size="sm" variant = 'outline-success'>
                                            <TiTick />
                                        </Button>
                                    </OverlayTrigger>
                                    <OverlayTrigger
                                        placement="left"
                                        delay={{ show: 100, hide: 400 }}
                                        overlay={rejectTooltip}
                                    >
                                        <Button className ='mx-1'size="sm" variant = 'outline-danger'>
                                            <TiCancel />
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

export default ApprovalList
