# Dependencies
from aurora.helpers import router

# Controllers routes
controllers = [
    router(controller='Index'),
    router(controller='Notes', url='my-notes', methods=['DELETE', 'GET']),
    router(controller='NewNote', url='new-note', methods=['GET', 'POST']),
    router(controller='EditNote', url='edit-note', methods=['GET', 'PUT']),
    router(controller='EditNote', url='edit-note/<int:id>', methods=['GET', 'PUT']),
]#do-not-change-me
