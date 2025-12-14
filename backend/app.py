from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from config import settings
from repository import UserRepository
from services import TokenService, AuthService
from routes import AuthAPI


def create_app() -> FastAPI:
    """Create and configure FastAPI application"""
    app = FastAPI(title="Auth API", version="1.0.0")
        
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # services
    user_repository = UserRepository()
    token_service = TokenService(
        secret_key=settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
        expiry_hours=settings.TOKEN_EXPIRY_HOURS
    )
    auth_service = AuthService(user_repository, token_service)
    
    # Setup
    AuthAPI(app, auth_service)
    
    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )