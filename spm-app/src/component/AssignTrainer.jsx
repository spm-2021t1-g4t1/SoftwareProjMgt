import React from 'react';
import { Link } from "react-router-dom";
import axios from "axios";
import { useState, useEffect } from 'react';
import "../App.css";
import SearchBox from './SearchBox';


// classcard

const AssignTrainer = (prop) => {
    // course_id, class_no
    const course_id = prop.course_id;
    const class_no = prop.class_no;

    function assign() {
        // set trainer_name to trainer name (if not null)
        const endpoint = 'http://127.0.0.1:5000/classes'
        const data = {}


        // const [stateChange, setStateChange] = useState(false)
        // const [inQueue, setInQueue] = useState([])

        // function classChange() {
        //     setStateChange(true)
        // }

    }

    useEffect(() => {
        const endpoint = 'wtf? sad code'
    })

    return(
        <h1>sad</h1>
    )
}

export default AssignTrainer;

// click on btn
// trainer list
// assign
// update db