import React from 'react';
import { useState, useEffect } from 'react';
import { useParams ,useHistory } from "react-router-dom"
import { Button, Table, Modal } from 'react-bootstrap';
import { MdAssignmentTurnedIn} from "react-icons/md";

import SearchBox from '../../component/SearchBox';

function AssignEngineerForm(prop) {
    const history = useHistory()
    const courseid = useParams().courseid
    const classno = useParams().classno

    const endpoint = 'http://127.0.0.1:5000/staff/engineers';
    const [engineers, setEngineers] = useState([])
    const [searchTerm, setSearchTerm] = useState('')
    const [modalShow, setModalShow] = useState(false);
    const [selectedEngr, setSelectedEngr] = useState('')

    useEffect(() => {fetch(endpoint).then(
        response => response.json()
        .then(data => {
            // console.log(data.data)
            const engArr = data.data
            setEngineers(engArr)
            
        })
    ).catch()
    }, [])
    
    function buttontrigger(engrs){
        setModalShow(true)
        setSelectedEngr(engrs)
    }

    function assignTrainer() {
        const endpoint = `http://127.0.0.1:5000/class/assign`
        const data = {
            course_id : courseid,
            class_no : classno,
            staff_username: selectedEngr
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
            setModalShow(false)
            prop.statechange()
            history.push("/Administrator/Course/unassigned")
        })
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
              Are you sure you wish to assign {selectedEngr} as the trainer ?
              </p>
            </Modal.Body>
            <Modal.Footer>
              <Button onClick={props.onHide}>No</Button>
              <Button variant='danger' onClick={props.func}>Yes</Button>
            </Modal.Footer>
          </Modal>
        );
      }
    
    return (
        <div className="EngineerDetails">
            <h1>Assign Engineer</h1>
            <SearchBox placeholder = 'Enter Name' handleChange = {(e) => setSearchTerm(e.target.value)}/>

            <Table hover responsive hover variant="light" className = 'admin-table' >
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Role</th>
                        <th>Department</th>
                        <th>Current Designation</th>
                        <th></th>
                    </tr>
                </thead>

                <tbody>

                    {engineers.filter((val) => {
                        if (searchTerm === "") {
                            return val
                        } else if (val.staff_name.toLowerCase().includes(searchTerm.toLowerCase())) {
                            return val
                        }
                        return null
                    }).map((val) => {
                        // console.log(val)
                        return (
                            <tr>
                                <td>{val.staff_name}</td>
                                <td>{val.role}</td>
                                <td>{val.department}</td>
                                <td>{val.current_designation}</td>
                                <td>
                                    <Button className ='mx-1' size="sm" variant = 'outline-primary' onClick={() => buttontrigger(val.staff_username)}>
                                        <MdAssignmentTurnedIn />
                                    </Button>
                                </td>
                            </tr>
                        )
                    })}
                </tbody>
            </Table>
            <DoubleCheck
                show={modalShow}
                func = {() => assignTrainer()}
                onHide={() => setModalShow(false)}
            />
        </div>
    );
}




export default AssignEngineerForm
