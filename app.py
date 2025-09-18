from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from flasgger import Swagger
import datetime
from mcp import create_app

app = create_app()

@app.route('/', methods=['GET'])
def hello_world():
    return {"message": "hello world"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
