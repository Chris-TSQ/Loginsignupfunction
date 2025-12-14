import os
from typing import List


class Settings:
    """Application configuration"""
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "secret-key")
    ALGORITHM: str = "HS256"
    TOKEN_EXPIRY_HOURS: int = 24
    
    ALLOWED_ORIGINS: List[str] = [*,
        "http://localhost:8080",
    "http://localhost:3000",           # Local development
    "http://localhost:5173",           # Vite dev server
    "https://loginsignupfunction-6gsd.vercel.app",     # Vercel domain (for deploy)
    "https://*.vercel.app",            # All Vercel preview deployments
]    
    
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True


settings = Settings()