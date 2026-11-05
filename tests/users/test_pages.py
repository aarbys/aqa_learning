from api.user_api import UserApi
from models.user import TeacherDTO
from tests.assertions import (
    assert_models_equal,
    assert_status,
    assert_is_none,
    assert_is_not_none,
    assert_size,
    assert_page,
    assert_is_empty,
    assert_valid_id
    )
from dataclasses import asdict
from faker import Faker


import pytest


fake = Faker('ru_RU')
SPRING_DEFAULT_PARAMS = {
    "page": 0,
    "size": 20,
    "sortBy": "secondName",
    "sortDir": "asc"
}

@pytest.mark.parametrize(
    'api_method_name,role, query_params',
    [
        ("get_teachers","TEACHER", {"page":1}),
        ("get_teachers","TEACHER", {"size":10000}),
        ("get_teachers","TEACHER", {"sortDir":"desc"}),
        ("get_teachers","TEACHER", {"sortBy":"id"}),
        ("get_teachers","TEACHER", {"sortBy":"login"}),
        ("get_teachers","TEACHER", {"sortBy":"firstName"}),
        ("get_teachers","TEACHER", {"sortBy":"patronymicName"}),
        ("get_teachers","TEACHER", {"sortBy":"email"}),
        ("get_teachers","TEACHER", {"sortBy":"birthDate"}),
        
        ("get_students","STUDENT", {"page":1}),
        ("get_students","STUDENT", {"size":10000}),
        ("get_students","STUDENT", {"sortDir":"desc"}),
        ("get_students","STUDENT", {"sortBy":"id"}),
        ("get_students","STUDENT", {"sortBy":"login"}),
        ("get_students","STUDENT", {"sortBy":"firstName"}),
        ("get_students","STUDENT", {"sortBy":"patronymicName"}),
        ("get_students","STUDENT", {"sortBy":"email"}),
        ("get_students","STUDENT", {"sortBy":"birthDate"}),
    ],
)
def test_get_page_list(api_method_name,role, query_params, create_user,user_api:UserApi):
    create_user(role)
    
    target_method = getattr(user_api, api_method_name)
    
    api_result = target_method(**query_params)
    
    assert_status(api_result.response.status_code, 200)
    assert_is_not_none(api_result.data)
    
    actual_size = getattr(api_result.data, "size")
    actual_page = getattr(api_result.data, "number")
    
    expected_size = query_params.get("size", SPRING_DEFAULT_PARAMS["size"])
    expected_page = query_params.get("page", SPRING_DEFAULT_PARAMS["page"])
    
    
    assert_size(actual_size,expected_size)
    assert_page(actual_page,expected_page)


@pytest.mark.parametrize(
    'api_method_name, role',
    [
        ("get_teachers","TEACHER"),
        ("get_students","STUDENT"),
    ],
)
def test_get_page_data(api_method_name, role, create_user,user_api:UserApi):
    user = create_user(role)
    
    target_method = getattr(user_api, api_method_name)
    
    query_params = {
            "page": 0,
            "size": 1,
            "sortBy": 'id',
            "sortDir":'desc'
        }
    
    api_result = target_method(**query_params)
    
    assert_status(api_result.response.status_code,200)
    assert_is_not_none(api_result.data)
    
    page_data = api_result.data
    
    assert_is_empty(page_data)
    
    users_list = getattr(page_data, "content")
    structure_dto = next((u for u in users_list if getattr(u, "id") == user.id), None)
    assert_is_not_none(structure_dto)
    
    assert_valid_id(structure_dto.id) # type: ignore
    
    assert_models_equal(structure_dto, user ,
                        ("fullName")) # type: ignore


@pytest.mark.parametrize(
    'api_method_name, query_params',
    [
        ("get_teachers", {"page":-1}),
        ("get_teachers", {"size":-1}),
        ("get_teachers", {"sortDir":"id"}),
        ("get_teachers", {"sortBy":"sasdasddsa"}),
        
        ("get_students", {"page":-1}),
        ("get_students", {"size":-1}),
        ("get_students", {"sortDir":"id"}),
        ("get_students", {"sortBy":"sasdasddsa"}),
    ],
)
def test_get_page_with_invalid_args(api_method_name, query_params, create_user, user_api:UserApi):
    target_method = getattr(user_api, api_method_name)
    query_params_data = {
            "page": 0,
            "size": 1,
            "sortBy": 'asd',
            "sortDir":'desc'
        }
    query_params_data.update(**query_params)
    
    api_result = target_method(**query_params_data)
    assert_status(api_result.response.status_code,400)


@pytest.mark.parametrize(
    'api_method_name',
    [
        ("get_teachers"),
        ("get_students"),
    ],
)

def test_get_teacher_with_invalid_query(api_method_name, create_user, user_api:UserApi):
    query_params = {"invalid_data":"str"}
    
    target_method = getattr(user_api, api_method_name)
    
    api_result = target_method(**query_params)
    
    assert_status(api_result.response.status_code, 400)

