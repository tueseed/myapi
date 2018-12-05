from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    print ("นี่คือหน้าหลัก")

if __name__ == '__main__':
    app.run()
