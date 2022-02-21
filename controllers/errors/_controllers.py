# Dependencies
from aurora.helpers import router

# Controllers routes
controllers = [
    router(controller='BadRequest', url='400'),
    router(controller='AccessDenied', url='403'),
    router(controller='NotFound', url='404'),
    router(controller='MethodForbidden', url='405'),
    router(controller='ServerError', url='500'),
]#do-not-change-me
