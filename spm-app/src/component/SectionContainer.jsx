import React, { useState, useEffect } from 'react'
import { Button, Container } from 'react-bootstrap';

const SectionContainer = (props) => {
    console.log(props.data)

    // eslint-disable-next-line
    const [sectionArrs, setSectionArrs] = useState(props.data)
    const sectionNumber = props.number
    const [isCompleted, setIsCompleted] = useState(false)

    // console.log(props.data.lesson_materials)
    function markLessonAsComplete() {
        const endpoint = `http://localhost:5000/lesson_completion/mark_complete`
        const data = { course_id: props.data.course_id, class_no: props.data.class_no, lesson_no: props.data.lesson_no, staff_username: 'darrelwilde' }
        console.log(data)
        fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then((res) => res.json())
            .then((result) => {
                console.log(result)
                setIsCompleted(true)

            })
    }

    useEffect(() => {
        setIsCompleted(sectionNumber <= props.completedLesson)
    },[props.completedLesson])

    return (
        <Container className='sectionCon'>
            <div className=' sectionCon-Top'>
                <h1>{sectionNumber} {sectionArrs['lesson_name']}</h1>
            </div>
            <Container className='border border-info container-bg my-3'>
                <div className='sectionCon-Description'>
                    <h2>Description</h2>
                    <p>
                        {sectionArrs['lesson_description']}
                    </p>
                </div>
                <Container className='d-flex justify-content-between container-md flex-wrap'>
                    <div>
                        <h2>Course Material</h2>
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
                            ? <Button className = 'm-1' variant='success'> Completed </Button>
                            : <Button className = 'm-1' variant='primary' onClick={markLessonAsComplete}>Mark as Completed</Button>

                        }
                        <Button className = 'm-1'varient='primary'>Take Quiz</Button>
                    </div>
                </Container>
            </Container>
        </Container>
    )
}

export default SectionContainer
