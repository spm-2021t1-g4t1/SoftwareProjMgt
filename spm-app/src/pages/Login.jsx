import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import axios from "axios";

const Login = ({setUser}) => {
    const history = useHistory();
    const [username, setUsername] = useState("darrelwilde");
    const [errMsg, setErrMsg] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!username) return;
        
        try {
            const endpoint = "http://127.0.0.1:5000/"
            
        // validate username
        axios.get(endpoint + `login/${username}`)
            .then((response) => {
                if (response.data.data) {
                    localStorage.setItem('user', JSON.stringify(response.data.data));
                    setUser(response.data.data)
                    setErrMsg("");
                    history.push(response.data.data.role);
                }
                else {  
                    setErrMsg("Invalid username");
                }
            })
        } catch (error) {
            console.log(error.message)
        }
    }

    // If user is already logged in, redirect away from login page.
    const user = JSON.parse(localStorage.getItem('user'));
    if (user) history.push(user.role);

    return (
        <div>
            <form>
                <h1>Login</h1>
                Enter your username:
                <input type="text" onInput={(e) => setUsername(e.target.value)} value={username}></input>
                <button onClick={handleSubmit}>Login</button>
                {errMsg}
            </form>
            <h2>Dev reference</h2>
            <p>Admin account: hananhyde</p>
            <p>Learner account: darrelwilde</p>
            <p>Trainer account: jackma</p>
        </div>
    );
}

export default Login;