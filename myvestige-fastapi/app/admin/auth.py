from fastapi import Depends, HTTPException
from app.dependencies.auth import get_current_user
from app.api.users.models import User

async def admin_required(user: User = Depends(get_current_user)):
    """Ensure user has admin privileges"""
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Admin access required")
    return user