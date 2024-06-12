import { createBrowserRouter } from "react-router-dom";

import App from "./App";
import About from "./components/About"
import ProjectContainer from "./components/ProjectContainer";
import ProjectsList from "./components/ProjectsList";
import ProjectForm from "./components/ProjectForm"
import ProjectDetails from "./components/ProjectDetails";

const routes = [
    {
      path: '/',
      element: <App />,
      children: [
        { index: true, element: <About /> },
        {
          path: 'projects',
          element: <ProjectContainer />,
          children: [
            { index: true, element: <ProjectsList /> },
            {
              path: 'new',
              element: <ProjectForm />
            }
          ]
        },
        {
          path: 'projects/:id',
          element: <ProjectDetails />
        }
      ]
    },
    {
      path: '/about',
      element: <About />
    }
]
  
export const router = createBrowserRouter(routes)