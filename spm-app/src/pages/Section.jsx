import React, { useState, useEffect } from 'react'

import SectionContainer from '../component/SectionContainer'



const Section = (prop) => {

    // console.log(prop.data.classes[0].lesson)

    //useState
    const[sectionArrs, setSectionArrs] = useState([])

   
    // pull api only once
    
    useEffect(() => {
        setSectionArrs(prop.data.classes[0].lesson)
        // console.log(sectionArrs)
    },[])

    return (
        <div className = 'col col-lg-9 col-md-8'>
            {sectionArrs.map((sectionArr,index) =>
                <SectionContainer key= {index } data = {sectionArr} number = {index+1}/>
            )}
        </div>
    )
}

export default Section
