import React from 'react';


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
        <div className="class-Section">
            <h2>Class {classSchema.class_no}</h2>
            <p className = 'class-text'>Slot: {classSchema.class_size}</p>
            <div className = 'class-timing'>
                <div className = 'class-text'>
                    <p>Start date: {classSchema.start_date}</p>
                    <p>End date: {classSchema.end_date}</p>
                </div>
                <div className = 'class-text'>
                    <p>Start Time: {classSchema.start_time}</p>
                    <p>End Time: {classSchema.end_time}</p>
                </div>
                {isCatalog 
                ? prop.inQueue.inQueue 
                    ? (<p className = 'redtext' >Awaiting Confirmation </p>)
                    : (<button  onClick = {enrolClass} className ='class-button blue-button'>Enroll</button>)
                : (<a href = {link}><button className ='class-button blue-button'>Enter Course</button></a>)}
                
            </div>
        </div>
    )
}


export default ClassCard