import connection
from datetime import date, datetime
from models.expense import Expense

expense_ref = connection.db.collection('expenses')

# Rango de fecha (ultimos 30 dias, de un solo mes, 2 meses)

def get_all_by_account(account):
    try:
        expenses = list()
        total = 0
        docs = expense_ref.where('account', "==", account).get()
        for doc in docs:
            expenseObj = Expense(id = doc.id)
            expenseObj.from_dict(doc.to_dict())
            expense = expenseObj.to_dict()
            total += expenseObj.amount
            expenses.append(expense)
        data = { "data": expenses, "total": total }
        code = 200
    except Exception as e:
        data = { 'Error': str(e) }
        code = 500 
    return { "message": data, "code": code }

def get_by_acount_and_date_range(account, obj):
    try:
        start_date = datetime.strptime(obj.get('start_date'), "%d/%m/%Y")
        end_date = datetime.strptime(obj.get('end_date'), "%d/%m/%Y")
        print("{} => start, {} => end".format(start_date, end_date))
        expenses = list()
        total = 0
        docs = expense_ref.where('account', "==", account).where('date', '<=', end_date).where('date', '>=', start_date).stream()
        for doc in docs:
            expenseObj = Expense(id = doc.id)
            expenseObj.from_dict(doc.to_dict())
            expense = expenseObj.to_dict()
            total += expenseObj.amount
            expenses.append(expense)
        data = { "data": expenses, "total": total }
        code = 200
    except Exception as e:
        data = { 'Error': str(e) }
        code = 500 
    return { "message": data, "code": code }