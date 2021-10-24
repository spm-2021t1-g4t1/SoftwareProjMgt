import React from 'react';
import { useState, useEffect } from 'react';
import "../App.css";
import SearchBox from './SearchBox';


function ViewEngineerDetails() {
    const endpoint = 'http://127.0.0.1:5000/staff';
    const [engineers, setEngineers] = useState([])
    const [searchTerm, setSearchTerm] = useState('')
    useEffect(() => {fetch(endpoint).then(
        response => response.json()
        .then(data => {
            // console.log(data.data)
            const engArr = data.data
            setEngineers(engArr)
            console.log('ji')
            console.log(engineers)
            
        })
    ).catch()
    }, [])

    return (
        <div className="EngineerDetails">
            <h1>Engineer Details</h1>
            <SearchBox placeholder = 'Enter Name' handleChange = {(e) => setSearchTerm(e.target.value)}/>

            <table border='1' >

                    <tr>
                        <th>Name</th>
                        <th>Username</th>
                        <th>Role</th>
                        <th>Department</th>
                        <th>Current Designation</th>
                    </tr>


                
            
            
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
                            <td>{val.staff_username}</td>
                            <td>{val.role}</td>
                            <td>{val.department}</td>
                            <td>{val.current_designation}</td>
                        </tr>

                    
                )
            })}

            </table>
            
            
            
        </div>
    );
}


export default ViewEngineerDetails;