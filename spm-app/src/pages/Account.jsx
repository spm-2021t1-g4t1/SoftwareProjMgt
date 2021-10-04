import React, { useState,useEffect } from 'react';
import axios from 'axios';
import Quizzes from '../component/Quizzes'

const Account = () => {
    const [quizzes, setQuizzes] = useState([]);
    
    useEffect(() => {
        fetch("http://127.0.0.1:5000/quiz").then(
            response => response.json()
            .then(data => {
                var xd = data.data;
                setQuizzes(xd)
            })
        ).catch(error => console.log(error))
    }, [])
    
    // console.log(quizzes)
    return (
        <div style={{textAlign: "center"}}>
            <p>Uploaded quizzes</p>
            <Quizzes quizzes={quizzes}/>
        </div>
    )
}

export default Account
