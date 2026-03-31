# 🔐 Auth API + Frontend (Fullstack Authentication System)

A clean, modular **authentication system** built with:

- ⚡ **FastAPI (Python backend)**
- 🔑 **JWT-based authentication**
- 🔒 **bcrypt password hashing**
- 🧠 **Service-layer architecture**
- 🌐 **Vanilla JavaScript frontend (MVC-style)**

This project demonstrates a production-style structure with separation of concerns, making it ideal for learning or extending into real-world apps.

---

## ✨ Features

### 🔐 Backend (FastAPI)
- User signup & login
- Password hashing with `bcrypt`
- JWT token generation & verification
- Token expiration handling
- CORS support for frontend integration
- Clean architecture (routes → services → repository)

### 🧠 Architecture
- **Repository Layer** → Data storage abstraction
- **Service Layer** → Business logic (Auth, Tokens, Passwords)
- **API Layer** → Route handlers

### 🌐 Frontend
- Login / Signup toggle UI
- Real-time form state handling
- API integration
- Loading states & error handling
- Token display after authentication

---

## 📁 Project Structure


project/
│
├── backend/
│ ├── main.py # App entrypoint
│ ├── config.py # Environment & settings
│ ├── models.py # Pydantic schemas
│ ├── repository.py # User data storage
│ ├── services.py # Auth, Token, Password logic
│ └── routes.py # API routes
│
├── frontend/
│ ├── api.js # API wrapper
│ ├── controller.js # App controller
│ ├── state.js # App state management
│ ├── ui.js # UI updates
│ └── index.html # Frontend UI
│
└── README.md


---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/auth-api-project.git
cd auth-api-project
```
2️⃣ Backend Setup
Install dependencies
pip install fastapi uvicorn python-dotenv bcrypt pyjwt
Create .env file
```
SECRET_KEY=your_secret_key_here
MONGODB_URL=
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
DEBUG=True
PORT=8000
```
Run the server
python main.py

Server will run at:

http://localhost:8000
3️⃣ Frontend Setup

Simply open your HTML file in a browser:

frontend/index.html

Or serve it with a local dev server (recommended).

🔌 API Endpoints
🟢 Base URL
http://localhost:8000
🔐 Auth Routes
➕ Signup
POST /signup

Body:
```
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123"
}
```
🔑 Login
POST /login

Body:
```
{
  "email": "john@example.com",
  "password": "password123"
}
```
✅ Verify Token
GET /verify?token=YOUR_JWT_TOKEN
🔐 Authentication Flow
User signs up → password is hashed
User logs in → credentials verified
JWT token is issued
Token is stored in frontend state
Protected requests can verify token
⚙️ Configuration

All configuration is handled via config.py:

Setting	Description
SECRET_KEY	JWT signing key
ALGORITHM	JWT algorithm (default: HS256)
TOKEN_EXPIRY_HOURS	Token validity duration
ALLOWED_ORIGINS	CORS whitelist
PORT	Server port
🧠 Key Concepts Demonstrated
Dependency Injection (services passed into routes)
JWT Authentication
Password hashing (bcrypt)
Clean code separation (SOLID principles)
Frontend state management without frameworks
Async API handling
⚠️ Limitations (For Learning)
Uses in-memory database (data resets on restart)
No refresh tokens
No role-based access control
No persistent storage (MongoDB config is placeholder)
## 🛠️ Future Improvements
✅ Add MongoDB / PostgreSQL integration
🔄 Implement refresh tokens
🔐 Add protected routes (middleware)
👤 User profile management
🌍 Deploy backend (Render / Railway)
⚡ Deploy frontend (Vercel)
🧪 Example Response
```
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```
💡 Tips
Make sure backend is running before using frontend
Check browser console for API errors
Ensure CORS origins match your frontend URL

⭐ If you like this project

Give it a star ⭐ and use it as a base for your next app!
