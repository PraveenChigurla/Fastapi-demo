from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str = Field(
        ...,
        examples=["Praveen"]
    )

    email: str = Field(
        ...,
        examples=["praveen@example.com"]
    )

    age: int = Field(
        ...,
        examples=[25],
        ge=1,
        le=120
    )


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int