import React from 'react';
// testing engineer details
import ViewEngineerDetails from '../component/EngineerDetails';
import AssignTrainer from '../component/AssignTrainer';
import { Container, Button } from 'react-bootstrap';
// import "../App.css";
const Admin = () => {
    return (
        <div>
            <h1>Admin</h1>

            <Container>
                <ViewEngineerDetails/>
            </Container>

            <Container>
                <AssignTrainer/>
            </Container>
            
        </div>
    )
}

export default Admin;