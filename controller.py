import random
import string
from database import getCollection
from flask import jsonify, abort
import json
from bson import json_util

#Generating random slug with length of 6 characters which is combination of ascii letters and digits
def generate_slug():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


#Adding new short link to the database
def post_short_link(request):
    #If the slug not inserted, we generate a random slug
    if request['slug'] != '':
        slug = request['slug']
    else:
        slug = generate_slug()
    
    #Making insatnce of our database collection to insert the short link as object in the DB
    db_collection = getCollection()
    new_short_link = {
        "slug": slug,
        "web": request['web'],
        "android": {
            "primary": request['android']['primary'],
            "fallback": request['android']['fallback']
            },
        "ios": {
            "primary": request['ios']['primary'],
            "fallback": request['ios']['fallback']
            }
    }
    db_collection.insert_one(new_short_link)

    #Responding with success message
    response = {
        "status": "successful",
        "slug": slug,
        "message": "created successfully"
    }
    return jsonify(response), 201


#Adding new short link to the database
def get_short_links():
    #Making insatnce of our database collection to get all the short links
    db_collection = getCollection()
    links = list(db_collection.find({}))
    #Responding with success message
    response = {
        "status": "successful",
        "links": parse_json(links),
        "message": "fetched links successfully"
    }
    return jsonify(response), 201


#Updates shortlink according to passed params
def update_short_link(slug, request):
    #Making insatnce of our database collection to get update short link by slug
    db_collection = getCollection()
    link = list(db_collection.find({"slug":slug}))[0]
    if link is None:
        abort(404)

    #Change the object attributes passed
    if 'web' in request:
        link['web'] = request['web']
    if 'android' in request:
        if 'primary' in request['android']:
            link['android']['primary'] = request['android']['primary']
        if 'fallback' in request['android']:
            link['android']['fallback'] = request['android']['fallback']
    if 'ios' in request:
        if 'primary' in request['ios']:
            link['ios']['primary'] = request['ios']['primary']
        if 'fallback' in request['ios']:
            link['ios']['fallback'] = request['ios']['fallback']

    db_collection.update_one({"slug":slug}, {"$set": link})

    response = {
        "status": "successful",
        "message": "updated successfully"
    }
    return jsonify(response), 201

#parsing the objects returned from MongoDB
def parse_json(data):
    return json.loads(json_util.dumps(data))