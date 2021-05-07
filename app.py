from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/')
def index():
    return "mkl;mkspvddf"

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
