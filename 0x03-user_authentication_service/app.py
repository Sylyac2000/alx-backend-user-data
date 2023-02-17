#!/usr/bin/env python3
"""Flask app module
"""

from flask import Flask, jsonify, request, redirect, abort
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/')
def index():
    """index endpoint
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """login
    """
    email = request.form['email']
    password = request.form['password']
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": f"{email}", "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """logout
    """
    session_id = request.cookies.get('session_id')
    if not session_id:
        raise abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if user is not None:
        AUTH.destroy_session(user.id)
        return redirect('/')

    raise abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """profile
    """
    session_id = request.cookies.get('session_id')
    if not session_id:
        raise abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        raise abort(403)
    return jsonify({"email": user.email})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register() -> str:
    """register user
    """
    try:

        email = request.form['email']
        password = request.form['password']
        AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
