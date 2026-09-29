# FastAPI Demo Project

This project is a small FastAPI application that demonstrates a clean layered architecture using controllers, services, repositories, and schemas.

## Project Structure

- `app/main.py` - Starts the FastAPI application and registers routes.
- `app/controllers/user_controller.py` - Exposes the API endpoints for users.
- `app/services/user_service.py` - Contains business logic.
- `app/repositories/user_repository.py` - Handles in-memory data access.
- `app/schemas/user_schema.py` - Defines request and response models using Pydantic.

## How the App Starts

The application is initialized in `app/main.py`:

- A `FastAPI` instance is created.
- The user router is included with `app.include_router(user_router)`.
- A root health endpoint is registered at `/`.

To run the project locally:

```bash
uvicorn app.main:app --reload
```

After starting, the API is available at:

- `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Execution Flow

The request flow in this project is layered as follows:

1. Request enters the application
   - FastAPI receives the HTTP request.
   - The route matching happens in `app/main.py` and `app/controllers/user_controller.py`.

2. Controller layer handles routing
   - `user_controller.py` defines endpoints like:
     - `GET /users/{user_id}`
     - `POST /users`
     - `DELETE /users/{user_id}`
   - The controller receives the incoming request data and forwards it to the service layer.

3. Schema validation happens before business logic
   - `UserCreate` validates the request body.
   - `UserResponse` defines how responses are structured.
   - Pydantic ensures the data matches the expected fields and constraints such as age range.

4. Service layer contains business logic
   - `user_service.py` is responsible for validating business rules.
   - For example:
     - If a user is not found, it raises `HTTPException(404, "User not found")`.
     - It calls the repository to create, fetch, or delete users.

5. Repository layer handles data access
   - `user_repository.py` stores users in an in-memory dictionary.
   - It performs the actual CRUD operations:
     - `get_user(user_id)`
     - `create_user(user_data)`
     - `delete_user(user_id)`

6. Response is returned to the client
   - The repository returns the data object.
   - The service sends it back to the controller.
   - The controller returns the final response.
   - FastAPI serializes the response using `UserResponse`.

## Request Lifecycle Example

### Create a user

```text
Client -> FastAPI app -> user_controller.create_user() -> user_service.create_user() -> user_repository.create_user() -> in-memory users dict -> UserResponse
```

### Get a user

```text
Client -> FastAPI app -> user_controller.get_user() -> user_service.get_user() -> user_repository.get_user() -> 404 check -> UserResponse
```

### Delete a user

```text
Client -> FastAPI app -> user_controller.delete_user() -> user_service.delete_user() -> user_repository.delete_user() -> 404 check -> 204 No Content
```

## API Endpoints

### Health Check

- `GET /`
- Returns:
  - status
  - message

### Users

- `GET /users/{user_id}` - Fetch a specific user
- `POST /users` - Create a new user
- `DELETE /users/{user_id}` - Delete a user

## Notes

This project is intentionally simple and uses an in-memory data store instead of a database. It is designed to teach the architecture pattern commonly used in production FastAPI applications: route -> controller -> service -> repository -> database/model layer.
