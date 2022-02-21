# Dependencies
from aurora.helpers import controller

# Controllers routes
controllers = [
    controller(name='BadRequest', url='400'),
    controller(name='AccessDenied', url='403'),
    controller(name='NotFound', url='404'),
    controller(name='MethodForbidden', url='405'),
    controller(name='ServerError', url='500'),
]#do-not-change-me
