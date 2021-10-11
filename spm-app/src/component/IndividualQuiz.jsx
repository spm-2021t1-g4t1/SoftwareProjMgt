import { React, useEffect, useState } from 'react'
import { Button, Stack, Card, Form, Col, Row} from 'react-bootstrap';
import { useLocation, Link } from "react-router-dom"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faPlus, faArrowDown, faArrowUp, faTrash, faCopy } from '@fortawesome/free-solid-svg-icons';
import QuestionCard from './QuestionCard';

const IndividualQuiz = (props) => {
    // const [quizDetails, setQuizDetails] = useState(quiz);
    // const  {quiz} = useLocation()
    // console.log('saddasasdadsadsads',props)
    const [quizDetails, setQuizDetails] = useState([]);

    const [quizName, setQuizName] = useState(props.location.state.quiz_name)

    useEffect(()=>{
        console.log("This is my quiz id",props.location.state.quiz_id)
        let retlist = quizDetails
      
        console.log(props)
    },[props])


    useEffect(() => {
        console.log(quizDetails)
    }, [quizDetails])

    const AddMCQ = () => {
        let no = quizDetails.length + 1
        console.log(no, props.location.state.quiz_id)
        setQuizDetails([...quizDetails, {
            qid: props.location.state.quiz_id,
            ques_id: no,
            question: "",
            question_type: "mcq"
        }])
        const data = {
            qid: props.location.state.quiz_id,
            ques_id: no,
            question: "",
            question_type: "mcq"
        }
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
            };
        fetch(`http://127.0.0.1:5000/add_ques/${props.location.state.quiz_id}`, requestOptions)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(err => console.log(err))
    }

    const AddTF = () => {
        let no = quizDetails.length + 1
        console.log(no, props.location.state.quiz_id)
        setQuizDetails([...quizDetails, {
            qid: props.location.state.quiz_id,
            ques_id: no,
            question: "",
            question_type: "tf"
        }])
        const data = {
            qid: props.location.state.quiz_id,
            ques_id: no,
            question: "",
            question_type: "tf"
        }
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
            };
        fetch(`http://127.0.0.1:5000/add_ques/${props.location.state.quiz_id}`, requestOptions)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(err => console.log(err))
    }

    useEffect(()=>{
        fetch("http://127.0.0.1:5000/quiz_ques/" + props.location.state.quiz_id).then(response => response.json()
        .then(data => {
            // console.log(data.data)
            const quesArr = data.data
            setQuizDetails(quesArr)
            // console.log(quizDetails)
        })).catch()
    },[])

    // useEffect(()=>{
    //     fetch("http://127.0.0.1:5000/ques_opt/" + props.location.state.quiz_id).then(response => response.json()
    //     .then(data => {
    //         // console.log(data.data)
    //     })).catch()
    // },[])
    const SaveDetails = () => {
        // console.log(props.quizCard.qid, props.quizCard.ques_id)
        const data = {
                quiz_id: props.location.state.quiz_id,
                quiz_name: quizName, 
                }
        // console.log(data)
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
            };
        fetch(`http://127.0.0.1:5000/quiz_update/${props.location.state.quiz_id}`, requestOptions)
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(err => console.log(err))   
    }

    return (
        <div>
            <h1>{props.location.state.uploader} 's</h1> 

            <Row>
            <Col sm='4'>
                <Form.Control onChange={ e => setQuizName(e.target.value)} as="textarea" rows={1} value={quizName} />
            </Col>
            <Col sm="8">
                <Link to="/account">
                <Button onClick={() => SaveDetails()} className="pull-right" variant="success">Save Quiz</Button>{' '}
                </Link>
            </Col>
            </Row>
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
            <hr></hr>
            <br></br>
            <div>
            <h1 className="col-md-4 mx-auto"> Add a Question </h1>
            <Stack gap={2} direction="horizontal" className="col-md-4 mx-auto">
                <Button onClick={AddMCQ} variant="outline-primary">Multiple Choice</Button>{' '}<Button onClick={AddTF} variant="outline-success">True / False</Button>{' '}
            </Stack>
            </div>
            <br></br>
            <hr></hr>
            <br></br>
            <br></br>
            <br></br>
            <br></br>
            <br></br>
        </div>
    )
}

export default IndividualQuiz