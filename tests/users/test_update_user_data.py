from api.user_api import UserApi
from models.user import User
from tests.assertions import (
    assert_models_equal,
    assert_status,
    assert_is_not_none,
    assert_message,
    assert_error_type
    )
from dataclasses import asdict
from typing import Any
from faker import Faker

import pytest


fake = Faker('ru_RU')
fake_en = Faker('en_US')

@pytest.mark.parametrize(
    'changed_field, new_value_factory',
    [
        ('login', lambda: fake.user_name().replace('_', '').replace('.', ''))
        ,('password', lambda:fake.password(length=12))
        ,('role', lambda: "STUDENT")
        ,('first_name', lambda :fake.first_name_female())
        ,('last_name', lambda: fake.last_name_female())
        ,('middle_name', lambda: fake.middle_name_female())
        ,('email', lambda: f'{fake_en.first_name().lower().replace("'", "")}_{fake_en.last_name().lower().replace("'", "")}@{fake.free_email_domain()}')
        ,('date_of_birth', lambda: fake.date_of_birth(minimum_age=1,maximum_age=35).isoformat())
    ],
)
def test_update_person_data(changed_field, new_value_factory, create_user, user_api: UserApi):
    user = create_user("STUDENT")
    api_result = user_api.get_user_by_id(user.id)
    
    assert_status(api_result.response.status_code,200)
    assert_models_equal(api_result.data,user)
    assert_is_not_none(api_result.data)
    
    new_value = new_value_factory()
    
    user_data = api_result.data 
    user_id = getattr(user_data, "id")
    
    user_data = prepare_user_data(pi_user_data=user_data, # type: ignore
                                  target_field=changed_field,
                                  target_value=new_value)
    
    updated_user = user_api.update_user(user_id, user_data)
    assert_status(updated_user.response.status_code,201)
    
    
@pytest.mark.parametrize(
    'field, value, expected_message',
    [
        ('login', None, 'Login cannot be empty')
        ,('login', ' ', 'Login cannot be empty')
        
        ,('password', None, 'rawpassword cannot be null')
        
        ,('first_name', ' ', 'First name cannot be empty')
        ,('first_name', None, 'First name cannot be empty')
        
        ,('last_name', ' ', 'Last name cannot be empty')
        ,('last_name', None, 'Last name cannot be empty')
        
        ,('email', ' ', 'email cannot be empty')
        ,('email', None, 'email cannot be empty')
        
        ,('date_of_birth' , None, 'birth date cannot be empty')
        ,('date_of_birth' , ' ', 'birth date cannot be empty')
    ],
)
def test_update_user_with_empty_values(field, value, expected_message, create_user,user_api:UserApi):
    user = create_user("STUDENT")
    api_result = user_api.get_user_by_id(user.id)
    
    assert_status(api_result.response.status_code,200)
    assert_models_equal(api_result.data,user)
    assert_is_not_none(api_result.data)
    
    user_data = api_result.data 
    user_id = getattr(user_data, "id")
    
    user_data = prepare_user_data(pi_user_data=user_data, # type: ignore
                                  target_field=field,
                                  target_value=value)

    updated_user = user_api.update_user(user_id, user_data)
    
    
    assert_status(updated_user.response.status_code, 400)
    error = updated_user.response.json()["code"]
    msg = updated_user.response.json()["message"]
    
    assert_error_type(error_type=error,expected_error_type='ERROR')
    assert_message(expected_message=expected_message,
                   fact_message=msg)
    
    
    
    
def prepare_user_data(pi_user_data: User, target_field: str, target_value: Any) -> dict:
    user_data = asdict(pi_user_data)
    
    user_data[target_field] = target_value
    
    if target_field != 'password':
            user_data['password'] = fake.password(length=12)
            
    user_data.pop('rank_level',None)
    user_data.pop('full_name',None)
    user_data.pop('id',None)
    user_data.pop('exp',None)
    
    return user_data