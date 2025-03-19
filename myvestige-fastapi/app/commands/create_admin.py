import asyncio
import bcrypt
from sqlalchemy.future import select

# Import from the root directory
from database import async_session_maker
from models import User  # Ensure models.py is also in the root

async def create_admin():
    async with async_session_maker() as session:
        result = await session.execute(select(User).where(User.username == "admin"))
        existing_admin = result.scalars().first()

        if existing_admin:
            print("Admin user already exists!")
            return

        hashed_password = bcrypt.hashpw("adminpassword".encode(), bcrypt.gensalt()).decode()
        admin_user = User(username="admin", hashed_password=hashed_password, is_admin=True)

        session.add(admin_user)
        await session.commit()
        print("Admin user created successfully!")

asyncio.run(create_admin())