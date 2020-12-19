from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application and wrap it around API
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dabase.db'
db = SQLAlchemy(app)


# primary_key is True when its value is going to be different for every class object
# nullable requires the variable to have a value
class VideoModel1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    view = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __init__(self, id, name, view, likes):
        self.id = id
        self.name = name
        self.view = view
        self.likes = likes

    def __repr__(self):
        return f"Videos(name = {self.name}, view = {self.view}, likes = {self.likes}) "





# Specify arguments that are required to create a video object
# video_put_args automatically parse the request and make sure that the information fits the guideline we define
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("view", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video is required", required=True)
# Help is for error handling. See notes to learn what parsing means.

resource_fields = {
    'id': fields.String,
    'name': fields.String,
    'view': fields.Integer,
    'likes': fields.Integer
}


# data for HelloWorld Class
names = {"Dylan": {"age": 19, "gender": "male"},
         "bill": {"age": 70, "gender": "male"}}

# data for Video Class
videos = {}


# Create a Video class that inherits from Resource. Function is used for creating a video object and getting its information.
class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel1.query.get(id=video_id)
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        #args = video_put_args.parse_args()
        #video = VideoModel1(id=video_id, name=args['name'], view=args['view'], likes=args['likes'])
        args = video_put_args.parse_args()
        video = VideoModel1(1, "Swings", 999, 10)
        db.session.add(video)
        db.session.commit()
        return video, 201


    def delete(self, video_id):
        del videos[video_id]
        return "", 204





# Function for practice
class HelloWorld(Resource):
    def get(self, name):
        return names[name]

    def post(self, name):
        return {"data": "Posted!"}


# This creates api
api.add_resource(Video, "/video/<int:video_id>")
api.add_resource(HelloWorld, "/helloworld/<string:name>")  # it is going to be accessble through /helloworld
# I want the user to pass in some kind of string data


# this is going to start the server and flask app. (debug for testing purpose)
if __name__ == "__main__":
    app.run(debug=True)
