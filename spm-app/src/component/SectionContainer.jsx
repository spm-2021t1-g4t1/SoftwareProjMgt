import React, { useState } from 'react'

const SectionContainer = (props) => {
    // console.log(props)
    
    let sectionArr = props.data;
    // eslint-disable-next-line
    const[sectionArrs, setSectionArrs] = useState({
        section_name: sectionArr.section_name,
        section_description: sectionArr.section_description,
        course_material: sectionArr.course_material})

    const sectionNumber = props.number

    // console.log(sectionArrs)

    
    return (
        <div className = 'sectionCon'>
            <div className =' sectionCon-Top'>
                <h1>{ sectionNumber } {sectionArrs['section_name']}</h1>
            </div>
            <div className = 'sectionCon-Content'>
                <div className = 'sectionCon-Description'>
                    <h2>Description</h2>
                    <p>
                        {sectionArrs['section_description']}
                    </p>
                </div>
                <div className = 'sectionCon-Material'>
                    <h2>Course Material</h2>
                    <ul>
                        {sectionArrs['course_material'].map((mat, index) =>
                            <li key={index}>{mat}</li>                        
                        )}
                    </ul>

                    <div className = 'sectionCon-Quiz'>
                        <button>Take Quiz</button>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default SectionContainer
