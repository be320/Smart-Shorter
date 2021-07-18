import random
import string
from database import getCollection
from flask import jsonify
import json
from bson import json_util

#Generating random slug with length of 6 characters which is combination of ascii letters and digits
def generate_slug():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


#Adding new short link to the database
def post_short_link(request):
    #If the slug not inserted, we generate a random slug
    if 'slug' in request:
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

def parse_json(data):
    return json.loads(json_util.dumps(data))