import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { Button, Table } from 'react-bootstrap';
import { MdArrowBack, MdAssignmentTurnedIn } from "react-icons/md";

const AssignEnrol = () => {
    const course_id = useParams().courseid;
    const class_no = useParams().classno;
    const endpoint = `http://127.0.0.1:5000/eligibility/${course_id}`;
    const [engineers, setEngineers] = useState([]);
    const [courseData, setCourseData] = useState({});

    useEffect(() => {
        // get list of eligible engineer IDs
        fetch(endpoint)
            .then(res => res.json())
            .then(data => {
                // for each eligible engineer, get their details
                const engineerIds = data.data;
                for (const engineerId of engineerIds) {
                    fetch(`http://127.0.0.1:5000/staff/${engineerId}`)
                        .then(res => res.json())
                        .then(data => setEngineers([...engineers, data.data]));
                }
            });

        fetch(`http://127.0.0.1:5000/course/${course_id}`)
            .then(res => res.json())
            .then(data => setCourseData(data.data));
    }, [])

    const handleClick = (staff_username) => {
        const data = {
            staff_username: staff_username,
            course_id: course_id,
            class_no: class_no
        }

        fetch(`http://127.0.0.1:5000/enrolment/enrol`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(result => {
            setEngineers(engineers.filter(engineer => engineer.staff_username != staff_username));
            console.log(result);
        })
        
    }

    console.log(engineers)
    return (
        <>
            <Link to={`/Administrator/Course/list`}>
                <Button variant="outline-primary" >
                    <MdArrowBack />
                </Button>
            </Link>
            <h3>Assign Enrolment</h3>
            <h4>For course: <strong>{courseData.course_name}</strong>, Class {class_no}</h4>

            <Table hover responsive hover variant="light" className='admin-table' >
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Role</th>
                        <th></th>
                    </tr>
                </thead>

                <tbody>
                    {engineers.length ? engineers.map(engineer =>
                        <tr>
                            <td>{engineer.staff_name}</td>
                            <td>{engineer.role}</td>
                            <td>
                                <Button className='mx-1' size="sm" variant='outline-primary' onClick={() => handleClick(engineer.staff_username)}>
                                    <MdAssignmentTurnedIn />
                                </Button>
                            </td>
                        </tr>
                    )
                    :
                    <h4 className="mt-4">No eligible learners</h4>}
                </tbody>

            </Table>
        </>
    );
}

export default AssignEnrol;