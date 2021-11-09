import React, { useState, useEffect } from 'react'
import { Container, Button } from 'react-bootstrap'
import { useParams } from "react-router-dom"


import SectionContainer from '../../component/SectionContainer'



const Section = () => {
    const courseid = useParams().courseid
    const classno = useParams().classno
    const staffusername = 'darrelwilde'


    //useState
    const [sectionArrs, setSectionArrs] = useState([])
    const [noCompleted, setNoCompleted] = useState(0)
    const [stateChange, setStateChange] = useState(0)
    const [boolFinals, setboolFinals] = useState(false)
    const [noAttempted, setNoAttempted] = useState(false)

    function classChange() {
        setStateChange(stateChange+1)
    }

    // pull api only once
    useEffect(() => {
        fetch(`http://127.0.0.1:5000/lesson/${courseid}/${classno}/${staffusername}`)
            .then(res => res.json())
            .then(
                (result) => {
                    // console.log(result.data)
                    setSectionArrs(result.data)
                    // console.log(sectionArrs)
                }
            )

        fetch(`http://127.0.0.1:5000/lesson_completion/${courseid}/${classno}/${staffusername}`)
            .then(res => res.json())
            .then(
                (result) => {
                    // console.log(result.data.length)
                    setNoCompleted((result.data).length)
                }
            )
        fetch(`http://127.0.0.1:5000/eligibility/final_quiz/${courseid}/${classno}/${staffusername}`)
            .then(res => res.json())
            .then(
                (result) => {
                    setboolFinals(result.eligiblity)
                }
            )
    }, [stateChange])

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/exam//${courseid}/${classno}/${staffusername}`)
        .then(res => res.json())
        .then(
            (result) => {
                console.log(result)
                setNoAttempted(result.data)
            }
        )
    },[boolFinals])


    return (
        <div className = 'col col-lg-9 col-md-8'>
            {sectionArrs.map((sectionArr,index) =>
                <SectionContainer key= {index} 
                                    data = {sectionArr} completedLesson = {noCompleted} number = {index+1}
                                    classChange = {classChange}/>
            )}
            {boolFinals
            ?<Container>
                <div className="text-center border border-info container-fluid container-bg">
                    <h2>Final Exam</h2>
                    <hr />
                    <Container className='d-flex justify-content-between container-md flex-wrap my-2' >
                        {noAttempted
                        ?<h4>Score: {noAttempted.quiz_score}/100</h4>
                        :<h4 className = "text-danger">Not Attempted</h4>
                        }
                        <Button>Take Exam</Button>
                        
                    </Container>
                </div>
            </Container>
            :""
            }
    
        </div>
    )
}

export default Section
