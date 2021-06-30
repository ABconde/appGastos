from flask import Flask, redirect, request, Response

import connection
import json
from services import userService, accountService
from models.user import User

app = Flask(__name__)

# @app.before_first_request
# def initDB():
#     connection.get_users()

@app.route("/")
def init():
    data = { 'Message': 'Pagina de inicio del API' }
    data_u = User(id='1')
    return format_response({ "message": data_u.__dict__, "code": 200 })

# -------- Users --------

@app.route("/users/all", methods=['GET'])
def get_all_users():
    return format_response(userService.get_all())

@app.route("/user/<id>", methods=['GET'])
def get_user_by_id(id):
    return format_response(userService.get(id))

@app.route("/user/<email>/<pw>", methods=['GET'])
def get_user(email, pw):
    return format_response(userService.login(em = email, pw = pw))

@app.route("/user", methods=['POST'])
def create_user():
    obj = request.get_json()
    return format_response( userService.create(obj) )

# -------- Accounts --------
@app.route("/account/<user>", methods=['GET'])
def get_account_by_user(user):
    return format_response(accountService.get_by_user(user))

@app.route("/account", methods=['POST'])
def create_account():
    obj = request.get_json()
    return format_response( accountService.create(obj) )

# -------- Functions --------

def format_response(request):
    # { "message": { 'Error': "En desarrollo"}, "code": 404 }
    return Response(json.dumps(request["message"]), status=request["code"], mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True, port=8081)