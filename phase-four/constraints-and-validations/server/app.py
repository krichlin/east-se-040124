from flask import make_response, request
from flask_restful import Resource

from config import app, db, api
from models import Post        

class Posts(Resource):
    def get(self):
        all_posts = []
        for post in Post.query.all():
            all_posts.append(post.to_dict(rules=('-comments',)))

        return make_response(all_posts)

    def post(self):
        data = request.json
        new_post = Post(title=data['title'], body=data['body'])

        db.session.add(new_post)
        db.session.commit()

        return make_response(new_post.to_dict(), 201)
        
api.add_resource(Posts, '/posts')

class PostById(Resource):
    def get(self, id):
        # post = Post.query.get(id)
        # post = db.get_or_404(Post, id, description="post not found")
        post = db.session.get(Post, id)

        if post:
            return make_response(post.to_dict())

    def patch(self, id):
        post = db.session.get(Post, id)
        if post:
            params = request.json
            for attr in params:
                setattr(post, attr, params[attr])
            db.session.commit()
            return make_response(post.to_dict())    

    def delete(self, id):
        post = db.session.get(Post, id)
        if post:
            db.session.delete(post)
            db.session.commit()
            return make_response({'message': "successfully deleted post"})

api.add_resource(PostById, '/posts/<int:id>')