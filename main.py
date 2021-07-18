from flask import Flask,request,jsonify
from flask_cors import CORS, cross_origin
from controller import *

app = Flask(__name__)


@app.route('/shortlinks', methods=['GET', 'POST'])
@cross_origin()
def short_links():
    if request.method == 'POST':
        return get_short_links()
    else:
        return post_short_link(request.json)


@app.route('/shortlinks/<slug>', methods=['PUT'])
@cross_origin()
def update_slug(slug):
    return update_short_link(slug, request.json)


@app.errorhandler(400)
def bad_request(e):
    response = {
        "status": "FAILED",
        "message": "BAD REQUEST"
    }
    return jsonify(response), 400

@app.errorhandler(404)
@app.errorhandler(405)
def page_not_found(e):
    response = {
        "status": "FAILED",
        "message": "NOT FOUND"
    }
    return jsonify(response), 404

@app.errorhandler(500)
def bad_request(e):
    return jsonify({}), 500
