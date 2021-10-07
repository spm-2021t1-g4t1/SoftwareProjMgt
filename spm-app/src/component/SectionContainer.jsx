import React, { useState } from 'react'

const SectionContainer = (props) => {
    console.log(props.data)
    
    let sectionArr = props.data
    // eslint-disable-next-line
    const[sectionArrs, setSectionArrs] = useState(props.data)

    const sectionNumber = props.number

    console.log(props.data.lesson_materials)
    
    
    return (
        <div className = 'sectionCon'>
            <div className =' sectionCon-Top'>
                <h1>{ sectionNumber } {sectionArrs['lesson_name']}</h1>
            </div>
            <div className = 'sectionCon-Content'>
                <div className = 'sectionCon-Description'>
                    <h2>Description</h2>
                    <p>
                        {sectionArrs['lesson_description']}
                    </p>
                </div>
                <div className = 'sectionCon-Material'>
                    <h2>Course Material</h2>
                    <ul>
                        {sectionArrs['lesson_materials'].map((mat, index) =>
                            <li key={mat['lesson_no']-mat['course_material_title']}>
                                <a href = {mat['link']}>{mat['course_material_title']}</a>
                            </li>                        
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
