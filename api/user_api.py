from api.generic_api import GenericApi

from models.user import User, TeacherDTO, StudentDTO
from models.page import Page
from api.api_result import ApiResult

class UserApi:
    def __init__(self, user_generic_api: GenericApi, page_generic_api: GenericApi):
        self.user_generic_api = user_generic_api
        self.page_generic_api = page_generic_api

    def get_user_by_id(self, user_id: int) -> ApiResult[User]:
        return self.user_generic_api.get_by_id(user_id)

    def get_all_users(self) -> ApiResult[list[User]]:
        return self.user_generic_api.get_all()

    def create_user(self, user_data: dict) -> ApiResult[User]:
        return self.user_generic_api.create(user_data)

    def update_user(self, user_id: int | str, user_data: dict) -> ApiResult[User]:
        return self.user_generic_api.update(item_id=user_id, 
                                       data=user_data)
    def delete_user(self, user_id: int | str) -> ApiResult[User]:
        return self.user_generic_api.delete(item_id=user_id)
    
    def get_teachers(self, **kwargs) -> ApiResult[Page[TeacherDTO]]:
        query_params = {
            "page": 0,
            "size": 20,
            "sortBy": 'secondName',
            "sortDir":'asc'
        }
        query_params.update(kwargs)
        return self.page_generic_api.get_page(
            sub_endpoint="teachers",
            params=query_params,
            list_key="content",
            inner_model=TeacherDTO
            )
        
        
    def get_students(self, **kwargs) -> ApiResult[Page[TeacherDTO]]:
        query_params = {
            "page": 0,
            "size": 20,
            "sortBy": 'secondName',
            "sortDir":'asc'
        }
        query_params.update(kwargs)
        return self.page_generic_api.get_page(
            sub_endpoint="students",
            params=query_params,
            list_key="content",
            inner_model=StudentDTO
            )