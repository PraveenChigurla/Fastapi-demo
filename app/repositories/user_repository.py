users = {
    1: {
        "id": 1,
        "name": "John",
        "email": "john@example.com",
        "age": 30
    }
}


def get_user(user_id: int):
    return users.get(user_id)


def create_user(user_data: dict):
    new_id = max(users.keys(), default=0) + 1

    new_user = {
        "id": new_id,
        **user_data
    }

    users[new_id] = new_user

    return new_user


def delete_user(user_id: int):
    if user_id not in users:
        return False

    del users[user_id]

    return True