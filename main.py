from flask import Flask,request,jsonify
from flask_cors import CORS, cross_origin
from controller import *

app = Flask(__name__)


#Post /shortLinks Route to create new shortlink
#Get /shortLinks Route to return List of All User’s Short Links return empty list if have no link
@app.route('/shortlinks', methods=['GET', 'POST'])
@cross_origin()
def short_links():
    if request.method == 'GET':
        return get_short_links()
    else:
        return post_short_link(request.json)

#PUT /shortlinks/<slug> TO Update Link Data
@app.route('/shortlinks/<slug>', methods=['PUT'])
@cross_origin()
def update_slug(slug):
    return update_short_link(slug, request.json)


@app.route('/', methods=['GET'])
@cross_origin()
def test():
    return {"test": "welcome to our server"}


# This section for handling different errors: 400, 404, 405, 500

@app.errorhandler(400)
def bad_request(e):
    print(e)
    response = {
        "status": "FAILED",
        "message": "BAD REQUEST"
    }
    return jsonify(response), 400

@app.errorhandler(404)
@app.errorhandler(405)
def page_not_found(e):
    print(e)
    response = {
        "status": "FAILED",
        "message": "NOT FOUND"
    }
    return jsonify(response), 404

@app.errorhandler(500)
def bad_request(e):
    print(e)
    return jsonify({}), 500
