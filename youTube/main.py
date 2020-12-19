from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application and wrap it around API
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///dabase.db'
db = SQLAlchemy(app)


# primary_key is True when its value is going to be different for every class object
# nullable requires the variable to have a value
class VideoModel1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    print("{vi")

    def __repr__(self):
        return f"Videos(name = {self.name}, views = {self.views}, likes = {self.likes}) "


db.create_all()

# Specify arguments that are required to create a video object
# video_put_args automatically parse the request and make sure that the information fits the guideline we define
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("view", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video is required", required=True)
# Help is for error handling. See notes to learn what parsing means.

# data for HelloWorld Class
names = {"Dylan": {"age": 19, "gender": "male"},
         "bill": {"age": 70, "gender": "male"}}

# data for Video Class
videos = {}


# This function is called when user tries to get a video that is not in the videos dictionary
def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Could not find video...")

def abort_if_video_exist(video_id):
    if video_id in videos:
        abort(409, message="video already exists with the given id")


# Create a Video class that inherits from Resource. Function is used for creating a video object and getting its information.
class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if_video_exist(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
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
