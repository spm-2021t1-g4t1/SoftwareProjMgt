import React from 'react';


const ClassCard = ({classSchema}) => {
    console.log(classSchema)

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
            </div>
        </div>
    )
}


export default ClassCard