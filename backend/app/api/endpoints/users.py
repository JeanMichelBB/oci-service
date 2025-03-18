from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user, get_user

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def create_user_endpoint(user: UserCreate):
    return await create_user(user)

@router.get("/{user_id}", response_model=UserResponse)
async def get_user_endpoint(user_id: str):
    user = await get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user