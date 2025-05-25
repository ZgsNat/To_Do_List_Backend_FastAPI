from src.domain.repositories.user_repository import UserRepository
from src.utils.security import verify_password, create_access_token
from fastapi import HTTPException, status

class AuthUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def login(self, username: str, password: str):
        user = self.user_repository.get_user_by_username(username)
        if not user or not verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token = create_access_token(data={"sub": user.username})
        return {"access_token": access_token, "token_type": "bearer"}
    def register(self, username: str, password: str):
        if self.user_repository.get_user_by_username(username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists",
            )
        user = self.user_repository.create_user(username, password)
        return {"message": "User created successfully", "user_id": user.id}
    def logout(self, user_id: str):
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        # In a real application, you might want to invalidate the user's session or token here
        return {"message": "User logged out successfully"}