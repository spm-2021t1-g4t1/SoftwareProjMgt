import React from 'react';
import { useState, useEffect } from 'react';
import { Button, Table } from 'react-bootstrap';
import { BiMessageRoundedDots} from "react-icons/bi";
import { FaEdit, FaTrash} from "react-icons/fa";

import SearchBox from '../../component/SearchBox';

function ViewUnassignedCourses() {
    const endpoint = 'http://127.0.0.1:5000/class/get_unassignedClass';
    const [courses, setCourses] = useState([])
    const [searchTerm, setSearchTerm] = useState('')
    useEffect(() => {fetch(endpoint).then(
        response => response.json()
        .then(data => {
            console.log(data.data)
            const courseArr = data.data
            setCourses(courseArr)
        })
    ).catch()
}, [])

return (
    <div className="EngineerDetails">
        <h1>Courses Without Trainers</h1>
        <SearchBox placeholder = 'Enter Course Name' handleChange = {(e) => setSearchTerm(e.target.value)}/>
        <Table hover responsive hover variant="light" className = 'admin-table' >
            <thead>
                <tr>
                    <th>Course Name</th>
                    <th>Course ID</th>
                    <th>Class No.</th>
                    <th>Class Size</th>
                    <th>Start Date</th>
                    <th>End Date</th>
                    <th>Start Time</th>
                    <th>End Time</th>
                    <th>Assign Trainer</th>
                </tr>
            </thead>

            <tbody>

                {courses.filter((val) => {
                    if (searchTerm === "") {
                        return val
                    } else if (val.course_name.toLowerCase().includes(searchTerm.toLowerCase())) {
                        return val
                    }
                    return null
                }).map((val) => {
                    return (
                        <tr>
                            <td>{val.course_name}</td>
                            <td>{val.course_id}</td>
                            <td>{val.class_no}</td>
                            <td>{val.class_size}</td>
                            <td>{val.start_date}</td>
                            <td>{val.end_date}</td>
                            <td>{val.start_time}</td>
                            <td>{val.end_time}</td>
                            <td>
                                <Button></Button>
                            </td>
                        </tr>
                    )
                })}

            </tbody>
        </Table>
    
    
    </div>
);
}

export default ViewUnassignedCourses;