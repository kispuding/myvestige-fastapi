
from fastapi_admin_next import init_admin_db
from sqladmin import Admin

from app.api.users.models import User
from app.db.session import async_session_maker

async def init_admin():
    """Initialize FastAPI Admin"""
    await init_admin_db(async_session_maker)

admin = Admin(title="My Admin Panel")
admin.add_resource(User, label="Users")