from flask import Flask
from firebase import firebase
import json

app = Flask(__name__)

@app.route('/')

def index():
    url = "https://carrecorder-4b621.firebaseio.com"
    messenger = firebase.FirebaseApplication(url,None)
    # car = {'carnum':'7625','km':{'km1':'99999','km3':'888888'}}
    # result = messenger.put('/car','car8',car)
    result = messenger.get('/car','car8')
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

if __name__ == '__main__':
    app.run()
