from fastapi import APIRouter, Depends

from app.core.dependencies import require_admin
from app.models.user import User
from app.schemas.auth import AdminUserResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.dependencies import get_db

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/users",response_model=list[AdminUserResponse])
async def get_all_users(
    current_user: User = Depends(require_admin),
    db:AsyncSession=Depends(get_db)
):
    result = await db.execute(select(User))
    users = result.scalars().all()

    return users