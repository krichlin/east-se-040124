from flask import request, make_response, session
from config import app, db, api
from models import Project, User
from flask_restful import Resource

import ipdb

class Projects(Resource):
    def get(self):
        projects = Project.query.all()
        projects_list = [project.to_dict() for project in projects]
        return make_response(projects_list)

    def post(self):
        data = request.json
        try:
            project = Project(name=data['name'],\
                             about=data['about'],\
                             phase=data['phase'],\
                             link=data['link'],\
                             image=data['image']\
                            )
            db.session.add(project)
            db.session.commit()
            return make_response(project.to_dict(), 201)
        except:
            return make_response({'error': "couldn't create project"}, 400)


api.add_resource(Projects, '/projects')

class ProjectById(Resource):
    def get(self, id):
        project = Project.query.get(id)
        return make_response(project.to_dict())

api.add_resource(ProjectById, '/projects/<int:id>')


# 3a. define /signup route

# 3c. add user_id to session
    # check cookies on frontend

# 4a. create /check_session route
    # b. request from frontend
    # c. check for user_id in session
    # d. if user_id, find user send back response
    # e. else send back error response

# 5. create /logout route
    #  remove user_id from session

# 6a. create /login route

# 6c. add user_id to session