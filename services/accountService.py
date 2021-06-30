import connection
from datetime import date, datetime
from models.account import Account

account_ref = connection.db.collection('accounts')

def get_by_user(user):
    try:
        accounts = list()
        docs = account_ref.where('user', "==", user).get()
        for doc in docs:
            accountObj = Account(id = doc.id)
            accountObj.from_dict(doc.to_dict())
            account = accountObj.to_dict()
            accounts.append(account)
        code = 200
    except Exception as e:
        accounts = { 'Error': str(e) }
        code = 500 
    return { "message": accounts, "code": code }


def create(obj):
    try:
        account_ref.add({
            'user': obj.get("user"),
            'name': obj.get("name"),
            'created_date': datetime.now(),
            'updated_date': datetime.now()
        })
        message = { 'message': "Cuenta creado" }
        code = 200
    except Exception as e:
        message = { 'Error': str(e) }
        code = 500
    return { "message": message, "code": code }

def update(account, obj):
    try:
        account_ref.document(account).update({
            'name': obj.get("name"),
            'updated_date': datetime.now()
        })
        message = { 'message': "Cuenta actualizada" }
        code = 200
    except Exception as e:
        message = { 'Error': str(e) }
        code = 500
    return { "message": message, "code": code }

def delete(account):
    try:
        account_ref.document(account).delete()
        message = { 'message': "Cuenta eliminada" }
        code = 200
    except Exception as e:
        message = { 'Error': str(e) }
        code = 500
    return { "message": message, "code": code }