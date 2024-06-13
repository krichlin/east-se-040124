from models import Project, User
from config import db, app

if __name__ == '__main__':
    with app.app_context():
        Project.query.delete()
        User.query.delete()
        projects = [
            {
            "name": "Great Outdoors Guide",
            "about": "Plan your next adventure to in the U.S. National Parks!",
            "phase": 4,
            "link": "https://great-outdoors-guide.netlify.app",
            "image": "https://i.imgur.com/8GnP2Uw.png"
            },
            {
            "name": "Book Her",
            "about": "The app takes you (the Casting Director) through a series of questions to determine the Models you need for your next Project.",
            "phase": 4,
            "link": "https://bookher.netlify.app/new_project",
            "image": "https://i.imgur.com/INs84Uk.png"
            },
            {
            "name": "Code Bucket",
            "about": "Web-based CSS, JS and HTML Editor",
            "phase": 4,
            "link": "https://code-bucket.netlify.app",
            "image": "https://i.imgur.com/Hz84TA2.png"
            },
            {
            "name": "Yourseum",
            "about": "Find great art",
            "phase": "4",
            "link": "https://yourseum.netlify.app",
            "image": "https://i.imgur.com/yywQCoi.png"
            },
            {
            "name": "YouTravel",
            "about": "YouTube for Travel Videos",
            "phase": "3",
            "link": "https://youtravel.netlify.app/",
            "image": "https://i.imgur.com/Y6mlORn.png"
            }
        ]

        project_objects = []

        for project in projects:
            p = Project(name=project['name'],\
                             about=project['about'],\
                             phase=project['phase'],\
                             link=project['link'],\
                             image=project['image']\
                            )
            project_objects.append(p)

        db.session.add_all(project_objects)
        db.session.commit()

        # u1 = User(username="emiley")
        # u2 = User(username="apollo")

        # db.session.add_all([u1, u2])
        # db.session.commit()