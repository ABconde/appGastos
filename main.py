from flask import Flask, redirect, request, Response

import connection
import json
from services import userService, accountService, expenseService
from models.user import User

app = Flask(__name__)

# @app.before_first_request
# def initDB():
#     connection.get_users()

@app.route("/")
def init():
    data = { 'Message': 'Pagina de inicio del API' }
    return format_response({ "message": data, "code": 200 })

# -------- Users --------
@app.route("/users/all", methods=['GET'])
def get_all_users():
    return format_response(userService.get_all())

@app.route("/user/<id>", methods=['GET'])
def get_user_by_id(id):
    return format_response(userService.get(id))

@app.route("/user/login", methods=['PATCH'])
def get_user_login():
    obj = request.get_json()
    return format_response(userService.login(obj))

@app.route("/user", methods=['POST'])
def create_user():
    obj = request.get_json()
    return format_response( userService.create(obj) )

@app.route("/user/<id>", methods=['PUT'])
def update_user(id):
    obj = request.get_json()
    return format_response(userService.update(id,obj))

@app.route("/user/pass/<id>", methods=['PUT'])
def update_user_pass(id):
    obj = request.get_json()
    return format_response(userService.change_password(id, obj))

# -------- Accounts --------
@app.route("/account/user/<user>", methods=['GET'])
def get_account_by_user(user):
    return format_response(accountService.get_by_user(user))

@app.route("/account/<id>", methods=['GET'])
def get_account(id):
    return format_response(accountService.get(id))

@app.route("/account", methods=['POST'])
def create_account():
    obj = request.get_json()
    return format_response( accountService.create(obj) )

@app.route("/account/<id>", methods=['PUT'])
def update_account(id):
    obj = request.get_json()
    return format_response(accountService.update(id,obj))

@app.route("/account/<id>", methods=['DELETE'])
def delete_account(id):
    return format_response(accountService.delete(id))

# -------- Expenses  --------

@app.route("/expense/account/<account>", methods=['GET'])
def get_expenses_by_account(account):
    return format_response(expenseService.get_all_by_account(account))

@app.route("/expense/account/<account>", methods=['PATCH'])
def get_expenses_by_account_and_date_range(account):
    obj = request.get_json()
    return format_response(expenseService.get_by_acount_and_date_range(account, obj))

@app.route("/expense/", methods=['POST'])
def create_expense():
    obj = request.get_json()
    return format_response( expenseService.create(obj) )

@app.route("/expense/<id>", methods=['PUT'])
def update_expnse(id):
    obj = request.get_json()
    return format_response(expenseService.update(id, obj))

@app.route("/expense/<id>", methods=['DELETE'])
def delete_expense(id):
    return format_response(expenseService.delete(id))

# -------- Functions --------

def format_response(request):
    # { "message": { 'Error': "En desarrollo"}, "code": 404 }
    return Response(json.dumps(request["message"]), status=request["code"], mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True, port=8081)