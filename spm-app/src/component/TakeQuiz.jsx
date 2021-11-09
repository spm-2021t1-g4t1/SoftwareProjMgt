import React, { useState, useEffect} from 'react'
import { Modal, Button, Container, Card, InputGroup,FormControl, Form } from 'react-bootstrap';
import { useHistory } from "react-router-dom";

const TakeQuiz = (props) => {

    const course_id = props.location.state[0]
    const class_no = props.location.state[1] 
    const lesson_no = props.location.state[2]
    const user = JSON.parse(localStorage.getItem('user'))
    const history = useHistory()
    const [getQuiz_data, setgetQuiz_data] = useState([]);
    const [getDuration, setgetDuration] = useState([]);
    const [getQuestions, setgetQuestions] = useState([]);
    const [getquizName, setgetquizName] = useState([]);
    const [getOptVal, setgetOptVal] = useState({});
    const [show, setShow] = useState(false);
    useEffect(() => {
        // let retlist = quizDetails
        fetch(`http://127.0.0.1:5000/get_assigned_quiz/${course_id}/${class_no}/${lesson_no}`)
            .then(response => response.json())
            .then(data => {
                const quiz_data = data.data
                setgetQuiz_data(quiz_data)
                setgetDuration(quiz_data.duration)
                setgetQuestions(quiz_data.question)
                setgetquizName(quiz_data.quiz_name)
                
            })
            .catch(err => console.log(err))
    }, [])
    const tabulateMarks = () => {
        let total = 0
        for(let key in getOptVal){
            total = total + getOptVal[key]
        }
        console.log( course_id, class_no, lesson_no, user.staff_username, total )
        fetch(`http://127.0.0.1:5000/update_quiz_score/${course_id}/${class_no}/${lesson_no}/${user.staff_username}/${total}`)
            .then(response => response.json())
            .then(data => {
                if(data.code === 200){
                    const goTo = {
                        pathname: `/course/${course_id}/${class_no}/curriculum` ,
                        state: data.data
                    }
                    history.push(goTo)
                }
            })
            .catch(err => console.log(err))
    }
    
    useEffect(() => {
        let tempObj = {...getOptVal}
        getQuestions.forEach((value) => {
            tempObj[value.ques_id] = 0
        })
        setgetOptVal(tempObj)
    },[getQuestions])

    const optVal = (ques_id, is_right) => {
        getOptVal[ques_id] = is_right
        
    }

    const handleClose = () => setShow(false);
    const handleShow = (e) => {
        e.preventDefault()
        setShow(true)
    };

    return (
        <div className= 'my-4' > 
            <div className="border border-dark container-fluid container-bg">    
                <h2 className="p-1">Time Left: {getDuration} </h2>
                <Form onSubmit={(e)=>handleShow(e)}>
                {
                    getQuestions.map(ques => {
                        console.log(ques)
                        return (
                            
                        <Card>
                            <Card.Header>Question: {ques.ques_id}</Card.Header>
                            <Card.Body>
                            <Card.Title>Answer the question below:</Card.Title>
                            <Card.Text>
                                {ques.question}
                            </Card.Text>
                            
                                {
                                    ques.question_option.map(option => {
                                        console.log(option)
                                        return (
                                            <Form.Group controlId={option.ques_id}>
                                                <InputGroup>
                                                    <InputGroup.Radio name={option.ques_id} onChange={() => optVal(option.ques_id, option.is_right)} value={option.opts_id}/>
                                                    <FormControl value={option.qopt}/> 
                                                </InputGroup>
                                            </Form.Group>
                                        )
                                    })
                                }
                            </Card.Body>
                        </Card>
                      )
                    })
                }
                <Button className="pull-right" type="submit" variant="danger">Submit</Button>{' '}
                <Modal show={show} onHide={handleClose}>
                    <Modal.Header closeButton>
                    <Modal.Title>Quiz Submission Confirmation</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>Are you sure you want to submit the quiz?</Modal.Body>
                    <Modal.Footer>
                    <Button variant="secondary" onClick={handleClose}>
                        Close
                    </Button>
                    <Button variant="primary" onClick={()=>tabulateMarks()}>
                        Submit Quiz
                    </Button>
                    </Modal.Footer>
                </Modal>
                </Form>
            </div>
        </div>
        )
    }
export default TakeQuiz
