import React from 'react';
import { Link } from "react-router-dom";
import axios from "axios";
import { useState, useEffect } from 'react';
import "../App.css";


function ViewEngineerDetails() {
    const endpoint = 'https://human-resource.hasura.app/v1/graphql';
    const [engineers, setEngineers] = useState([])
    useEffect(() => {axios.post(endpoint, { 
        query:  `query MyQuery {
            engineers {
                name
                type
                engineer_id
                email
            }
        }`
    }, {
        headers: {
            'x-hasura-admin-secret': 'R4q79TU2Z13Q22LVeawbwkhBynR4pbHUK8zZY5V4KhCw0Unse0zhh6h7hTtnpJHm',
            'content-type': 'application/json'
        }
    })
        .then(res => {
            console.log('hi');
            console.log(res.data.data);
            setEngineers(res.data.data.engineers);
        })
}, [])
    return (
        <div className="EngineerDetails">
            <h1>Engineer Details</h1>
            
            <div>
                <EngTable data={engineers} />
            </div>
            
            
            
        </div>
    );
}

const EngTable = ({data}) => {
    return (
        <table border='1'>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Senior / Junior</th>
                <th>Email</th>
            </tr>
            {data.map(el => (
                <tr>
                    <td>{el.engineer_id}</td>
                    <td>{el.name}</td>
                    <td>{el.type}</td>
                    <td>{el.email}</td>
                </tr>
            ))}
        </table>
    )
}
    

export default ViewEngineerDetails;