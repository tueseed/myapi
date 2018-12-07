from flask import Flask, request
from firebase import firebase
import json
app = Flask(__name__)

@app.route('/')
def index():
    url = "https://carrecorder-4b621.firebaseio.com"
    messenger = firebase.FirebaseApplication(url,None)
    # car = {'carnum':'7625','km':{'km1':'99999','km3':'888888'}}
    # result = messenger.put('/car','car8',car)
    result = messenger.get('/car','car16')
    result1 = json.dumps(result)
    y = json.loads(result1)
    return y["carnum"]

@app.route('/car_data', methods=['POST'])
def car_data():
    url = "https://carrecorder-4b621.firebaseio.com"
    messenger = firebase.FirebaseApplication(url,None)
    result = messenger.get('/car',None)
    result1 = json.dumps(result)
    # y = json.loads(result1)
    return result1

@app.route('/add_car', methods=['POST'])

def add_car():
    json1 = json.dumps(request.form)
    # url = "https://carrecorder-4b621.firebaseio.com"
    # messenger = firebase.FirebaseApplication(url,None)
    # result = messenger.post('/car',json1)
    # return result
    return type(json1)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == '__main__':
    app.run()
