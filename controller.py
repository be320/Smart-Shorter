import random
import string
from database import getCollection
from flask import jsonify

def generate_slug():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def post_short_link(request):
    if 'slug' in request:
        slug = request['slug']
    else:
        slug = generate_slug()
    
    db_collection = getCollection()

    new_short_link = {
        "slug": slug,
        "web": request['web'],
        "android": {
            "primary": request['android']['primary'],
            "fallback": request['android']['fallback'],
            },
        "ios": {
            "primary": request['ios']['primary'],
            "fallback": request['ios']['fallback'],
            },
    }

    db_collection.insert_one(new_short_link)

    response = {
        "status": "successful",
        "slug": slug,
        "message": "created successfully"
    }
    return jsonify(response), 201