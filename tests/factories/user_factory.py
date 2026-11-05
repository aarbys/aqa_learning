from uuid import uuid4
from  random import choice
from faker import Faker

fake = Faker('ru_RU')


def build_user_data() -> dict[str, str]:
    gender = choice(["male", "female"])
    
    # generating fake names
    first_name = fake.first_name_female()
    second_name = fake.last_name_female()
    middle_name = fake.middle_name_female()
    if gender == "male":
        first_name = fake.first_name_male()
        second_name = fake.last_name_male()
        middle_name = fake.middle_name_male()
        
    birth_date = fake.date_of_birth(minimum_age=1,maximum_age=35)
    
    unique_value = uuid4().hex[:10]
    coins = str(uuid4().int)[:3]
    return {
        "login": f"{fake.user_name().replace('_', '').replace('.', '')}{unique_value}",
        "password": fake.password(length=12),
        
        'role': choice(["TEACHER", "STUDENT", "ADMIN"]) , # Тут через рандом дополнить роли
        'first_name': first_name,
        'last_name': second_name,
        'middle_name': middle_name,
        "email": f"user_{unique_value}@{fake.free_email_domain()}",
        'date_of_birth': birth_date.isoformat(),
        "balance_coins": f"{coins}",
    }
    
    
def build_teacher_data() -> dict[str, str]:
    user_data = build_user_data()
    user_data["role"] = "TEACHER"
    return user_data

def build_admin_data() -> dict[str, str]:
    user_data = build_user_data()
    user_data["role"] = "ADMIN"
    return user_data

def build_student_data() -> dict[str, str]:
    user_data = build_user_data()
    user_data["role"] = "STUDENT"
    return user_data
