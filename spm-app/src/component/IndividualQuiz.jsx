import { React, useEffect, useState } from 'react'
import { Button, Stack, Card } from 'react-bootstrap';
import { useLocation } from "react-router-dom"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faEdit, faArrowDown, faArrowUp, faTrash, faCopy } from '@fortawesome/free-solid-svg-icons';
import QuestionCard from './QuestionCard';

const IndividualQuiz = (props) => {
    // const [quizDetails, setQuizDetails] = useState(quiz);
    // const  {quiz} = useLocation()
    // console.log('saddasasdadsadsads',props)


    const [quizDetails, setQuizDetails] = useState([]);
    const [optionsDetails, setOptionDetails] = useState([])
    useEffect(()=>{
        console.log("hello am i receivign anyt",props.location.state)
    },[props])

    useEffect(()=>{
        fetch("http://127.0.0.1:5000/quiz_ques/" + props.location.state.quiz_id).then(response => response.json()
        .then(data => {
            // console.log(data.data)
            const quesArr = data.data
            setQuizDetails(quesArr)
            console.log(quizDetails)
        })).catch()
    },[])

    // useEffect(()=>{
    //     fetch("http://127.0.0.1:5000/ques_opt/" + props.location.state.quiz_id).then(response => response.json()
    //     .then(data => {
    //         // console.log(data.data)
    //     })).catch()
    // },[])

    return (
        <div>
            <h1>{props.location.state.uploader} 's</h1>
            <h1>{props.location.state.quiz_name}</h1>
            <br></br>
            <hr></hr>
            <br></br>

            <Stack gap={2}>
            
            {quizDetails.map(quiz => {
            return(
                    <QuestionCard key={quiz.ques_id} quizCard={quiz}/> 
                )
            })}
           
            </Stack>
            <br></br>
        </div>
    )
}

export default IndividualQuiz