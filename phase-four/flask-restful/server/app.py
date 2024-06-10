from flask import make_response, request

from config import app, db
from models import Post

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'GET':
        all_posts = []
        for post in Post.query.all():
            all_posts.append(post.to_dict(rules=('-comments',)))

        return make_response(all_posts)
    elif request.method == 'POST':
        data = request.json

        new_post = Post(title=data['title'], body=data['body'])

        db.session.add(new_post)
        db.session.commit()

        return make_response(new_post.to_dict(), 201)