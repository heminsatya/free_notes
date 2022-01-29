_models = ('Users', 'Notes')

Users = {'table': 'users', 'col_type': {'id': 'integer', 'username': 'varchar(100)', 'email': 'varchar(100)', 'password': 'varchar(500)'}, 'primary_key': 'id', 'unique': ['username', 'email'], 'not_null': ['id', 'username', 'email', 'password'], 'default': {}, 'foreign_key': {}}

Notes = {'table': 'notes', 'col_type': {'id': 'integer', 'user_id': 'integer', 'title': 'text', 'content': 'text', 'date': 'date'}, 'primary_key': 'id', 'unique': [], 'not_null': ['id', 'title', 'content', 'date'], 'default': {}, 'foreign_key': {'user_id': {'r_table': 'users', 'r_column': 'id', 'on_update': 'CASCADE', 'on_delete': 'CASCADE'}}}

