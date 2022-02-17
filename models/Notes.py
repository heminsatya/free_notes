# Dependencies
from aurora import Model

# The model class
class Notes(Model):

    # Model columns
    id = Model.column(datatype='int', size='lg', not_null=True)
    user_id = Model.column(datatype='int', size='lg', related_to='Users', on_update='CASCADE')
    title = Model.column(datatype='str', size='xs', not_null=True)
    content = Model.column(datatype='str', size='sm', not_null=True)
    date = Model.column(datatype='datetime', not_null=True, default="CURRENT_TIMESTAMP")

    # Model constructor
    def __init__(self):
        # Inherit the parent class
        super().__init__()

        # Override the parent class default properties
        self.table = 'notes'
        self.primary_key = 'id'

        # Repair the database
        self.repair = {}
