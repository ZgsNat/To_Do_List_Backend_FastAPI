from dataclasses import dataclass
from enum import Enum

class Role(str, Enum):
    USER = "user"
    ADMIN = "admin"

@dataclass
class User:
    id: int
    username: str
    email: str
    password: str
    role: Role = Role.USER
    dob: str = None
    # Date of Birth in YYYY-MM-DD format   

    def __post_init__(self):
        if not isinstance(self.role, Role):
            raise ValueError(f"Invalid role: {self.role}. Must be one of {list(Role)}")