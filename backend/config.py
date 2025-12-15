import os
from typing import List
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Application configuration"""
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "nsarbmfrpdvualvmtwzspspsinhqbvdr")
    ALGORITHM: str = "HS256"
    TOKEN_EXPIRY_HOURS: int = 24
    
    # MongoDB
    MONGODB_URL: str = os.getenv("MONGODB_URL", "")
    
    # CORS - Frontend URLs that can access this backend
    # Set in Render environment as comma-separated list:
    # https://loginsignupfuncti.vercel.app,http://localhost:5173
    ALLOWED_ORIGINS: List[str] = os.getenv(
        "ALLOWED_ORIGINS",
        "http://localhost:5173,http://localhost:3000"
    ).split(",")
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = int(os.getenv("PORT", 8000))
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"


settings = Settings()