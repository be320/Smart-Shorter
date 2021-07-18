import pymongo
from dotenv import dotenv_values

#.env file is private file containing the database name, password, and the collection name 
config = dotenv_values(".env")

#connecting to MLAB by pymongo client
cluster = pymongo.MongoClient("mongodb+srv://ahmedbahaa_98:"+config['PASS']+"@cluster0.goykf.mongodb.net/"+config['DATABASE']+"?retryWrites=true&w=majority")

#Selecting the cluster to use
db = cluster[config['DATABASE']]
#Selecting the collection to use
collection = db[config['COLLECTION']]

#getter function to use the database collection in our application
def getCollection():
    return collection

