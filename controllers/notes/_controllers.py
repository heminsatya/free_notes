# Dependencies
from aurora.helpers import controller

# Controllers routes
controllers = [
    controller(name='Index', url='', methods=['GET']),
    controller(name='Notes', url='my-notes', methods=['DELETE', 'GET']),
    controller(name='NewNote', url='new-note', methods=['GET', 'POST']),
    controller(name='EditNote', url='edit-note', methods=['GET', 'PUT']),
    controller(name='EditNote', url='edit-note/<int:id>', methods=['GET', 'PUT']),
]#do-not-change-me
