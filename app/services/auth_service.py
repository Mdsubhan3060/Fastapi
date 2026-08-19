from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.security import hash_password
from app.models.user import User
from app.schemas.auth import UserRegister,UserLogin,UserResponse
from app.core.security import(hash_password,verify_password,create_access_token,create_refresh_token)

async def register_user(
    db: AsyncSession,
    user_data: UserRegister
):
    hashed_password = hash_password(user_data.password)

    new_user = User(
        username=user_data.username,
        email=user_data.email,
        password_hash=hashed_password
    )

    db.add(new_user)

    try:
        await db.commit()
        await db.refresh(new_user)

    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Username or email already exists"
        )

    return new_user
async def authenticate_user(
    db: AsyncSession,
    user_data: UserLogin
):
    result = await db.execute(
        select(User).where(
            User.email == user_data.email
        )
    )

    user = result.scalar_one_or_none()
    if user is None:
        return None
    if not verify_password(
        user_data.password,user.password_hash
    ):
        return None
    return user
async def get_user(db:AsyncSession):
    result=await db.execute(select (User))
    user=result.scalars().all()
    if not user:
        return None
    return user