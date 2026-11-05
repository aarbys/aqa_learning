from api.user_api import UserApi
from models.user import User
from tests.assertions import (
    assert_models_equal, 
    assert_valid_id,
    assert_status, 
    assert_error_type,
    assert_message
    )

from uuid import uuid4
from datetime import date
from tests.factories.user_factory import build_user_data

import pytest


@pytest.mark.parametrize(
            "user_data",
    [
        (
            { # Correct person
            "login": "User1",
            "password": 'aboba',
            'role': "ADMIN",
            'first_name': "Aboba",
            'last_name': "Aboba",
            'middle_name': "Aboba",
            "email": "user_1@example.com",
            'date_of_birth': "2026-10-19",
            "coins": 12
            }
        )
    ]
)
def test_create_user_positive(user_data, user_api: UserApi):
    
    api_result = user_api.create_user(user_data)
    expected_user = User(**user_data)
    assert_status(
        status_code=api_result.response.status_code,
        expected_status_code=201
    )
    
    assert_models_equal(model=api_result.data,
                        expected_model=expected_user,
                        ignore_fields=set(["password",'coins','id','date_of_birth']))

    assert_valid_id(api_result.data.id)
    




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
def test_create_user_with_empty_values(field, value, expected_message ,user_api:UserApi):
    
    user_data = build_user_data()
    
    user_data[field] = value
    api_result = user_api.create_user(user_data)

    assert_status(
        status_code=api_result.response.status_code,
        expected_status_code=400
    )
    error = api_result.response.json()["code"]
    msg = api_result.response.json()["message"]
    
    assert_error_type(error_type=error,expected_error_type='ERROR')
    assert_message(expected_message=expected_message,
                   fact_message=msg)


@pytest.mark.parametrize(
    'field, value, expected_message',
    [
        ('login', 'asd_1', 'Invalid format of login')
        
        ,('first_name', 'string_1', 'Invalid format of first name')
        
        ,('first_name', 'string_1', 'Invalid format of last name')
        
        ,('middle_name', 'string_1', 'Invalid format of middle name')
        
        ,('email', 'ASD', 'Invalid email format')
        
        ,('date_of_birth' , '2026-02-29', '???')
        ,('date_of_birth' , '2026-06-31', '???')
    ],
)
def test_create_user_with_invalid_values(field, value, expected_message ,user_api:UserApi):
    
    user_data = build_user_data()
    
    user_data[field] = value
    api_result = user_api.create_user(user_data)

    assert_status(
        status_code=api_result.response.status_code,
        expected_status_code=400
    )
    error = api_result.response.json()["code"]
    msg = api_result.response.json()["message"]
    
    assert_error_type(error_type=error,expected_error_type='ERROR')
    assert_message(expected_message=expected_message,
                   fact_message=msg)



@pytest.mark.parametrize(
    'duplicate_field, expected_status',
    [
        ('login', 400)
        ,('password', 201)
        ,('role', 201)
        ,('first_name', 201)
        ,('last_name', 201)
        ,('middle_name', 201)
        ,('email', 400)
        ,('date_of_birth', 201)
    ],
)
def test_create_user_duplicate_data(duplicate_field, expected_status, user_api: UserApi):
    user_data_1 = build_user_data()
    base_user = user_api.create_user(user_data_1)
    assert_status(
        status_code=base_user.response.status_code,
        expected_status_code=201
    )
    
    user_data_2 = build_user_data()
    user_data_2[duplicate_field] = user_data_1[duplicate_field]


    api_result = user_api.create_user(user_data_2)
    
    assert_status(
        status_code=api_result.response.status_code,
        expected_status_code=expected_status
    )
