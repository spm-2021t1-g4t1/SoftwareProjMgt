import React from 'react'
import { Button, Dropdown } from 'react-bootstrap';
import { Link } from "react-router-dom";

const Quizzes = ({ quizzes }) => {

    function goToQuizDetails(qid){
        fetch("http://127.0.0.1:5000/quiz/"+qid).then(
            response => response.json()
            .then(data => {
                console.log(data.data[0])
            })
        ).catch(error => console.log(error))
    }
    return (
        <Dropdown>
            <Dropdown.Toggle variant="success" id="dropdown-basic">
                Uploaded Quizzes
            </Dropdown.Toggle>

            <Dropdown.Menu>
            {quizzes.map(quiz => {
            return(
                <Dropdown.Item key={quiz.quiz_name}>
                    <Link to={{
                                pathname: "/Engineer/IndividualQuiz",
                                state: quiz 
                            }}>
                    <Button variant="outline-secondary" size='lg'  onClick={() => goToQuizDetails(quiz.quiz_id)}>{quiz.quiz_name}</Button>{' '}
                    </Link>
                </Dropdown.Item>
                )
            })}
            </Dropdown.Menu>
            </Dropdown>
            
    )
}

export default Quizzes