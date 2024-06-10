from config import app, db
from models import Post, Comment, User

if __name__ == '__main__':
    with app.app_context():
        # delete all data
        Post.query.delete()
        User.query.delete()
        Comment.query.delete()
        db.session.commit()

        # create post instances
        p1 = Post(title="React is cool", body="We will start working with react tomorrow")
        p2 = Post(title="Flask-restful is cool", body="We will start working with Flask-restful tomorrow")
        p3 = Post(title="Serialization is cool", body="We will start working with Serialization today")

        # add to db
        db.session.add_all([p1, p2, p3])
        db.session.commit()

        u1 = User(name='Emiley')
        u2 = User(name='Conner')

        db.session.add_all([u1, u2])
        db.session.commit()

        c1 = Comment(content='cool', post_id=p1.id,user_id=u1.id)
        c2 = Comment(content='awesome', post_id=p1.id,user_id=u2.id)
        c3 = Comment(content='nice', post_id=p2.id,user_id=u1.id)
        c4 = Comment(content='spectacular', post_id=p1.id,user_id=u2.id)
        c5 = Comment(content='stellar', post_id=p3.id,user_id=u1.id)

        db.session.add_all([c1,c2,c3,c4,c5])
        db.session.commit()

