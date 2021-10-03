import React from 'react';

import ClassCard from './ClassCard';

const CourseCard = ({courseSchema}) => {

    // console.log(courseSchema)

    return(
        <div> 
            <div className="Catalog-Section">    
                <h2>{courseSchema.course_id} - {courseSchema.course_name}</h2>
                <p>Description: {courseSchema.description}</p>
            </div>
            {courseSchema.classes.map(classes => <ClassCard classSchema={classes} key={courseSchema.course_code - classes.class_no}/>)}
        </div>
        
    )
}


export default CourseCard