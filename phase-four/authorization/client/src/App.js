import { useState, useEffect } from "react"
import { Outlet } from "react-router-dom"

import Header from "./components/Header"
import Auth from "./components/Auth"

function App() {
  const [ darkMode, setDarkMode ] = useState(true)
  const [ loggedInUser, setLoggedInUser ] = useState(null)

  function onDarkModeToggle() {
    setDarkMode(!darkMode)
  }

  function logoutUser() {
    setLoggedInUser(null)
  }

  useEffect(() => {
    fetch('/check_session')
      .then((resp) => {
        if (resp.ok) {
          resp.json().then(user => setLoggedInUser(user))
        }
      })
  }, [])

  const className = darkMode ? 'App' : 'App light'

  return <div className={className}>
    <Header darkMode={darkMode} onDarkModeToggle={onDarkModeToggle} logoutUser={logoutUser}/> 
    {
      !!loggedInUser ?
      <Outlet /> :
      <Auth setUser={setLoggedInUser} />
    }
  </div>;
}

export default App;
