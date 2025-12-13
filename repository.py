from typing import Dict, Optional


class UserRepository:
    """Handles user database operations"""
    
    def __init__(self):
        self.users_db: Dict[str, Dict] = {}
    
    def user_exists(self, email: str) -> bool:
        """Check if user exists"""
        return email in self.users_db
    
    def create_user(self, name: str, email: str, hashed_password: str) -> Dict:
        """Create new user"""
        user = {
            "name": name,
            "email": email,
            "password": hashed_password
        }
        self.users_db[email] = user
        return user
    
    def get_user(self, email: str) -> Optional[Dict]:
        """Retrieve user by email"""
        return self.users_db.get(email)
    
    def get_user_response(self, email: str) -> Optional[Dict]:
        """Get user data for response (without password)"""
        user = self.get_user(email)
        if user:
            return {"name": user["name"], "email": user["email"]}
        return None
    
    def delete_user(self, email: str) -> bool:
        """Delete user by email"""
        if email in self.users_db:
            del self.users_db[email]
            return True
        return False
    
    def get_all_users(self) -> list:
        """Get all users (without passwords)"""
        return [{"name": u["name"], "email": u["email"]} for u in self.users_db.values()]