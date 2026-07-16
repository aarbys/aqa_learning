from api.user_api import UserApi
from models.user import User

from tests.assertions import assert_models_equal, assert_valid_id,assert_model_list,assert_status



import pytest

def test_get_user_by_id(user_api: UserApi):
    api_result = user_api.get_user_by_id(1)
    expected_user = User(
        id=1,
        name="Leanne Graham",
        email="Sincere@april.biz"
    )
        
    assert_status(api_result=api_result,
                  expected_status_code=200)

    assert_models_equal(model=api_result.data,
                        expected_model=expected_user)



# def test_get_unknown_user(user_api: UserApi):
#     api_result = user_api.get_user_by_id(999)
#     assert api_result.response.status_code == 404

#     assert api_result.data is None




def test_create_new_user(user_api: UserApi):
    user_data = {
        "name": "Arbuz",
        "email": "Arbuz@example.com"
    }
    api_result = user_api.create_user(user_data)
    
    expected_user = User(id=1, 
                         name=user_data["name"],
                         email=user_data["email"]
                         )

    assert_models_equal(model=api_result.data,
                        expected_model=expected_user,
                        ignore_fields=["id"])

    assert_valid_id(api_result.data.id)


def test_get_all_users(user_api: UserApi):
    api_result = user_api.get_all_users()
    assert_model_list(api_result=api_result.data,
                      expected_model=User)  


@pytest.mark.parametrize(
            "user_data, expected_status",
    [
        # (
            # {
            # "name": "Arbuz"
            # }, 
            # 201),
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
        expected_user = User(id=1,
                             name=user_data['name'],
                             email=user_data['email']
                             )      
        
        assert_status(api_result=api_result,expected_status_code=expected_status)
        assert_models_equal(api_result.data,
                            expected_user,["id"])