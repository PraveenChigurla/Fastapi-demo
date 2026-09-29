from fastapi import HTTPException

from app.repositories import user_repository


def get_user(user_id: int):

    user = user_repository.get_user(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


def create_user(user_data):

    return user_repository.create_user(
        user_data.model_dump()
    )


def delete_user(user_id: int):

    deleted = user_repository.delete_user(user_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )