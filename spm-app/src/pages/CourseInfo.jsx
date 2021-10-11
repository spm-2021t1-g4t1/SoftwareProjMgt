import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faAward } from '@fortawesome/free-solid-svg-icons'


const CourseInfo = ( prop ) => {
    // console.log(prop)
    if (prop == null) {
        console.log("im null")
    }
    const courseDescription = prop.data.description 
    const learningObjective = prop.data.learning_objective

    return (
                <div className = 'leftSection'>
                    <div className = 'courseInfo-Section'>
                        <h2>About this course</h2>
                        {courseDescription}
                    </div>
                    <div className = 'courseInfo-Section'>
                        <h2>Training Objective</h2>
                        <ul>
                        {learningObjective.map((objective,index) => 
                            <li key ={index}><FontAwesomeIcon icon ={faAward} />  {objective}</li>
                        )}
                        </ul>
                    </div>
                </div>
        
    )
}

export default CourseInfo
