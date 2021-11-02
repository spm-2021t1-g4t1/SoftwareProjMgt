import React from 'react';
import { useState, useEffect } from 'react';
import { Button, Col, Row } from 'react-bootstrap';

function CourseListAdmin() {
    const endpoint = 'http://127.0.0.1:5000/class/get_futureClass';
    const [courseList, setCourseList] = useState([]);
    useEffect(() => {
        fetch(endpoint)
            .then(res => res.json())
            .then(data => {
                setCourseList(data.data);
            })
    }, [])

    console.log(courseList);


    return (
        <div>
            <div className="border border-info container-fluid container-bg">
                <Col md={12}>
                    <Row>
                        <h2>Pending classes</h2>
                    </Row>

                    {courseList.map(course =>
                        <ClassEnrolDateCard course={course} key={course.course_id.toString() + course.class_no.toString()} />
                    )}

                </Col>
            </div>
        </div>
    )
}

const ClassEnrolDateCard = ({ course }) => {
    const [selfEnrolStart, setSelfEnrolStart] = useState(course.selfenrol_start);
    const [selfEnrolEnd, setSelfEnrolEnd] = useState(course.selfenrol_end);
    const [ freshlySaved, setFreshlySaved ] = useState(false);
    const endpoint = "http://127.0.0.1:5000/class/setSelfEnrolDates"

    const handleSubmit = () => {
        const data = {
            course_id: course.course_id,
            class_no: course.class_no,
            selfenrol_start: selfEnrolStart,
            selfenrol_end: selfEnrolEnd
        }
        try {
            
            fetch(endpoint, {
                method: "POST",
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            }).then(response => response.json())
            .then(data => {
                console.log(data);
                setFreshlySaved(true);
                setTimeout(() => setFreshlySaved(false), 3000);
            })
        } catch (err) {
            console.log(err)
        }
    }

    return (
        <div>
            <Row className="mt-4 border border-primary">
                <Col md={4} className="px-4">
                    <Row><strong>{course.course_name}</strong></Row>
                    <Row>Class {course.class_no}</Row>
                    <Row>Start date: {course.start_date}</Row>
                </Col>
                <Col md={4}>Set self-enrol start date:
                    <input type="date" value={selfEnrolStart} onInput={(e) => setSelfEnrolStart(e.target.value)} />
                </Col>
                <Col md={4}>Set self-enrol end date:
                    <input type="date" value={selfEnrolEnd} onInput={(e) => setSelfEnrolEnd(e.target.value)} />
                </Col>
            <Row>
                <Col md={4} className="my-2">
                    {freshlySaved ? 
                    <Button variant="success" onClick={handleSubmit}>Changes saved!</Button> 
                    : 
                    <Button variant="primary" onClick={handleSubmit}>Save Changes</Button>}
                </Col>
            </Row>
            </Row>
        </div>
    )
}

export default CourseListAdmin;