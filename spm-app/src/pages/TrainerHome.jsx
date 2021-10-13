import React from 'react';

const TrainerHome = ({handleLogout}) => {
    return (
        <div>
            <h1>Trainer Home</h1>
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
}

export default TrainerHome;