import { React, useEffect, useState } from 'react'
import { Button, Stack, Card , Form, Row, Col, Modal} from 'react-bootstrap';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faEdit, faArrowDown, faArrowUp, faTrash, faCopy, faSave, faPlus, faUndo } from '@fortawesome/free-solid-svg-icons';


const QuestionCard = (props) => {
    const [isEditting, setisEditting] = useState(false)
    const [optionsList, setoptionsList] = useState([])
    const [questionName, setquestionName] = useState(props.quizCard.question)
    const [show, setShow] = useState(false);

    useEffect(()=>{
        fetch("http://127.0.0.1:5000/ques_opt/" + props.quizCard.qid + "/" + props.quizCard.ques_id).then(response => response.json()
        .then(data => {
            // console.log(data.data)
            const optArr = data.data
            setoptionsList(optArr)
        })).catch()
    },[props.quizCard.qid,props.quizCard.ques_id])
    //
    const toggleEdit = () => {
        setisEditting(!isEditting);
    }

    const tickBox = (optid) => {
        // console.log(optid)
        let retlist = [...optionsList]
        for(let opt of retlist){
            if( opt.opts_id === optid){
                console.log(opt.is_right)
                opt.is_right = !opt.is_right
            }  
        }
        setoptionsList(retlist)

    }

    // useEffect(()=>{
    //     console.log(questionName)
    // }, [questionName, optionsList])

    const handleOpt = (eventValue, OptID) => {
        let retlist = [...optionsList]
        for(let opt of retlist){
            if( opt.opts_id === OptID){
                opt.qopt = eventValue
            }  
        }
        setoptionsList(retlist)
    }


    const AddOption = () => {
        console.log(props.quizCard.question_type)
        let num_of_ques = optionsList.length
        if(props.quizCard.question_type === "mcq"){
            let no = optionsList.length + 1
            setoptionsList([...optionsList, {opts_id: no, ques_id: props.quizCard.ques_id, quiz_id: props.quizCard.qid, is_right: 0 }])
        } else if(props.quizCard.question_type === "tf" && num_of_ques < 2){
            console.log("boop!")
            let no = optionsList.length + 1
            setoptionsList([...optionsList, {opts_id: no, ques_id: props.quizCard.ques_id, quiz_id: props.quizCard.qid, is_right: 0 }])
        }
    }
    const handleClose = () => {
        setShow(false)
    };
    const removeQues = (quiz_id, ques_id) => {
        try {
            fetch("http://127.0.0.1:5000/ques_delete/" + quiz_id + "/" + ques_id).then(response => response.json()
            .then(data => {
                // console.log(data.data)
                console.log(data)
                handleClose()
                window.location.reload(false);
            })).catch(err => console.log(err))
        }
        catch(err){
            console.log(err) 
        }
    }
    const handleShow = () => {setShow(true)};
    
    const RemoveOpt = (OptID) => {
        console.log(OptID)
        try {
            let removeList = [...optionsList]
            let items = removeList.filter(row => row.opts_id !== OptID);
            setoptionsList(items);
            fetch("http://127.0.0.1:5000/ques_opt_delete/" + props.quizCard.qid + "/" + props.quizCard.ques_id + "/" + OptID).then(response => response.json()
            .then(data => {
                handleClose()
            })).catch(err => console.log(err))
        }
        catch(err){
            console.log(err) 
        }
    }

    const SaveDetails = () => {
        const data = {
                question: questionName,
                optionsList: optionsList 
                }
        // console.log(data)
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
            };
        fetch(`http://127.0.0.1:5000/ques_opt_update/${props.quizCard.qid}/${props.quizCard.ques_id}`, requestOptions)
            .then(response => response.json())
            .then(() => {
                toggleEdit()
                window.location.reload(false);
            })
            .catch(err => console.log(err))
            
            
    }

    let result;
  if (isEditting) {
    result = (
        <Card className="mt-5">
        <Card.Body>
        <Card.Title>#{props.quizCard.ques_id}</Card.Title>
        <Form>
        <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
            <Form.Label> Question: </Form.Label>
            <Form.Control as="textarea" rows={3} onChange={e => setquestionName(e.target.value)} value={questionName} />
            {optionsList.map(opt => {
                return(
                    <Form.Group as={Row} key={opt.opts_id} className="mt-5">
                        <Col md="1">
                            <Form.Check aria-label="option 1" defaultChecked={opt.is_right} onChange={() => tickBox(opt.opts_id)}/>
                        </Col>
                        <Col md="9">
                            <Form.Control onChange={ e => handleOpt(e.target.value, opt.opts_id)} as="textarea" rows={1} value={opt.qopt} />
                        </Col>
                        <Col md="2">
                            <Button onClick={() => handleShow()} type="button" variant="danger"><FontAwesomeIcon icon={faTrash}/></Button>
                            <Modal show={show} onHide={handleClose} animation={false}>
                                <Modal.Header closeButton>
                                <Modal.Title>Modal heading</Modal.Title>
                                </Modal.Header>
                                <Modal.Body>Are you sure you want to remove this Option?</Modal.Body>
                                <Modal.Footer>
                                <Button variant="secondary" onClick={handleClose}>
                                    Close
                                </Button>
                                <Button variant="danger" onClick={() => RemoveOpt(opt.opts_id)}>
                                    Confirm
                                </Button>
                                </Modal.Footer>
                            </Modal>
                            
                        </Col>
                    </Form.Group>
                )
            })}
        </Form.Group>
        </Form>
            <Stack gap={2} direction="horizontal" className="col-md-2 mx-auto">
                <Button type="button" onClick={AddOption} variant="success"><FontAwesomeIcon icon={faPlus}/></Button>
                <Button type="button" onClick={SaveDetails} variant="primary"><FontAwesomeIcon icon={faSave}/></Button>
                <Button type="button" onClick={toggleEdit} variant="warning"><FontAwesomeIcon icon={faUndo}/></Button>
            </Stack>
            </Card.Body>
        </Card>
    );
  } else {
    result = (
        <Card key={props.quizCard.ques_id} className="mt-5">
        <Card.Body>
        <Card.Title>#{props.quizCard.ques_id}</Card.Title>
            {props.quizCard.question}
            {optionsList.map(opt => {
                return(
                    <Card key={opt.opts_id} className="mt-5">
                        <Card.Body>
                            {opt.qopt}
                        </Card.Body>
                    </Card>
                )
            })}
            <br></br>
            <br></br>
            <br></br>
            <Stack gap={2} direction="horizontal" className="col-md-2 mx-auto">
                <Button type="button" onClick={toggleEdit} variant="primary"><FontAwesomeIcon icon={faEdit}/></Button>
                <Button type="button" variant="primary"><FontAwesomeIcon icon={faArrowUp}/></Button>
                <Button type="button" variant="primary"><FontAwesomeIcon icon={faArrowDown}/></Button>
                <Button type="button" onClick={() => handleShow()} variant="danger"><FontAwesomeIcon icon={faTrash}/></Button>
                <Modal show={show} onHide={handleClose} animation={false}>
                    <Modal.Header closeButton>
                    <Modal.Title>Modal heading</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>Are you sure you want to remove this question? <br></br>
                    {props.quizCard.question}</Modal.Body>
                    <Modal.Footer>
                    <Button variant="secondary" onClick={handleClose}>
                        Close
                    </Button>
                    <Button variant="danger" onClick={() => removeQues(props.quizCard.qid,props.quizCard.ques_id)}>
                        Confirm
                    </Button>
                    </Modal.Footer>
                </Modal>
                <Button type="button" variant="secondary"><FontAwesomeIcon icon={faCopy}/></Button>
            </Stack>
            </Card.Body>
        </Card>
    );
  }
    return result
}

export default QuestionCard