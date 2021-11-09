import React, { useState, useEffect } from 'react'
import { Modal, Button, Container } from 'react-bootstrap';

const SectionContainer = (props) => {
    console.log(props.data)




    return (
        <Container className='my-2'>
            <div className="border border-info container-fluid container-bg">
                <h2>{sectionNumber} {sectionArrs['lesson_name']}</h2>
            </div>
            <Container className='border border-info container-bg pt-3 mb-3'>
                <div className='sectionCon-Description'>
                    <h3>Description</h3>
                    <p>
                        {sectionArrs['lesson_description']}
                    </p>
                </div>
                <Container className='d-flex justify-content-between container-md flex-wrap my-2'>
                    <div>
                        <h3>Course Material</h3>
                        <ul>
                            {sectionArrs['lesson_materials'].map((mat, index) =>
                                <li key={mat['lesson_no']+"-"+mat['course_material_title']}>
                                    <a href={mat['link']}>{mat['course_material_title']}</a>
                                </li>
                            )}
                        </ul>
                    </div>

                    <div className='my-auto'>
                        {
                            isCompleted 
                            ? <Button className = 'm-1' variant='success' > Completed </Button>
                            : <Button className = 'm-1' variant='primary' onClick={() => setModalShow(true)}>Mark as Completed</Button>

                        }
                    </div>

                    <DoubleCheck
                    show={modalShow}
                    func = {() => markLessonAsComplete()}
                    onHide={() => setModalShow(false)}
                    />
                </Container>
                <Container className='d-flex justify-content-between container-md flex-wrap my-2'>
                    <div className="align-middle">
                        <h3 className="my-3">Quiz Score: {
                        props.data.quiz_score
                        ? props.data.quiz_score + "/100"
                        : "Unattempted"
                        }</h3>
                    </div>

                    <div className='my-auto'>
                        <Button className = 'm-1'varient='primary'>Take Quiz</Button>
                    </div>
                </Container>
            </Container>
        </Container>
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
            Are you sure you reviewed your lessons ?
          </p>
        </Modal.Body>
        <Modal.Footer>
          <Button onClick={props.onHide}>No</Button>
          <Button variant='danger' onClick={props.func}>Yes</Button>
        </Modal.Footer>
      </Modal>
    );
  }

export default SectionContainer
