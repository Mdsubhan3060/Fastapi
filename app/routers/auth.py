from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.dependencies import get_db
from app.schemas.auth import UserRegister
from app.services.auth_service import register_user,authenticate_user,get_user
from app.schemas.auth import UserRegister, UserResponse,UserLogin
from app.core.security import create_access_token
from app.core.dependencies import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)
@router.get("/me",response_model=UserResponse)
async def get_me(
    current_user = Depends(get_current_user)
):
    return current_user

@router.post("/register", response_model=UserResponse)
async def register(
    user: UserRegister,
    db: AsyncSession = Depends(get_db)
):
    return await register_user(db, user)
@router.post("/login")
async def login(
    form_data:OAuth2PasswordRequestForm=Depends(),
    db: AsyncSession = Depends(get_db)
):
    authenticated_user =authenticated_user = await authenticate_user(
    db,
    UserLogin(
        email=form_data.username,
        password=form_data.password
    )
)
    

    if authenticated_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    access_token = create_access_token(
        authenticated_user.id
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
    
@router.get("users")
async def users( db: AsyncSession = Depends(get_db)):
    result=await get_user(db)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail="No records Found"
        )
    return result 