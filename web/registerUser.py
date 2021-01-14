from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient

app = Flask (__name__)
api = Api(app)

try:
    client = MongoClient("mongodb://db:27017")
    print("Connected to database successfully !!")
except:
    print("Could not connect to MongoDb")

# Create or use existing database UserProfile
db = client.UserData

# Create a collection or Switch to existing collection:
collection = db.UserProfile
# Insert data in database
@app.route("/userdata", methods=['POST'])
def insert_data():
    postedData = request.get_json(force=True)
    collection.insert_one(postedData).inserted_id
    return ('', 204)

# Get data from database
@app.route('/getdata')
def get():
    documents = collection.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return jsonify(response)

if __name__=="__main__":
    app.run(host='0.0.0.0')