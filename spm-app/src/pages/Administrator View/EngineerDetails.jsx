import React from 'react';
import { useState, useEffect } from 'react';
import { Button, Table } from 'react-bootstrap';
import { BiMessageRoundedDots} from "react-icons/bi";
import { FaEdit, FaTrash} from "react-icons/fa";

import SearchBox from '../../component/SearchBox';


function ViewEngineerDetails() {
    const endpoint = 'http://127.0.0.1:5000/staff/engineers';
    const [engineers, setEngineers] = useState([])
    const [searchTerm, setSearchTerm] = useState('')
    useEffect(() => {fetch(endpoint).then(
        response => response.json()
        .then(data => {
            // console.log(data.data)
            const engArr = data.data
            setEngineers(engArr)
            
        })
    ).catch()
    }, [])

    return (
        <div className="EngineerDetails">
            <h1>Engineer Details</h1>
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

                    {engineers.filter((val) => {
                        if (searchTerm === "") {
                            return val
                        } else if (val.staff_name.toLowerCase().includes(searchTerm.toLowerCase())) {
                            return val
                        }
                        return null
                    }).map((val) => {
                        return (
                            // <div>{val.staff_name}</div>

                                <tr>
                                    <td>{val.staff_name}</td>
                                    <td>{val.role}</td>
                                    <td>{val.department}</td>
                                    <td>{val.current_designation}</td>
                                    <td>
                                        <Button className ='mx-1'size="sm" variant = 'outline-dark'>
                                            <FaEdit />
                                        </Button>
                                        <Button className ='mx-1' size="sm" variant = 'outline-primary'>
                                            <BiMessageRoundedDots />
                                        </Button>
                                        <Button className ='mx-1'size="sm" variant = 'outline-danger'>
                                            <FaTrash />
                                        </Button>
                                        
                                    </td>
                                </tr>

                            
                        )
                    })}
                </tbody>
            </Table>
        </div>
    );
}


export default ViewEngineerDetails;