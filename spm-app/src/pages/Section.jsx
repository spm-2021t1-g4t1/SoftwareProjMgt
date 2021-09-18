import React, { useState, useEffect } from 'react'

import SectionContainer from '../component/SectionContainer'



const Section = (prop) => {

    // console.log(prop.data)

    //useState
    const[sectionArrs, setSectionArrs] = useState([])


    // pull api only once
    useEffect(() => {
        fetch('/jsonfiles/sectiondata.json')
        .then(res => res.json()) 
        .then (
            (result) => {
                let section_Array = result.data.section_schema_section
                let section_list = []
                for ( let i of section_Array) {
                    if (i.course_code === prop.data) {              
                        section_list.push(i)
                    }
                }
                setSectionArrs(section_list)
                // console.log(section_list)
            }
        )
    }, [prop.data])

    return (
        <div className = 'leftSection'>
            {sectionArrs.map((sectionArr,index) =>
                <SectionContainer key= {index } data = {sectionArr} number = {index+1}/>
            )}
        </div>
    )
}

export default Section
