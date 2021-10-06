import React from 'react';

const AdminHome = ({handleLogout}) => {
    return (
        <div>
            <h1>Admin Home</h1>
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
}

export default AdminHome;