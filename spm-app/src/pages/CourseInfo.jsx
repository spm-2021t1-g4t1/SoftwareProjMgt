import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faAward } from '@fortawesome/free-solid-svg-icons'
import { Container } from 'react-bootstrap'

const CourseInfo = ( prop ) => {
    // console.log(prop)
    if (prop == null) {
        console.log("im null")
    }
    const courseDescription = prop.data.description 
    const learningObjective = prop.data.learning_objective

    return (
                <div className = 'col col-lg-9 col-md-8'>
                    <Container className = 'border border-info container-bg my-3'>
                        <h2>About this course</h2>
                        {courseDescription}
                    </Container>
                    <Container className = 'border border-info container-bg my-3'>
                        <h2>Training Objective</h2>
                        <ul className = 'list-group my-3'>
                        {learningObjective.map((objective,index) => 
                            <li className = 'list-group-item' key ={index}><FontAwesomeIcon icon ={faAward} />  {objective}</li>
                        )}
                        </ul>
                    </Container>
                </div>
        
    )
}

export default CourseInfo
