import os
from flask import Flask,redirect

# Initiate Flask
app = Flask(__name__)

# Get URL from env var
URLREDIRECT=os.environ['URLREDIRECT']

@app.route('/')
def notHere():
    return redirect("URLREDIRECT")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=443)
