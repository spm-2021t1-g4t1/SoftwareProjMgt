import { React, useEffect, useState } from 'react'
import { Button, Stack, Form, Col, Row, Modal, Dropdown } from 'react-bootstrap';
import { useHistory } from "react-router-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faTrash } from '@fortawesome/free-solid-svg-icons';
import QuestionCard from './QuestionCard';

const IndividualQuiz = (props) => {
    const history = useHistory();
    // const [quizDetails, setQuizDetails] = useState(quiz);
    // const  {quiz} = useLocation()
    // console.log('saddasasdadsadsads',props)
    const [quizDetails, setQuizDetails] = useState([]);

    const [quizName, setQuizName] = useState(props.location.state.quiz_name);
    const [quizDuration, setQuizDuration] = useState(props.location.state.duration);
    const [errMsg, setErrMsg] = useState("");
    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);
    const [courseSec, setCourseSec] = useState([]);
    const [assignQuizName, setassignQuizName] = useState("");

    useEffect(() => {
        console.log("This is my quiz id", props.location.state.quiz_id)
        // let retlist = quizDetails
        fetch(`http://127.0.0.1:5000/get_lesson_of_quiz/${props.location.state.quiz_id}`)
            .then(response => response.json())
            .then(data => setassignQuizName(`You have assigned this quiz to Course_ID ${data.data.course_id}, Class No: ${data.data.class_no} and Lesson No: ${data.data.lesson_no}`))
            .catch(err => {
                setassignQuizName("Assign a Quiz")
            })
        
    }, [])


    useEffect(() => {
        console.log("This is my quiz id", props.location.state.quiz_id)
        // let retlist = quizDetails

        console.log(props);
    }, [props, quizDetails])


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

    useEffect(() => {
        fetch("http://127.0.0.1:5000/quiz_ques/" + props.location.state.quiz_id).then(response => response.json()
            .then(data => {
                // console.log(data.data)
                const quesArr = data.data
                setQuizDetails(quesArr)
                // console.log(quizDetails)
            })).catch()
    }, [props.location.state.quiz_id])

    // useEffect(()=>{
    //     fetch("http://127.0.0.1:5000/ques_opt/" + props.location.state.quiz_id).then(response => response.json()
    //     .then(data => {
    //         // console.log(data.data)
    //     })).catch()
    // },[])
    const SaveDetails = () => {
        // console.log(props.quizCard.qid, props.quizCard.ques_id)
        setErrMsg("");

        // FIXME - basic validation of duration format - NOT SAFE!!!!!!!!
        if (!quizDuration.match(/^\d:\d{2}:\d{2}$/)) {
            setErrMsg("Invalid duration format. Please input duration as H:MM:SS and submit again.");
            return;
        }

        // submit query
        const data = {
            quiz_id: props.location.state.quiz_id,
            quiz_name: quizName,
            duration: quizDuration
        }
        // console.log(data)
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        };
        fetch(`http://127.0.0.1:5000/quiz_update/${props.location.state.quiz_id}`, requestOptions)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                history.push("/account");
            })
            .catch(err => console.log(err))
    }
    const DeleteQuiz = () => {
        // /quiz_delete/<int:quiz_id>
        fetch(`http://127.0.0.1:5000/quiz_delete/${props.location.state.quiz_id}`)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                history.push("/account");
                window.location.reload(false);
            })
            .catch(err => console.log(err))
    }

    useEffect(() => {
        fetch("http://127.0.0.1:5000/lesson")
        .then(response => response.json())
        .then(lesson_data => {
                // console.log(data.data)
                const data = lesson_data.data
                // console.log(data)
                setCourseSec(data)
                // console.log(quizDetails)
            }).catch()
    }, [])

    const assignQuiz = (course_id, class_no, lesson_no, quiz_assigned_id) => {
        // console.log(course_id, class_no, lesson_no, quiz_assigned_id)
        fetch(`http://127.0.0.1:5000/update_assign_quiz/${course_id}/${class_no}/${lesson_no}/${quiz_assigned_id}`)
        .then(response => response.json())
        .then(data => {
            console.log(data.code)
            if(data.code === 200){
                // console.log("testing")
                setassignQuizName(`You have assigned this quiz to Course_ID ${data.data.course_id}, Class No: ${data.data.class_no} and Lesson No: ${data.data.lesson_no}`)
            } 
            console.log(data)
        
        })
        .catch()
    }
    
    return (
        <div>
            <h1>{props.location.state.uploader} 's</h1>

            <Row>
                <Col sm='4'>
                    <Form.Label>Quiz Name</Form.Label>
                    <Form.Control size="lg" onChange={e => setQuizName(e.target.value)} type="text" value={quizName} />
                </Col>
                <Col sm='2'>
                    <Form.Label>Quiz Duration</Form.Label>
                    <Form.Control onChange={e => setQuizDuration(e.target.value)} type="text" value={quizDuration} />
                </Col>
                <Col sm='2'>
                <Dropdown>
                        <Dropdown.Toggle variant="info" id="dropdown-basic">
                            {assignQuizName}
                        </Dropdown.Toggle>

                        <Dropdown.Menu>

                        {courseSec.map(singleSec => {
                        return(
                            <div key={singleSec.lesson_name}>
                            <Dropdown.Item onClick={() => assignQuiz(singleSec.course_id, singleSec.class_no, singleSec.lesson_no, props.location.state.quiz_id)}>
                                {singleSec.lesson_name}
                            </Dropdown.Item>
                            </div>
                            )
                        })}
                        </Dropdown.Menu>
                        
            </Dropdown>
                </Col>
                <Col sm="2">
                    <Button onClick={() => SaveDetails()} className="pull-right" variant="success">Save Quiz</Button>{' '}
                </Col>
                <Col sm="2">
                    <Button onClick={() => handleShow()} variant="danger"> <FontAwesomeIcon icon={faTrash}/> </Button>{' '}
                    <Modal show={show} onHide={handleClose}>
                        <Modal.Header closeButton>
                        <Modal.Title>Delete Quiz?</Modal.Title>
                        </Modal.Header>
                        <Modal.Body>Are you sure you want to delete this entire quiz?</Modal.Body>
                        <Modal.Footer>
                        <Button variant="secondary" onClick={handleClose}>
                            Close
                        </Button>
                        <Button variant="danger" onClick={() => DeleteQuiz()}>
                            Confirm Delete
                        </Button>
                        </Modal.Footer>
                    </Modal>
                </Col>
            </Row>
            <Row>
                <Col>{errMsg}</Col>
            </Row>
            <br></br>
            <hr></hr>
            <br></br>
            <Stack gap={2}>
                {quizDetails.map(quiz => {
                    return (
                        <QuestionCard key={quiz.ques_id} quizCard={quiz} />
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