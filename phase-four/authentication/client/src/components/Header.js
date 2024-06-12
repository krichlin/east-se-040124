import { NavLink } from "react-router-dom";

function Header({ darkMode, onDarkModeToggle, logoutUser }) {
    const handleModeClick = () => onDarkModeToggle()
    const buttonText = darkMode ? "Light Mode" : "Dark Mode"

    function handleLogout() {
        fetch('/logout', {
            method: 'DELETE'
        }).then( resp => {
            if (resp.ok) {
                // update the state of the user back to a falsey value
                logoutUser()
            }
        })
    }

    return (
        <header>
            <h1>
                <span className="logo">{"//"}</span>
                Project Showcase
            </h1>
            <nav>
                <NavLink to="/projects">Projects</NavLink>
                <NavLink to="/projects/new">New Project</NavLink>
            </nav>
            <button onClick={handleLogout}>Logout</button>
            <button onClick={handleModeClick}>{ buttonText }</button>
        </header>
    )
}

export default Header;