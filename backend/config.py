import os
from typing import List
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "nsarbmfrpdvualvmtwzspspsinhqbvdr")
    ALGORITHM: str = "HS256"
    TOKEN_EXPIRY_HOURS: int = 24
    
    # MongoDB
    MONGODB_URL: str = os.getenv("MONGODB_URL", "")
    
    # CORS with Vercel domain
    ALLOWED_ORIGINS: List[str] = os.getenv(
        "ALLOWED_ORIGINS",
        "http://localhost:5173,http://localhost:3000,https://loginsignupfuncti.vercel.app"
    ).split(",")
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = int(os.getenv("PORT", 8000))
    DEBUG: bool = os.getenv("DEBUG", "False") == "True"

settings = Settings()