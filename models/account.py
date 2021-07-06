class Account:
    
    def __init__(self, **data):
        self.id = data.get('id')
        self.name = 'Default Name'
        self.created_date = 'Default created date'
        self.updated_date = 'Default updated date'

    def from_dict(self, data):
        self.name = data['name']
        self.created_date = "{}".format(data['created_date'])
        self.updated_date = "{}".format(data['updated_date'])

    def to_dict(self):
        return self.__dict__