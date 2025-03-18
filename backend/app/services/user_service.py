from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

async def create_user(user_data: UserCreate, db: Session):
    new_user = User(**user_data.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

async def get_user(user_id: str, db: Session):
    return db.query(User).filter(User.id == user_id).first()