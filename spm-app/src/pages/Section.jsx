import React, { useState, useEffect } from 'react'
import { useParams } from "react-router-dom"


import SectionContainer from '../component/SectionContainer'



const Section = () => {
    const courseid = useParams().courseid
    const classno = useParams().classno
    const staffusername = 'darrelwilde'


    //useState
    const[sectionArrs, setSectionArrs] = useState([])
    const[noCompleted, setNoCompleted] = useState(0)
    const [stateChange, setStateChange] = useState(0)

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

        fetch(`http://127.0.0.1:5000//lesson_completion/${courseid}/${classno}/${staffusername}`)
            .then(res => res.json())
            .then(
                (result) => {
                    // console.log(result.data.length)
                    setNoCompleted((result.data).length)
                }
            )
    }, [stateChange])


    return (
        <div className = 'col col-lg-9 col-md-8'>
            {sectionArrs.map((sectionArr,index) =>
                <SectionContainer key= {index} 
                                    data = {sectionArr} completedLesson = {noCompleted} number = {index+1}
                                    classChange = {classChange}/>
            )}
        </div>
    )
}

export default Section
