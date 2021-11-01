import React, { useState,useEffect } from 'react';
import Quizzes from '../component/Quizzes'

const Account = () => {
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

    
    
    // console.log(quizzes)
    return (
        <div style={{textAlign: "center"}}>
            {role === "Trainer" ? <div>
                <p>Uploaded quizzes</p>
                <Quizzes quizzes={quizzes}/>
            </div> : <div></div>}
        </div>
    )
}

export default Account
