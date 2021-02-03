# mongo.py
from flask import request, url_for, Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://db:27017/restdb'

mongo = PyMongo(app)

# Insert Images in mongoDB

@app.route('/create', methods=['POST'])
def create():
  if 'profile_image' in request.files:
    profile_image = request.files['profile_image']
    mongo.save_file(profile_image.filename, profile_image)
    mongo.db.users.insert({'username': request.get('username'), 'profile_image_name': profile_image.filename})
  return 'Done'

# Endpoint to retrieve data from mongoDB

@app.route('/file/<filename>')
def file(filename):
  return mongo.send_file(filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True))