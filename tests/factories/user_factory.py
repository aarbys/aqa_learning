from uuid import uuid4


def build_user_data() -> dict[str, str]:
    unique_value = uuid4().hex[:10]
    phone = str(uuid4().int)[:10]
    return {
        "name": f"User_{unique_value}",
        "email": f"user_{unique_value}@example.com",
        "phone": f"+7{phone}",
    }
    