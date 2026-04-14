from fastapi import APIRouter

router = APIRouter(prefix="/auth")

@router.get("/")
def test_auth():
    return {"msg": "auth working"}
