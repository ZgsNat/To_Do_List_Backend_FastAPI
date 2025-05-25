from abc import ABC, abstractmethod
from src.domain.entities.user import User

class UserRepository(ABC):
    @abstractmethod
    def create_user(self, user: User) -> User:
        """Create a new user in the database."""
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        """Retrieve a user by their ID."""
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> User:
        """Retrieve a user by their username."""
        pass

    @abstractmethod
    def update_user(self, user: User) -> User:
        """Update an existing user's information."""
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        """Delete a user from the database."""
        pass