from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

def success_response():
    resp = jsonify({
        "status": "success",
        "method": "GET",
        "message": "Hello from Flask"
    })
    resp.status_code = 200
    resp.headers["Server"] = "hypercorn-h11"
    return resp

def error_405_response():
    resp = jsonify({
        "status": "error",
        "message": "Method not allowed"
    })
    resp.status_code = 405
    resp.headers["Server"] = "hypercorn-h11"
    return resp

def error_404_response():
    resp = jsonify({
        "status": "error",
        "message": "Not found"
    })
    resp.status_code = 404
    resp.headers["Server"] = "hypercorn-h11"
    return resp

@app.before_request
def global_guard():
    if request.path != "/":
        return error_404_response()
    elif request.method != "GET":
        return error_405_response()

@app.route("/", methods=["GET"])
def home():
    return success_response()
