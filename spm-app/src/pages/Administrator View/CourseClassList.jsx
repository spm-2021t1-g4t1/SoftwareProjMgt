import React from 'react';
import { useState, useEffect } from 'react';
import { BrowserRouter, Route } from "react-router-dom";
import { useParams } from "react-router-dom";
import { Button, Table } from 'react-bootstrap';
import { BiMessageRoundedDots} from "react-icons/bi";
import { FaEdit, FaTrash} from "react-icons/fa";

import SearchBox from '../../component/SearchBox';

function ViewClassList(prop) {

    console.log(prop)
    const courseid = prop.courseid
    const classno = prop.classno

    const [classList, setClassList] = useState([])
    const [searchTerm, setSearchTerm] = useState('')


    // pull api 
    useEffect(() => {
        
        fetch(`http://127.0.0.1:5000/enrolment/${courseid}/${classno}`)
        .then(res => res.json())
        .then(
            (result) => {

                setClassList(result.data)

            }
            
        ).catch()
    }, [])
    
    useEffect(() => {
        console.log(classList)
    },[classList])

    return (
        <div>
            <h1>Class List</h1>
            <SearchBox placeholder = 'Enter Name' handleChange = {(e) => setSearchTerm(e.target.value)}/>

            <Table hover responsive hover variant="light" className = 'admin-table' >
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Role</th>
                        <th>Department</th>
                        <th>Current Designation</th>
                        <th></th>
                    </tr>
                </thead>

                <tbody>

                    {classList.filter((val) => {
                        if (searchTerm === "") {
                            return val
                        } else if (val.staff_name.toLowerCase().includes(searchTerm.toLowerCase())) {
                            return val
                        }
                        return null
                    }).map((val) => {
                        console.log(val)
                        return (
                        
                                <tr>
                                    <td>{val.staff_name}</td>
                                    <td>{val.role}</td>
                                    <td>{val.department}</td>
                                    <td>{val.current_designation}</td>
                                    
                                </tr>

                            
                        )
                    })}
                </tbody>
            </Table>
        </div>
    )
}

export default ViewClassList;