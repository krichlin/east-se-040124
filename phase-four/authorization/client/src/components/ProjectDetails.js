import { useEffect, useState } from "react"
import { useParams } from "react-router-dom"

function ProjectDetails() {
    const { id } = useParams()
    const [project, setProject] = useState(null)

    useEffect(() => {
        fetch(`/projects/${id}`)
        .then((resp) => resp.json())
        .then((data) => setProject(data))
        .catch((error) => console.log(error))
    }, [])

    if (!project) return <p>Loading....</p>

    return (
        <div className="card">
            <h2>{project.name}</h2>
            <p>{project.about}</p>
            <figure className="image">
                <img src={project.image} alt={project.name}/>
            </figure>
        </div>
    )
}

export default ProjectDetails