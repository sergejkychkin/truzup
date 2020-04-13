from flask import Flask
from flask_restful import Resource,Api,reqparse,fields, marshal_with


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
resource_fields ={
    'data' : fields.List(fields.Nested(post_fields)),

}


class Posts(Resource):
    @marshal_with(resource_fields)
    def get(self):
        session = Session()
        data = session.query(Postdb).all()
        return {'data':data}


    @marshal_with(post_fields)
    def post(self):
        args = parser.parse_args()
        session = Session()
        post = Postdb(text=args['text'])
        session.add(post)
        session.commit()
        return post