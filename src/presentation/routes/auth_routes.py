from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from src.infrastructure.security.oauth import get_current_admin
from src.application.services.auth_service import AuthService
from src.infrastructure.database.db import get_db
from src.infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from src.schemas.user_schema import Token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(lambda: AuthService(UserRepositoryImpl(get_db()))),
):
    """
    Login user and return access token.
    """
    try:
        return auth_service.login(form_data.username, form_data.password)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        ) from e
    
@router.post("/logout")
def logout():
    """
    Logout user.
    """
    return {"message": "Logout successful"}

@router.get("/admin-only")
def admin_only(current_user: str = Depends(get_current_admin)):
    """
    Admin-only route.
    """
    return {"message": "This is an admin-only route"}