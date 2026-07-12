from api.user_api import UserApi
from models.user import User
import pytest

def test_get_user_by_id(user_api: UserApi):
    api_result = user_api.get_user_by_id(1)

    assert api_result.data.id == 1
    assert api_result.data.name == "Leanne Graham"
    assert api_result.data.email == "Sincere@april.biz"


def test_get_unknown_user(user_api: UserApi):
    api_result = user_api.get_user_by_id(999)
    assert api_result.response.status_code == 404

    assert api_result.data is None




def test_create_new_user(user_api: UserApi):
    user_data = {
        "name": "Arbuz",
        "email": "Arbuz@example.com"
    }
    api_result = user_api.create_user(user_data)
    
    assert api_result.data is not None
    assert api_result.data.name == user_data["name"]
    assert api_result.data.email == user_data["email"]

    assert api_result.data.id is not None
    assert isinstance(api_result.data.id, int)
    assert api_result.data.id > 0


def test_get_all_users(user_api: UserApi):
    api_result = user_api.get_all_users()

    assert isinstance(api_result.data, list)
    assert len(api_result.data) > 0

    for user in api_result.data:
        assert isinstance(user, User)
        assert user.id is not None
        assert user.name is not None
        assert user.email is not None



@pytest.mark.parametrize(
            "user_data, expected_status",
    [
        (
            {
            "name": "Arbuz"
            }, 
            201),
        (
            {
            "name": 1212,
            "email": "Arbuz@example.com"
            }, 
            201),
        (
            {
            "name": "    ",
            "email": "Arbuz@example.com"
            }, 
            201),
        (
            {
            "name": "Arbuz",
            "email": "Arbuz@example.com",
            "salary": 500000
            }, 
            201),
        (
            {
            "name": "Arbuz",
            "email": "Arbuz"
            }, 
            201),
    ]


    )
def test_create_user_negative(user_data, expected_status, user_api: UserApi):
        api_result = user_api.create_user(user_data)
        assert api_result.response.status_code == expected_status
