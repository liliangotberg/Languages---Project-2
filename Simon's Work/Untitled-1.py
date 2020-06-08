from flask import Flask, jsonify
import json
app = Flask(__name__)

@app.route("/")
def index():
  with open('csvjson.json') as json_file:
   
    data = json.load(json_file)
    print(data)

if __name__ == '__main__':
    app.run(debug=True)