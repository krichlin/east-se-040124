import { useState, useEffect } from "react"
import { Outlet } from "react-router-dom"

function ProjectContainer() {
    const [ projects, setProjects ] = useState([])

    useEffect(() => {
        fetch('/projects')
        .then((resp) => resp.json())
        .then((data) => setProjects(data))
    }, [])

    function onAddProject(newProject) {
        setProjects((currentProjects) => {
            return [...currentProjects, newProject]
        })
    }

    const context = {
        projects: projects,
        onAddProject: onAddProject
    }

    return (
        <div>
            <Outlet context={context} />
        </div>
    )
}

export default ProjectContainer