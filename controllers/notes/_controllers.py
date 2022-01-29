##
# @Caution! Please do not change this file until you fully understand the controllers documentation.
# @Desc: App Controllers
# @Ex: ('ControllerName', 'controller-url', [methods]),
# @info! Methods are optional. Supported methods are ['GET', 'POST', 'PUT']. The ['Get'] is the default method.
# 
controllers = [
   ('Index', '', ['GET']),
   ('Notes', 'my-notes', ['DELETE', 'GET']),
   ('NewNote', 'new-note', ['GET', 'POST']),
   ('EditNote', 'edit-note', ['GET', 'PUT']),
   ('EditNote', 'edit-note/<int:id>', ['GET', 'PUT']),
]#do-not-change-me