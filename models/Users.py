# Dependencies
from aurora import Model

# The model class
class Users(Model):

    # Model columns
    id = Model.column(datatype='int', size='lg', not_null=True)
    username = Model.column(datatype='str', size='xs', unique=True, not_null=True)
    email = Model.column(datatype='str', size='xs', unique=True, not_null=True)
    password = Model.column(datatype='str', size='sm', not_null=True)

    # Model constructor
    def __init__(self):
        # Inherit the parent class
        super().__init__()

        # Override the parent class default properties
        self.table = 'users'
        self.primary_key = 'id'

        # Repair the database
        self.repair = {}
