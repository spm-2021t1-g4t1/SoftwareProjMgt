import React, { useState, useEffect } from 'react'
import { useParams } from "react-router-dom"
import { Accordion, Container} from 'react-bootstrap';

function TrainerClassResult() {
    const courseid = useParams().courseid
    const classno = useParams().classno
    const endpoint = `http://127.0.0.1:5000/class_result/${courseid}/${classno}`
    const[staffResults, setStaffResults] = useState([]);
    
    useEffect(() => {
        fetch(endpoint)
            .then(res => res.json())
            .then(
                (result) => {
                    console.log(result.data)
                    setStaffResults(result.data)
                }
            )
    }, [])


    return (
        <div className = 'col col-lg-9 col-md-8'>
            
            
            <div className = 'bg-white border border border-2 rounded'>
                <h3 className ="text-center">ClassList</h3>

            {staffResults.length
            ?<Accordion defaultActiveKey= "0">
                {staffResults.map((staffResult, index) => 
                <Accordion.Item eventKey={index}>
                <Accordion.Header>{staffResult.staff_name}</Accordion.Header>
                <Accordion.Body>
                {staffResult.lesson_quiz_results.map((quiz_result,index) =>
                    <Container className='d-flex justify-content-between border-bottom border-top py-2'>
                        <h3 className ="my-2">Lesson {quiz_result.lesson_no}</h3>
                        {quiz_result.quiz_score
                        ?<span>Score: {quiz_result.quiz_score}/100</span>
                        :<span className = 'text-danger'>Not Attempted</span>
                        }
                    </Container>
                
                )}
                    <Container className='d-flex justify-content-between border-bottom  py-2'>
                        <h3 className ="my-2">Final Exam</h3>
                        {staffResult.final_quiz_result
                        ?<span>Score: {staffResult.final_quiz_result}/100</span>
                        :<span className = 'text-danger'>Not Attempted</span>
                        }
                    </Container>
                    </Accordion.Body>
                </Accordion.Item>
                )}
            </Accordion>
            :<div className = 'border-top border border-2'>
                <h5 className = 'text-danger text-center my-2'>No Engineer Enrolled</h5>
            </div>
            
            
            }    
            
            </div>
            
        

        </div>
    )
}

export default TrainerClassResult
