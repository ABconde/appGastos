class Expense:

    def __init__(self, **data):
        self.id = data.get('id')
        self.comment = 'Default Name'
        self.amount = 0
        self.account = 'Default Account'
        self.date = 'Default date'
        self.created_date = 'Default created date'
        self.updated_date = 'Default updated date'

    def from_dict(self, data):
        self.comment = data['comment']
        self.amount = data['amount']
        self.account = data['account']
        self.date = "{}".format(data['date'])
        self.created_date = "{}".format(data['created_date'])
        self.updated_date = "{}".format(data['updated_date'])

    def to_dict(self):
        return self.__dict__
