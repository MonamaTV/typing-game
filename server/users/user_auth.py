from fastapi import APIRouter
from ..models import user_model
router = APIRouter(
    prefix="/auth"
)


@router.post("/login")
def login(data: user_model):
    return data


@router.post("/register")
def register():
    pass


@router.post("/change-password")
def change_password():
    pass


"""
Typing:
    : t_id
    : user_id
    : wpm
    : wps
    : accuracy
    : time_completed
    : date_played
    : avg_words_typed
    :
"""
