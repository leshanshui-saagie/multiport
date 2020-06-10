from flask import Flask, jsonify, request
application = Flask(__name__)
 
@application.route("/")
def hello():
    return jsonify({'response': "Hello World!"}), 201
 
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8079)
