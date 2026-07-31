from api.user_api import UserApi
from models.user import User
from tests.assertions import (
    assert_models_equal,
    assert_status,
    assert_is_none
    )

from uuid import uuid4

import pytest



def test_get_valid_person(created_user, user_api: UserApi):
    
    user = created_user
    api_result = user_api.get_user_by_id(user.id)
    
    
    assert_status(api_result.response.status_code,200)
    assert_models_equal(api_result.data,user)



@pytest.mark.parametrize(
            "user_id, excepted_status",
    [
        (-1,404),
        (1000,404),
        ("123",404),
    ]

)
def test_get_invalid_person(user_id,excepted_status, user_api: UserApi):
    api_result = user_api.get_user_by_id(user_id)
    assert_status(api_result.response.status_code,excepted_status)
    assert_is_none(api_result.data)
    
