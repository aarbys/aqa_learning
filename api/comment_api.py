from api.generic_api import GenericApi

from models.comment import Comment
from api.api_result import ApiResult

class CommentApi:
    def __init__(self, generic_api: GenericApi):
        self.generic_api = generic_api

    def get_comment_by_id(self, comment_id: int) -> ApiResult[Comment]:
        return self.generic_api.get_by_id(comment_id)

    def get_all_comments(self) -> ApiResult[list[Comment]]:
        return self.generic_api.get_all()

    def create_comment(self, comment_data: dict) -> ApiResult[Comment]:
        return self.generic_api.create(comment_data)
