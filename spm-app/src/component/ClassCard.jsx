import React from 'react';
import { Button } from 'react-bootstrap';

const ClassCard = (prop) => {
    console.log(prop.inQueue.inQueue)

    const classSchema = prop.classSchema
    const link = `course/${classSchema.course_id}/${classSchema.class_no}/overview`
    const isCatalog = window.location.pathname.includes('catalog')


    const endpoint = `http://127.0.0.1:5000/queue/darrelwilde/${classSchema.course_id}`
    const data = {class_no: classSchema.class_no}
    
    function enrolClass() {
        fetch(endpoint,{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then((res) => res.json()) 
        .then((result) => {
        // console.log(result)
        prop.classChange()

        })
    }


    return(
        <div className="border border-info container-fluid container-bg">
            <div className = 'd-flex justify-content-between'>
                <h2>Class {classSchema.class_no}</h2>
                <p className = 'class-text'>Slot: {classSchema.class_size}</p>
            </div>
            
            <div className = 'd-flex justify-content-around'>
                <div className = 'container-fluid'>
                    <p className = 'm-1'>Start date: {classSchema.start_date}</p>
                    <p className = 'm-1'>End date: {classSchema.end_date}</p>
                </div>  

                <div className = 'container-fluid'>
                    <p className = 'm-1'>Start Time: {classSchema.start_time}</p>
                    <p className = 'm-1'>End Time: {classSchema.end_time}</p>
                </div>

                {isCatalog 
                ? prop.inQueue.inQueue 
                    ? (<p className = 'redtext' >Awaiting Confirmation </p>)
                    : (<Button variant="primary"  onClick = {enrolClass}>Enroll</Button>)
                : (<a href = {link}> <Button variant="primary">Enter Course</Button></a>)}
                
            </div>
        </div>
    )
}


export default ClassCard