import connection
from datetime import datetime
from models.user import User

users_ref = connection.db.collection('users')

def get_all():
    users = list()
    try:
        docs = users_ref.stream()
        for doc in docs:
            user = User(id = doc.id)
            user.from_dict(doc.to_dict())
            users.append(user.to_dict())
        code = 200
    except Exception as e:
        users = { 'Error': str(e) }
        code = 500
    return { "message": users, "code": code }

def login(obj):
    try:
        docs = users_ref.where('email', '==', obj.get('email')).where('pass', '==', obj.get('pass')).get()
        user = {}
        for doc in docs:
            userObj = User(id = doc.id)
            userObj.from_dict(doc.to_dict())
            user = userObj.to_dict()
        if 'id' in user :
            code = 200
        else:
            print(user)
            user = users = { 'Error': "User Not Found" }
            code = 401
    except Exception as e:
        user = { 'Error': str(e) }
        code = 500
    return { "message": user, "code": code }

def get(id):
    try:
        doc = users_ref.document(id).get()
        if doc.exists:
            userObj = User(id = doc.id)
            userObj.from_dict(doc.to_dict())
            user = userObj.to_dict()
            code = 200
        else:
            user = { "Error": "Usurio no encontrado" }
            code = 404
    except Exception as e:
        user = { 'Error': str(e) }
        code = 500
    return { "message": user, "code": code }

def create(obj):
    try:
        users_ref.add({
            'email': obj.get("email"),
            'name': obj.get("name"),
            'lastname': obj.get("lastname"),
            'pass': obj.get("pass"),
            'created_date': datetime.now(),
            'updated_date': datetime.now()
        })
        message = { 'message': "Usuario creado" }
        code = 200
    except Exception as e:
        message = { 'Error': str(e) }
        code = 500
    return { "message": message, "code": code }

def update(user, obj):
    try:
        users_ref.document(user).update({
            'email': obj.get("email"),
            'name': obj.get("name"),
            'lastname': obj.get("lastname"),
            'updated_date': datetime.now()
        })
        message = { 'message': "Usuario actualizado" }
        code = 200
    except Exception as e:
        message = { 'Error': str(e) }
        code = 500
    return { "message": message, "code": code }

def change_password(user, obj):
    try:
        users_ref.document(user).update({
            'pass': obj.get("pass"),
            'updated_date': datetime.now()
        })
        message = { 'message': "Usuario actualizado" }
        code = 200
    except Exception as e:
        message = { 'Error': str(e) }
        code = 500
    return { "message": message, "code": code }
