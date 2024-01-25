from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

# names = {
#     "dio": {"age": 23, "gender": "male"},
#     "bill": {"age": 70, "gender": "male"}}



video_put_args = reqparse.RequestParser() # parse the request automatically
video_put_args.add_argument("name", type=str, help="Name of the video is required", required= True)
video_put_args.add_argument("views", type=int, help="Views of the video", required= True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required= True)

videos = {}

def abort_id(video_id):
    if video_id not in videos:
        abort(404, message = "Video id is not valid...")

class Video(Resource):
    def get(self, video_id):
        abort_id(video_id)
        return videos[video_id]

    # def post(self):
    #     return{"data":"Posted"}

    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return {video_id: args}, 201
        

#api.add_resource(HelloWorld, "/helloworld/<string:name>")
api.add_resource(Video, "/video/<int:video_id>")


if __name__ == "__main__":
    app.run(debug=True)
