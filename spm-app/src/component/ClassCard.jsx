import React , {useEffect, useState} from 'react';
import { Modal, Container, Button } from 'react-bootstrap';

const ClassCard = (prop) => {
   
    // Variable
    const classSchema = prop.classSchema
    const link = `course/${classSchema.course_id}/${classSchema.class_no}/overview`
    const isCatalog = window.location.pathname.includes('catalog')
    const [modalShow, setModalShow] = useState(false);
    const [classNum, setClassNum] = useState(0)
    const [isEligible, setIsEligible] = useState(true)



    function enrolClass() {
        const endpoint = `http://127.0.0.1:5000/queue/darrelwilde/${classSchema.course_id}`
        const data = {class_no: classSchema.class_no}
        fetch(endpoint,{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then((res) => res.json()) 
        .then((result) => {
        // console.log(result)
        prop.classChange()

        })
    }

    function withdrawClass() {
        const endpoint = `http://127.0.0.1:5000/queue/withdraw`
        const data = {
            staff_username: "darrelwilde",
            course_id: classSchema.course_id
        }
        fetch(endpoint,{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then((res) => res.json()) 
        .then((result) => {
        // console.log(result)
        setModalShow(false)
        prop.classChange()
        
        window.location.reload(false)
        })
    }

        useEffect(() => {

            if (isCatalog) {

                const endpoint = `http://127.0.0.1:5000/enrolment/${classSchema.course_id}/${classSchema.class_no}/length`
                fetch(endpoint)
                .then((res) => res.json()) 
                .then((result) => {
                // console.log(result)
                    setClassNum(result.message)
        
                })
                if (prop.hasPrereq) {
                    const endpoint1 = `http://127.0.0.1:5000/eligiblity/${classSchema.course_id}/darrelwilde`
                    fetch(endpoint1)
                    .then((res) => res.json()) 
                    .then((result) => {
                    // console.log(classSchema.course_id)
                    // console.log(result.eligiblity)
                    setIsEligible(result.eligiblity)
                    })
                }


            }



        },[])
    


    return(
        <div className="border border-info container-fluid container-bg">
            <div className = 'd-flex justify-content-between'>
                <h2>Class {classSchema.class_no}</h2>
                <p className = 'class-text'>Slot: {classNum}/{classSchema.class_size}</p>
            </div>
            
            <div className = 'd-flex justify-content-around'>
                <Container>
                    <p className = 'm-1'>Start date: {classSchema.start_date}</p>
                    <p className = 'm-1'>End date: {classSchema.end_date}</p>
                </Container>  

                <Container>
                    <p className = 'm-1'>Start Time: {classSchema.start_time}</p>
                    <p className = 'm-1'>End Time: {classSchema.end_time}</p>
                </Container>
                <Container className = 'my-auto'>
                    {isCatalog 
                    ? isEligible
                        ? prop.inQueue.inQueue 
                            ? (<p className = 'text-danger' >Awaiting Confirmation </p>)
                            : (<Button variant="primary"  onClick = {enrolClass}>Self Enroll</Button>)
                        : (<Button variant="secondary" disabled>Not Eligible</Button>)
                    : (<a href = {link}> <Button variant="primary">Enter Course</Button></a>)}
                </Container>
            </div>
            {prop.inQueue.inQueue 
                ? ( <Container className="d-flex justify-content-end pb-2">
                    <Button variant="danger" onClick={() => setModalShow(true)} >Withdraw enrollment</Button>
                </Container>
                ):''}
            
            <DoubleCheck
                show={modalShow}
                func = {() => withdrawClass()}
                onHide={() => setModalShow(false)}
            />
        </div>
        
    )

    
}

function DoubleCheck(props) {
    return (
      <Modal
        {...props}
        size="lg"
        aria-labelledby="DoubleCheck"
        centered
      >
        <Modal.Header closeButton>
        </Modal.Header>
        <Modal.Body>
          <h4>Confirmation</h4>
          <p className = 'py-2'>
          Are you sure you wish to withdraw your enrollment ?
          </p>
        </Modal.Body>
        <Modal.Footer>
          <Button onClick={props.onHide}>No</Button>
          <Button variant='danger' onClick={props.func}>Yes</Button>
        </Modal.Footer>
      </Modal>
    );
  }

export default ClassCard