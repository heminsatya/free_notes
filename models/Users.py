# Dependencies
from aurora import Model

# The model class
class Users(Model):

    # Model columns
    id = Model.column(datatype='integer', not_null=True)
    username = Model.column(datatype='varchar(100)', unique=True, not_null=True)
    email = Model.column(datatype='varchar(100)', unique=True, not_null=True)
    password = Model.column(datatype='varchar(500)', not_null=True)

    # Model meta data
    def __init__(self):
        # Inherit the parent class
        super().__init__()

        # Override the parent class default properties
        self.table = 'users'
        self.primary_key = 'id'
