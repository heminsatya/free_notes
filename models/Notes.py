# Dependencies
from aurora import Model

# The model class
class Notes(Model):

    # Model columns
    id = Model.column(datatype='integer', not_null=True)
    user_id = Model.column(datatype='integer', related_to='Users')
    title = Model.column(datatype='text', not_null=True)
    content = Model.column(datatype='text', not_null=True)
    date = Model.column(datatype='date', not_null=True)

    # Model meta data
    def __init__(self):
        # Inherit the parent class
        super().__init__()

        # Override the parent class default properties
        self.table = 'notes'
        self.primary_key = 'id'
