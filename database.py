import pymongo
from dotenv import dotenv_values

config = dotenv_values(".env")

cluster = pymongo.MongoClient("mongodb+srv://ahmedbahaa_98:"+config['PASS']+"@cluster0.goykf.mongodb.net/"+config['DATABASE']+"?retryWrites=true&w=majority")
db = cluster[config['DATABASE']]
collection = db[config['COLLECTION']]

def getCollection():
    return collection

