import React, { useState, createContext, useContext } from 'react'
import { BrowserRouter, Route, useHistory, Redirect } from "react-router-dom"
import LearnerHome from './pages/EngineerView/LearnerHome';
import Login from './pages/Login';
import AdminHome from './pages/Administrator View/AdminHome';
import TrainerHome from './pages/EngineerView/TrainerHome';

import './App.css';

const userContext = createContext({
  user: {
    current_designation: undefined,
    department: undefined,
    role: undefined,
    staff_email: undefined,
    staff_name: undefined
  },
  setUser: (user) => { }
});

const App = () => {
  const history = useHistory();
  // TODO: set username into context once logged in so child components can access it
  const [user, setUser] = useState(JSON.parse(localStorage.getItem('user')));
  console.log(user)

  return (
    <BrowserRouter>
      <Route path='/login'>
        <Login setUser={setUser} />
      </Route>
      <Route path='/' >
        <LoginWrapper user={user} setUser={setUser}/>
      </Route>
    </BrowserRouter>
  );
}

export default App;


const LoginWrapper = ({ user, setUser }) => {
  const handleLogout = () => {
      localStorage.removeItem('user');
      setUser(undefined);
    }

  if (!user) {
    return (<Redirect to='/login' />);
  }
  if (user.role === 'Administrator') {
    return (<AdminHome handleLogout={handleLogout} />);
  }
  if (user.role === 'Learner' || user.role === 'Trainer') {
    return (<LearnerHome handleLogout={handleLogout} />);
  }
  // if (user.role === 'Trainer') {
  //   return (<TrainerHome handleLogout={handleLogout} />);
  // }
  return(<h1>Something has gone wrong and the user is undefined. Run localStorage.clear() in the console to reset.</h1>);
}