import { Link } from "react-router-dom"

function ProjectListItem({ project }) {
    const { name, image, id } = project
    return (
        <li className="card">
            <figure className="image">
                <img src={image} alt={`project: ${name}`}/>
            </figure>
            <article>
                <h4>{name}</h4>
                <Link to={`/projects/${id}`}>See Details</Link>
            </article>
        </li>
    )
}

export default ProjectListItem