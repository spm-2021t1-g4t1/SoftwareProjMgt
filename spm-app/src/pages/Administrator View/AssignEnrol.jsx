import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { Button, Table } from 'react-bootstrap';
import { MdArrowBack} from "react-icons/md";

const AssignEnrol = () => {
    const course_id = useParams().courseid;
    const class_no = useParams().classno;
    const endpoint = `http://127.0.0.1:5000/eligibility/${course_id}`;
    const [engineers, setEngineers] = useState([]);
    const [courseData, setCourseData] = useState({});

    useEffect(() => {
        fetch(endpoint)
        .then(res => res.json())
        .then(data => {
            const engineerIds = data.data;

            for (const engineerId of engineerIds) {
                fetch(`http://127.0.0.1:5000/staff/${engineerId}`)
            }
        });

        fetch(`http://127.0.0.1:5000/course/${course_id}`)
        .then(res => res.json())
        .then(data => setCourseData(data.data));
    }, [])

    
    return (
        <>
            <Link to={`/Administrator/Course/list`}>
                <Button variant ="outline-primary" >
                    <MdArrowBack />
                </Button>
            </Link>
            <h3>Assign Enrolment</h3>
            <h4>For course: <strong>{courseData.course_name}</strong>, Class {class_no}</h4>
        </>
    );
}

export default AssignEnrol;