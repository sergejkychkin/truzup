from flask import Flask
from flask_restful import  Api



from truzup.Post import Post
from truzup.Posts import Posts
from truzup.DB import  engine,Base,Session
app = Flask(__name__)
api = Api(app)



api.add_resource(Posts,"/")
api.add_resource(Post,"/<post_id>")


if __name__ == '__main__':
    #Base.metadata.create_all(engine)

    app.run(debug=True)