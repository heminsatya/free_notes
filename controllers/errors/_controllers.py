# Dependencies
from aurora.helpers import controller

# Controllers routes
controllers = [
    controller(name='BadRequest', url='400', methods=['GET']),
    controller(name='AccessDenied', url='403', methods=['GET']),
    controller(name='NotFound', url='404', methods=['GET']),
    controller(name='MethodForbidden', url='405', methods=['GET']),
    controller(name='ServerError', url='500', methods=['GET']),
]#do-not-change-me
