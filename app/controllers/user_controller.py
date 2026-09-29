from fastapi import APIRouter, status

from app.schemas.user_schema import (
    UserCreate,
    UserResponse
)

from app.services import user_service


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Get a user",
    description="Fetch a user using their unique user ID.",
    responses={
        404: {
            "description": "User not found"
        }
    }
)
def get_user(user_id: int):

    return user_service.get_user(user_id)


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a user",
    description="Create a new user.",
)
def create_user(user: UserCreate):

    return user_service.create_user(user)


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a user",
    description="Delete a user using their unique user ID.",
    responses={
        404: {
            "description": "User not found"
        }
    }
)
def delete_user(user_id: int):

    user_service.delete_user(user_id)

    return None