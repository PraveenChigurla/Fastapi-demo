from fastapi import FastAPI

from app.controllers.user_controller import router as user_router


app = FastAPI(
    title="FastAPI Demo API",
    description="A production-style FastAPI demo demonstrating controllers, services, repositories, schemas, and OpenAPI documentation.",
    version="1.0.0",
)


app.include_router(user_router)


@app.get(
    "/",
    tags=["Health"],
    summary="Health check"
)
def health_check():

    return {
        "status": "ok",
        "message": "FastAPI application is running"
    }