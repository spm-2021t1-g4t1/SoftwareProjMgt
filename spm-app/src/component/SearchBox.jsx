import React from 'react';

const SearchBox = (props) => {
    return (
        <div className="form-outline">
            <input type = 'search'
                    className = 'form-control'
                    placeholder = {props.placeholder}
                    onChange = {props.handleChange}
                    />
        </div>
        
    )
}

export default SearchBox;