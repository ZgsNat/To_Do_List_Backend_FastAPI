from sqlalchemy.orm import Session
from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository
from src.infrastructure.database.models.user_model import User as UserModel 

class UserRepositoryImpl(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: User) -> User:
        db_user = UserModel(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return User.from_orm(db_user)

    def get_user_by_id(self, user_id: int) -> User:
        db_user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if db_user:
            return User.from_orm(db_user)
        return None

    def get_user_by_username(self, username: str) -> User:
        db_user = self.db.query(UserModel).filter(UserModel.username == username).first()
        if db_user:
            return User.from_orm(db_user)
        return None

    def update_user(self, user: User) -> User:
        db_user = self.db.query(UserModel).filter(UserModel.id == user.id).first()
        if db_user:
            for key, value in user.dict().items():
                setattr(db_user, key, value)
            self.db.commit()
            self.db.refresh(db_user)
            return User.from_orm(db_user)
        return None

    def delete_user(self, user_id: int) -> None:
        db_user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if db_user:
            self.db.delete(db_user)
            self.db.commit()