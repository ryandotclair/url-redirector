import os
from flask import Flask,redirect

# Initiate Flask
app = Flask(__name__)

# Get URL from env var
URL=os.environ['URL']

@app.route('/')
def notHere():
    return redirect("URL")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
