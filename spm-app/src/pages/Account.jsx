import React, { useState,useEffect } from 'react';
import Quizzes from '../component/Quizzes'
import { Stack , Button } from 'react-bootstrap';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import {faPlus} from '@fortawesome/free-solid-svg-icons';
import { Link, useHistory } from 'react-router-dom';

const Account = () => {
    const history = useHistory()
    const [quizzes, setQuizzes] = useState([]);
    const [role, setRole] = useState("");
    useEffect(() => {
        setRole(JSON.parse(localStorage.getItem("user")).role);
        
        fetch("http://127.0.0.1:5000/quiz").then(
            response => response.json()
            .then(data => {
                var xd = data.data;
                setQuizzes(xd)
            })
        ).catch(error => console.log(error))
    }, [])

    function addAndgoQuizDetails(){
        var let_new_qid = quizzes.length + 1
        var staff_username = JSON.parse(localStorage.getItem('user')).staff_username
        fetch(`http://127.0.0.1:5000/insert_quiz/${let_new_qid}/${staff_username}`).then(
            response => response.json()
            .then(
                goToQuizDet(let_new_qid)
            )
        ).catch(error => console.log(error))
    }
    const goToQuizDet = (new_qid) => {
        // console.log(new_qid)
        fetch("http://127.0.0.1:5000/quiz/"+new_qid).then(
            response => response.json()
            .then(data => {
                console.log(data.data)
                const goTo = {pathname:"/individualQuiz", state: data.data[0]}
                history.push(goTo)
                // window.location.reload(false);
            })
        ).catch(error => console.log(error))
    }
    // console.log(quizzes)
    return (
        <div style={{textAlign: "center"}}>
            
            <Stack gap={2} direction="horizontal" className="col-md-2 mx-auto">
                <Button type="button" onClick={() => addAndgoQuizDetails()} variant="success"><FontAwesomeIcon icon={faPlus}/></Button>
                <Quizzes quizzes={quizzes}/>
            </Stack>
            
        </div>
    )
}

export default Account
