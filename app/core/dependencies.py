from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import oauth2_scheme,decode_access_token
from app.database.dependencies import get_db
from app.models.user import User


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db:AsyncSession=Depends(get_db)
):
    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    user_id=payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid token")
    
    result=await db.execute(select(User).where(User.id==int(user_id)))
    user=result.scalar_one_or_none()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is not found")
    return user
async def require_admin(
        current_user: User=Depends(get_current_user)
):
    if current_user.role!="admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="admin access require")
    return current_user 