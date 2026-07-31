import pytest

from api.user_api import UserApi
from api.api_client import ApiClient
from api.generic_api import GenericApi
from tests.factories.user_factory import build_user_data

from models.user import User

@pytest.fixture
def api_client() -> ApiClient:
    return ApiClient(timeout=15)

@pytest.fixture
def user_generic_api(api_client: ApiClient) -> GenericApi:

    return GenericApi(
        client=api_client,
        endpoint="users",
        model=User
    )

@pytest.fixture
def user_api(user_generic_api: GenericApi) -> UserApi:
    return UserApi(generic_api=user_generic_api)




@pytest.fixture
def created_user(user_api: UserApi):
    user_data = build_user_data()

    api_result = user_api.create_user(user_data)

    
    
    assert api_result.response.status_code == 201, (
        f"Status: {api_result.response.status_code}\n"
        f"Response: {api_result.response.text}\n"
        f"Request data: {user_data}"
    )
    assert api_result.data is not None
    assert api_result.data.id is not None
    
    yield api_result.data

    # user_api.delete_user(api_result.data.id)