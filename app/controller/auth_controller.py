from fastapi import APIRouter, HTTPException

from app.service.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])

service = AuthService()


@router.post("/login")
def login(data: dict):

    try:
        return service.login(data["username"], data["password"])

    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))