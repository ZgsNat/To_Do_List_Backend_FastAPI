from src.application.use_cases.auth_use_case import AuthUseCase
from src.domain.repositories.user_repository import UserRepository

class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.auth_use_case = AuthUseCase(user_repository)

    def login(self, username: str, password: str):
        return self.auth_use_case.login(username, password)