import React from 'react';
import { useState, useEffect } from 'react';
import { Button} from 'react-bootstrap';
import { useParams, useHistory } from "react-router-dom";
import { Table } from 'react-bootstrap';
import { MdArrowBack} from "react-icons/md";

import SearchBox from '../../component/SearchBox';

function ViewClassList() {
    const history = useHistory()
    const courseid = useParams().courseid
    const classno = useParams().classno

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
            <Button onClick = {() => history.goBack()} variant ="outline-primary" >
                    <MdArrowBack />
            </Button>
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

                    {classList.length
                    ?classList.filter((val) => {
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
                                    <td></td>
                                </tr>
                        )
                    })
                    :   <tr className = 'table-secondary'>
                            <td colSpan = "5" className = 'text-center' colSpan="5"><h3>No Engineer Enrolled</h3></td>
                        </tr>
                }
                </tbody>
            </Table>
        </div>
    )
}

export default ViewClassList;