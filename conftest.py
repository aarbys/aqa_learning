import pytest

from api.user_api import UserApi
from api.api_client import ApiClient
from api.comment_api import CommentApi
from api.generic_api import GenericApi


from models.user import User
from models.comment import Comment

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
def comment_generic_api(api_client: ApiClient) -> GenericApi:
    return GenericApi(
        client=api_client,
        endpoint="comments",
        model=Comment
    )

@pytest.fixture
def comment_api(comment_generic_api: GenericApi) -> CommentApi:
    return CommentApi(generic_api=comment_generic_api)



