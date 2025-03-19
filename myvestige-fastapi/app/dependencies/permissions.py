from fastapi import Depends, HTTPException
from app.dependencies.auth import get_current_user
from app.api.users.models import User

def admin_required(user: User = Depends(get_current_user)):
    """Check if user is an admin"""
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="You do not have permission to access this resource")
    return user