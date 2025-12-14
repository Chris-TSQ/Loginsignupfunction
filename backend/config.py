import os
from typing import List


class Settings:
    """Application configuration"""
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "secret-key")
    ALGORITHM: str = "HS256"
    TOKEN_EXPIRY_HOURS: int = 24
    
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:8080",
        "http://localhost:3000",
        "http://localhost:5173",
        "https://loginsignupfunction.vercel.app",
        "https://loginsignupfunction-xli2.vercel.app",  # Add other Vercel domain
    ]
    
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True


settings = Settings()