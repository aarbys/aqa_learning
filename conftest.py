import pytest
from config import AUTH_TOKEN

from api.user_api import UserApi
from api.api_client import ApiClient
from api.generic_api import GenericApi
from tests.factories.user_factory import (
    build_user_data, 
    build_teacher_data,
    build_student_data
    )

from models.user import User
from models.page import Page




# 
@pytest.fixture
def generic_api_factory(api_client: ApiClient):
    def _create_api(endpoint: str, model: type):
        return GenericApi(client=api_client, endpoint=endpoint, model=model)
    return _create_api


@pytest.fixture
def api_client() -> ApiClient:
    client = ApiClient(timeout=15)
    client.headers["Authorization"] = AUTH_TOKEN
    return client




@pytest.fixture
def user_api(generic_api_factory) -> UserApi:
    user_generic_api = generic_api_factory(endpoint="users", model=User)
    page_generic_api = generic_api_factory(endpoint="users", model=Page)
    return UserApi(
        user_generic_api=user_generic_api,
        page_generic_api=page_generic_api
                   )

    
    
@pytest.fixture
def create_user(user_api: UserApi):
    created_idx = list()
    
    def _create(role:str | None = None):
        user_data = build_user_data()
        if role is not None:
            user_data['role'] = role.upper()
        api_result = user_api.create_user(user_data)
        
        assert api_result.response.status_code == 201, (
            f"Status: {api_result.response.status_code}\n"
            f"Response: {api_result.response.text}\n"
            f"Request data: {user_data}"
        )
        assert api_result.data is not None
        assert api_result.data.id is not None
        
        
        created_idx.append(api_result.data.id)
        return api_result.data
    
    yield _create
    
    for user in created_idx:
        user_api.delete_user(user)