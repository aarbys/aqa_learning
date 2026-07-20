from api.user_api import UserApi
from models.user import User
from tests.assertions import (
    assert_models_equal, 
    assert_valid_id,
    assert_status, 
    assert_error_type
    )

from uuid import uuid4

import pytest


@pytest.mark.parametrize(
            "user_data",
    [
        (
            { # Correct person
            "name": "Arbuz",
            "email": "Arbuz1@example.com",
            "phone": "+123123"
            })
    ]
)
def test_create_user_positive(user_data, user_api: UserApi):
    
    api_result = user_api.create_user(user_data)
    
    expected_user = User(
                         name=user_data["name"],
                         email=user_data["email"].lower(),
                         phone=user_data["phone"]
                         )
    
    assert_status(
        status_code=api_result.response.status_code,
        expected_status_code=201
    )
    
    assert_models_equal(model=api_result.data,
                        expected_model=expected_user,
                        ignore_fields=set(["id"]))

    assert_valid_id(api_result.data.id)
    
    
@pytest.mark.parametrize(
            "user_data, expected_status, expected_error_type",
    [       
        
        (
            { # Name - Integer instead of string
            "name": 1212,
            "email": "Arbuz2@example.com",
            "phone": "+123123"
            },422,"string_type"),
        
        (
            { # email - Integer instead of string
            "name": "1212",
            "email": 123123,
            "phone": "+123123"
            },422,"string_type"),
        
        (
            { # phone - Integer instead of string
            "name": "1212",
            "email": "Arbuz3@example.com",
            "phone": 123123
            },422,"string_type"),
        
        (
            { # Wrong field name
            "name": "Arbuz",
            "email": "Arbuz4@example.com",
            "salary": "123123123",
            "phone": "+1232"
            },422,"extra_forbidden"),

        (
            { # Person have no phone number
            "name": "123",
            "email": "Arbuz5@example.com"
            },422,"missing"),
        (
            { # Person have no email
            "name": "Arbuz",
            "phone": "+123123"
            },422,"missing"),
        (
            { # Person have no name
            "email": "Arbuz6",
            "phone": "+123123"
            },422,"missing"),      
        
        (
            { # Field ID in request
            "id": 2,
            "name": "1212",
            "email": "Arbuz91@example.com",
            "phone": "+123123"
            },422,"extra_forbidden"),
        (
            { # Name - too long
            "name": "a"*51,
            "email": "Arbuz2@example.com",
            "phone": "+123123"
            },422,"string_too_long"),
        (
            { # Name - too short
            "name": "a",
            "email": "Arbuz2@example.com",
            "phone": "+123123"
            },422,"string_too_short"),
        (
            { # phone - too short
            "name": "a"*12,
            "email": "Arbuz2@example.com",
            "phone": "1"
            },422,"string_too_short"),
        (
            { # phone - too long
            "name": "a"*12,
            "email": "Arbuz2@example.com",
            "phone": "+" + "1"*21
            },422,"string_too_long"),
        
        
    ]
)
def test_create_user_negative(user_data,expected_status, expected_error_type, user_api: UserApi):
    
    api_result = user_api.create_user(user_data)
    
    assert_status(
        status_code=api_result.response.status_code,
        expected_status_code=expected_status
    )
    
    error = api_result.response.json()["detail"][0]
    assert_error_type(error["type"], expected_error_type)
     


@pytest.mark.parametrize(
     "user_data",
    [       
        
        (
            { # Name - 2 symbols
            "name": "12",
            "email": "User_1@example.com",
            "phone": "+123123"
            }),
        (
            { # Name - 50 symbols
            "name": "9"*50,
            "email": "User_2@example.com",
            "phone": "+123123"
            }),
        (
            { # Phone - 5 symbols
            "name": "123",
            "email": "User_3@example.com",
            "phone": "+" + "9"*4
            }),
        (
            { # Phone - 20 symbols
            "name": "123",
            "email": "User_4@example.com",
            "phone": "+" + "9"*19
            }),
    ]   
)
def test_create_user_with_valid_boundary_values(user_data, user_api: UserApi):
    api_result = user_api.create_user(user_data)
    
    expected_user = User(
                         name=user_data["name"],
                         email=user_data["email"].lower(),
                         phone=user_data["phone"]
                         )
    
    assert_status(
        status_code=api_result.response.status_code,
        expected_status_code=201
    )
    
    assert_models_equal(model=api_result.data,
                        expected_model=expected_user,
                        ignore_fields=set(["id"]))

    assert_valid_id(api_result.data.id)



@pytest.mark.parametrize(
    "duplicate_field, expected_status",
    [
        (# Email not unique
            "email",
            409),
        ( # Phone not unique
            "phone",
            201)
    ]
)
def test_create_user_duplicate_data(duplicate_field,expected_status, user_api: UserApi):
    unique_value = uuid4().hex
    
    
    base_user_data = {
            "name":"First user",
            "email": f"base-{unique_value}@example.com",
            "phone": f"+7{str(uuid4().int)[:10]}",
        }
    
    duplicate_user_data = {
        "name": "Second user",
        "email": f"second-{unique_value}@example.com",
        "phone": f"+7{str(uuid4().int)[:10]}",
    }
    
    base_user = user_api.create_user(
        base_user_data
        )
    
    assert_status(
        status_code=base_user.response.status_code,
        expected_status_code=201
    )
    

    duplicate_user_data[duplicate_field] = base_user_data[duplicate_field]

    api_result = user_api.create_user(duplicate_user_data)
    
    assert_status(
        status_code=api_result.response.status_code,
        expected_status_code=expected_status
    )
