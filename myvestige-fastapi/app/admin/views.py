from fastapi_admin.resources import Model
from app.api.users.models import User
from fastapi_admin.depends import get_current_admin

class UserAdmin(Model):
    resource_type = "users"
    label = "Users"
    model = User
    page_size = 10