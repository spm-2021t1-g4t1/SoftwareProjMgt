import React, { useState,useEffect } from 'react';
import { Link } from "react-router-dom";
import axios from 'axios';

const Account = () => {
    // const [quiz, sectionname] = useState({});
    // const fetchQuiz = async () => {
    //     const res = await axios.get('http://localhost:3003/quiz');
    //     quiz(res.data)
    // }
    const [Data,setData]=useState({
        quiz_name:'',
        description:''
    })
    useEffect(()=>{
        axios.get('http://localhost:3003/quiz')
            .then(res=>{
                console.log('Response from main API: ',res)
                console.log('Home Data: ',res.data)
                let jsondata=res.data;
                setData({quiz_name:jsondata.quiz_name,description:jsondata.description})
            })
            .catch(err=>{
                console.log(err);
            })
    },[])

//     useEffect(() => {
//         getallQuizzes();
//    }, []);

//     const getallQuizzes = () => {axios({
//         url:'http://localhost:3003/quiz',
//     }).then(res=>{
//         console.log(res.data);
//         const allQuiz = res.data;
//         getQuizzes(allQuiz);
//     })

    return (
        <div style={{textAlign: "center"}}>
            <p>Uploaded quizzes</p>
            <h1>{Data.quiz_name}</h1>
            <p>{Data.description}</p>
        </div>
    )
}

export default Account
