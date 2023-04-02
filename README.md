# Welcome to Free Notes (Multi Language)

Free Notes is a web application to create dynamic free notes, written in [Python](https://www.python.org/) 
and built on [Aurora](https://github.com/heminsatya/aurora) framework.

It is an MVC web application based on REST architecture.

It uses Vanilla JavaScript for the front-end development.

You can find all the dependencies for this project at the end of this file.

> Please note that this project is created for testing the functionality of the Aurora framework.
> You can find a detailed documentation for aurora framework on [Aurora Docs](https://github.com/heminsatya/aurora/tree/main/docs).


## Features And Specifications

- Free Notes is a responsive, mobile-first web application.
- It is a multi-user web application, with a Login/Register system.
- Users can create dynamic notes using a WYSIWYG HTML editor.
- Users can manage all their notes and perform some actions to them.
- Users can edit and delete their notes. 
- Each user can only access to their own notes.
- It uses SQLite database for managing the application data.
- It is a [RESTFUL](https://en.wikipedia.org/wiki/Representational_state_transfer) web application.
- It uses JavaScript to send forms to the server.
- It uses a CSRF token for forms to protect against CSRF attacks.


# Project Files

## Apps

In addition to the `errors` app and `aurora` app that comes with the Aurora framework, 
It has two other apps:

- users: For login, register and logout the users.
- notes - For create, update and delete notes for the users.


## App Components:

### Controllers

The controllers directory contains all the controllers for all the apps. Each app has its own
subdirectory that contains all the controller classes of that application.

Each controller class can provide up to four RESTFUL CRUD methods:

CRUD Methods | HTTP Methods | Controller Methods
------------ | ------------ | ------------------
Create       | POST         | **post**
Read         | GET          | **get**
Update       | PUT          | **put**
Delete       | DELETE       | **delete**


### Forms

For forms I have used only the CSRF attribute of WTForms, and have validated forms via python code.


### Database Initialization

To initialize the database run the following command:

```
(venv) python manage.py init-db 
```

### Models

This application uses two models:

- Users - Which is responsible to manipulate the `users` table of the database.
- Notes - Which is responsible to manipulate the `notes` table of the database.

> These models are AuroraSQL models.


### Static Files

Each application has its own static files inside the `statics` directory.

There is also a subdirectory  called `assets` which is used for all the apps.


### View Files

Each application has its own view files inside the `views` directory.

Each view file is an HTML like Jinja2 template.


## Modules

- `_apps.py` is a system module from Aurora framework that contains a python collection of all installed apps.
- `app.py` module is used for instantiate the root app of Aurora framework, to serve all the child apps and run the server.
- `config.py` is the configuration module for the whole project.
- `manage.py` module is the CLI application of Aurora framework.
- `app.db` is the SQLite database file created by Aurora framework.


# Project Dependecies

## Front-End

- [Bootstrap 4.5](https://getbootstrap.com/docs/4.5/).
- [Summernote WYSIWYG Editor](https://summernote.org/).


## Backend-End

- [Python](https://www.python.org/) version 3 or higher.
- [Aurora](https://github.com/heminsatya/aurora) Framework.
- [Flask](https://github.com/pallets/flask) Framework.
- [WTForms](https://pypi.org/project/WTForms/).

