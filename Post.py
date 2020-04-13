from flask import Flask
from flask_restful import Resource,Api,reqparse,fields,marshal_with




from truzup.DB import  Post as Postdb
from truzup.DB import Session



parser = reqparse.RequestParser()
parser.add_argument("text",type=str)
parser.add_argument("id",type=int)

post_fields = {
    'id' : fields.Integer,
    'text' : fields.String,
    'date' : fields.DateTime,
}


class Post(Resource):


    @marshal_with(post_fields)
    def get(self,post_id):
        args = parser.parse_args()
        session = Session()

        post = session.query(Postdb).filter_by(id=post_id).first()
        return post


    def post(self,post_id):
        pass


    def delete(self,post_id):
        pass

    def put(self,post_id):
        args = parser.parse_args()
        session = Session()
        session.query(Postdb).filter_by(id=post_id).update({'text':args['text']})




