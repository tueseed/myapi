from flask import Flask, request
from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# Fetch the service account key JSON file contents
cred = credentials.Certificate('carrecorder-4b621-firebase-adminsdk-zx0lv-99250f07ee.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://carrecorder-4b621.firebaseio.com/'
})
import json
app = Flask(__name__)

@app.route('/')
def index():
    ref = db.reference('car')
    return json.dumps(ref.get())

@app.route('/car_data', methods=['POST'])
def car_data():
    ref = db.reference('car')
    return json.dumps(ref.get())

@app.route('/add_car', methods=['POST'])

def add_car():
    json1 = json.dumps(request.form)
    json2 = json.loads(json1)
    url = "https://carrecorder-4b621.firebaseio.com"
    messenger = firebase.FirebaseApplication(url,None)
    result = messenger.post('/car',json2)
    return "INSERT DATA SUCCESS!!"


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == '__main__':
    app.run()
