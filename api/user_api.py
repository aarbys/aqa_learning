from api.generic_api import GenericApi

from models.user import User
from api.api_result import ApiResult

class UserApi:
    def __init__(self, generic_api: GenericApi):
        self.generic_api = generic_api

    def get_user_by_id(self, user_id: int) -> ApiResult[User]:
        return self.generic_api.get_by_id(user_id)

    def get_all_users(self) -> ApiResult[list[User]]:
        return self.generic_api.get_all()

    def create_user(self, user_data: dict) -> ApiResult[User]:

        return self.generic_api.create(user_data)

