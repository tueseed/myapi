from flask import Flask
# from firebase import firebase

app = Flask(__name__)

@app.route('/')

def index():
    # url = "https://carrecorder-4b621.firebaseio.com"
    # messenger = firebase.FirebaseApplication(url,None)
    # car = {'carnum':'7625','km':{'km1':'99999','km3':'888888'}}
    # result = messenger.put('/car','car8',car)
    # result = messenger.get('/car','car8')
    return "testpage"

if __name__ == '__main__':
    app.run()
