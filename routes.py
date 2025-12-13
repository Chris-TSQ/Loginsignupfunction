from fastapi import FastAPI

from models import UserSignup, UserLogin, Token
from services import AuthService


class AuthAPI:
    """FastAPI route handlers"""
    
    def __init__(self, app: FastAPI, auth_service: AuthService):
        self.app = app
        self.auth_service = auth_service
        self._setup_routes()
    
    def _setup_routes(self):
        """Setup all routes"""
        self.app.get("/")(self.read_root)
        self.app.post("/signup", response_model=Token)(self.signup)
        self.app.post("/login", response_model=Token)(self.login)
        self.app.get("/verify")(self.verify)
    
    def read_root(self):
        """Root endpoint"""
        return {"message": "Auth API is running"}
    
    def signup(self, user: UserSignup) -> Token:
        """Create new user account"""
        return self.auth_service.signup(user)
    
    def login(self, credentials: UserLogin) -> Token:
        """Authenticate user"""
        return self.auth_service.login(credentials)
    
    def verify(self, token: str):
        """Verify JWT token"""
        return self.auth_service.verify_token(token)