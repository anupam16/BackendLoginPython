from flask import request
from flask_restful import Resource
from app import db, api
from app.models import User
from app.utils import hash_password, verify_password, generate_jwt

class UserSignUp(Resource):
    def post(self):
        data = request.json
        new_user = User(
            full_name=data['full_name'],
            email=data['email'],
            phone_number=data['phone_number'],
            username=data['username'],
            password=hash_password(data['password'])
        )
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created successfully' ,'code':200}, 201

class UserLogin(Resource):
    def post(self):
        data = request.json
        user = User.query.filter_by(username=data['username']).first()
        if user and verify_password(data['password'], user.password):
            token = generate_jwt(user.id)
            return {'token': token,'code':200}, 200
        return {'message': 'Invalid credentials', "code":401}, 401

api.add_resource(UserSignUp, '/signup')
api.add_resource(UserLogin, '/login')
