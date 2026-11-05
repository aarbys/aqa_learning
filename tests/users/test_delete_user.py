from api.user_api import UserApi
from models.user import User
from tests.assertions import (
    assert_status,
    assert_is_none
    )

from uuid import uuid4

import pytest



def test_delete_valid_user(create_user,user_api: UserApi):
    user = create_user("STUDENT")
    
    api_result = user_api.delete_user(user.id)
    assert_status(
        status_code=api_result.response.status_code,
        expected_status_code=200
    )
    

@pytest.mark.parametrize(
    "user_id",
    [
        (-1),
        (1000),
        ("123"),
    ]

)
def test_delete_invalid_user(user_id,user_api: UserApi):

    api_result = user_api.delete_user(user_id)
    
    assert_status(api_result.response.status_code,400)
    assert_is_none(api_result.data)