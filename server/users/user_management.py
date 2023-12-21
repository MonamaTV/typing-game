from fastapi import APIRouter

router = APIRouter(
    prefix="/users"
)

@router.get("/me")
def get_user():
    pass

@router.patch("/")
def update_user():
    pass

@router.delete("/")
def delete_user():
    pass

