from passlib.hash import pbkdf2_sha256
import jwt
from datetime import datetime, timedelta
from app import app

def hash_password(password):
    return pbkdf2_sha256.hash(password)

def verify_password(password, hash):
    return pbkdf2_sha256.verify(password, hash)

def generate_jwt(user_id):
    payload = {
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': user_id
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
