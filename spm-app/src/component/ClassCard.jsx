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
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    const today  = new Date();
    const startEnrol = new Date(classSchema.selfenrol_start)
    const endEnrol = new Date(classSchema.selfenrol_end)
    const [buttonHTML, setButtonHTML] =useState(<a href = {link}> <Button variant="primary">Enter Course</Button></a>)



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
    
        useEffect(() => {
            console.log(`${classSchema.course_id} - ${classSchema.class_no}`)
            console.log(!classSchema.selfenrol_start)
            console.log(today > startEnrol)
            console.log(today < endEnrol)

            if (!isEligible) {
                setButtonHTML(<Button variant="secondary" disabled>Not Eligible</Button>)
            }
            else if ((!classSchema.selfenrol_start) || today < startEnrol || today > endEnrol) {
                setButtonHTML(<Button variant="secondary" disabled>Class Unavailable</Button>)
            }
            else if (classNum >= classSchema.class_size) {
                setButtonHTML(<Button variant="secondary" disabled>Class Full</Button>)
            }
            else if (prop.inQueue.inQueue) {
                console.log(`${classSchema.class_no} - Withdraw`)
                setButtonHTML(<Button variant="danger" onClick={() => setModalShow(true)} >Withdraw enrollment</Button>)
            }
            else {
                console.log(`${classSchema.class_no} - Not Self`)
                setButtonHTML(<Button variant="primary"  onClick = {enrolClass}>Self Enroll</Button>)
            }
        },[isEligible,prop.inQueue.inQueue,classNum])

    return(
        <div className="border border-info container-fluid container-bg">
            <div className = 'd-flex justify-content-between'>
                <h2>Class {classSchema.class_no}</h2>
                {classSchema.selfenrol_start
                ?<p>Enrolment period: {(new Date(classSchema.selfenrol_start)).toLocaleDateString("en-US", options)} - {(new Date(classSchema.selfenrol_end)).toLocaleDateString("en-US", options)} </p>
                :<p>Enrolment period: Not Available </p>
                }
                <p className = 'class-text'>Slot: {classNum}/{classSchema.class_size}</p>
                {prop.inQueue.inQueue 
                ?<p className = 'text-danger' >Awaiting Confirmation </p>
                : ""
                }
            </div>
            
            <div className = 'd-flex justify-content-between'>
                <Container>
                    <p className = 'm-1'>Start date: {(new Date(classSchema.start_date)).toLocaleDateString("en-US", options)}</p>
                    <p className = 'm-1'>End date: {(new Date(classSchema.end_date)).toLocaleDateString("en-US", options)}</p>
                </Container>  

                <Container>
                    <p className = 'm-1'>Start Time: {classSchema.start_time}</p>
                    <p className = 'm-1'>End Time: {classSchema.end_time}</p>
                </Container>
                <Container className = 'my-auto text-center'>
                    {isCatalog 
                    ? buttonHTML
                    : (<a href = {link}> <Button variant="primary">Enter Course</Button></a>)}
                </Container>
                
            </div>
            
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