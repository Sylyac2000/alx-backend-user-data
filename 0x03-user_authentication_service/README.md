## 0x03. User authentication service

## Requirements
* Language: Javascript, Python 3.8.5 (and C )
* OS: Ubuntu 20.04 LTS
* Compiler: python3  (and gcc 9.3.0)
* Version: MySQL  8.0.25
* Style guidelines: [Pycodestyle] (https://github.com/PyCQA/pycodestyle)


## Synopsis
This repository holds some python projects I worked on at ALX SPECIALIZATION.


## Background Context
In this project, you will implement a Session Authentication. You are not allowed to install any other module.

In the industry, you should not implement your own Session authentication system and use a module or framework that doing it for you (like in Python-Flask: Flask-HTTPAuth). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

* How to declare API routes in a Flask app
* How to get and set cookies
* How to retrieve request form data
* How to return various HTTP status codes

# Requirements
##General
* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/env python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle style (version 2.5)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* All your functions should be type annotated
* The flask app should only interact with Auth and never with DB directly.
* Only public methods of Auth and DB should be used outside these classes

## Tasks

* 0. User model
* 1. create user
* 2. Find user
* 3. update user
* 4. Hash password
* 5. Register user
* 6. Basic Flask app
* 7. Register user
* 8. Credentials validation
* 9. Generate UUIDs
* 10. Get session ID
* 11. Log in
* 12. Find user by session ID

**Repo:**

*   GitHub repository: `alx-backend-user-data`
*   Directory: `0x03-user_authentication_service`

