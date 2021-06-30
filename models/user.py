class User:

    def __init__(self, **data):
        self.id = data.get('id')
        self.name = 'Default Name'
        self.lastname = 'Default Lastname'
        self.email = 'Default email'
        self.pw = 'Defaul pass'
        self.created_Date = 'Default created date'
        self.updated_Date = 'Default updated date'

    def from_dict(self, data):
        self.name = data['name']
        self.lastname = data['lastname']
        self.email = data['email']
        self.pw = data['pass']
        self.created_date = "{}".format(data['created_date'])
        self.updated_date = "{}".format(data['updated_date'])

    def to_dict(self):
        return self.__dict__