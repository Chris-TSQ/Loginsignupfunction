import jwt
import bcrypt
from datetime import datetime, timedelta
from typing import Dict
from fastapi import HTTPException

from models import UserSignup, UserLogin, Token
from repository import UserRepository


class PasswordService:
    """Handles password hashing and verification"""
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash password using bcrypt"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify password against hash"""
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


class TokenService:
    """Handles JWT token creation and verification"""
    
    def __init__(self, secret_key: str, algorithm: str = "HS256", expiry_hours: int = 24):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.expiry_hours = expiry_hours
    
    def create_token(self, email: str) -> str:
        """Create JWT token"""
        payload = {
            'email': email,
            'exp': datetime.utcnow() + timedelta(hours=self.expiry_hours)
        }
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
    
    def verify_token(self, token: str) -> Dict:
        """Verify and decode JWT token"""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")


class AuthService:
    """Main authentication service"""
    
    def __init__(self, repository: UserRepository, token_service: TokenService):
        self.repository = repository
        self.token_service = token_service
        self.password_service = PasswordService()
    
    def signup(self, user: UserSignup) -> Token:
        """Register new user"""
        if self.repository.user_exists(user.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        
        hashed_pw = self.password_service.hash_password(user.password)
        self.repository.create_user(user.name, user.email, hashed_pw)
        
        token = self.token_service.create_token(user.email)
        user_data = self.repository.get_user_response(user.email)
        
        return Token(token=token, user=user_data)
    
    def login(self, credentials: UserLogin) -> Token:
        """Authenticate user and return token"""
        user = self.repository.get_user(credentials.email)
        
        if not user:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        
        if not self.password_service.verify_password(credentials.password, user["password"]):
            raise HTTPException(status_code=401, detail="Invalid email or password")
        
        token = self.token_service.create_token(credentials.email)
        user_data = self.repository.get_user_response(credentials.email)
        
        return Token(token=token, user=user_data)
    
    def verify_token(self, token: str) -> Dict:
        """Verify token and return user data"""
        payload = self.token_service.verify_token(token)
        email = payload.get("email")
        
        user_data = self.repository.get_user_response(email)
        if not user_data:
            raise HTTPException(status_code=401, detail="User not found")
        
        return {"valid": True, "user": user_data}