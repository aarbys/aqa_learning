import pytest

from api.user_api import UserApi
from api.api_client import ApiClient
from api.comment_api import CommentApi
from api.generic_api import GenericApi


from models.user import User

@pytest.fixture
def api_client() -> ApiClient:
    return ApiClient()

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
def comment_api(api_client: ApiClient) -> CommentApi:
    return CommentApi(client=api_client)

