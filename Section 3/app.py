from flask import Flask

app = Flask(__name__) # __name__ to create files with unique names

@app.route('/') # 'http://google.com/'

def home():
    return "Hello, world"

app.run(port=5000)