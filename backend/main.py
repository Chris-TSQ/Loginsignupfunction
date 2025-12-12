from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import Optional
import jwt
import bcrypt
from datetime import datetime, timedelta

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_KEY = "secret-key"
ALGORITHM = "HS256"

users_db = {}

class UserSignup(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    token: str
    user: dict

def hash_password(password: str) -> str:
    """Hash password using bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against hash"""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_token(email: str) -> str:
    """Create JWT token"""
    payload = {
        'email': email,
        'exp': datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

@app.get("/")
def read_root():
    return {"message": "Auth API is running"}

@app.post("/signup", response_model=Token)
def signup(user: UserSignup):
    """Create new user account"""
    
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pw = hash_password(user.password)
    users_db[user.email] = {
        "name": user.name,
        "email": user.email,
        "password": hashed_pw
    }
    
    token = create_token(user.email)
    
    return {
        "token": token,
        "user": {
            "name": user.name,
            "email": user.email
        }
    }

@app.post("/login", response_model=Token)
def login(credentials: UserLogin):
    """Login user"""
    
    if credentials.email not in users_db:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    user = users_db[credentials.email]
    
    # Verify password
    if not verify_password(credentials.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    token = create_token(credentials.email)
    
    return {
        "token": token,
        "user": {
            "name": user["name"],
            "email": user["email"]
        }
    }

@app.get("/verify")
def verify_token(token: str):
    """Verify JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("email")
        
        if email not in users_db:
            raise HTTPException(status_code=401, detail="User not found")
        
        user = users_db[email]
        return {
            "valid": True,
            "user": {
                "name": user["name"],
                "email": user["email"]
            }
        }
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)