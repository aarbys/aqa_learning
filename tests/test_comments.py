from api.comment_api import CommentApi
from models.comment import Comment
import pytest

def test_get_comment_by_id(comment_api: CommentApi):
    comment_id = 1
    api_result = comment_api.get_comment_by_id(comment_id)

    assert isinstance(api_result.data,Comment)

    assert api_result.data.id == comment_id

    assert api_result.data.postId is not None
    assert api_result.data.name is not None
    assert api_result.data.email is not None
    assert api_result.data.body is not None


def test_get_all_comments(comment_api: CommentApi):
    api_result = comment_api.get_all_comments()

    assert isinstance(api_result.data, list)
    assert len(api_result.data) > 0

    for comment in api_result.data:
        assert isinstance(comment, Comment)
        assert comment.id is not None
        assert comment.postId is not None
        assert comment.name is not None
        assert comment.email is not None
        assert comment.body is not None


def test_create_comment(comment_api: CommentApi):
    comment_data = {
        "postId": 1,
        "name": "Test Comment",
        "email": "arbyz@gmail.com",
        "body": "This is a test comment."
    }
    api_result = comment_api.create_comment(comment_data)

    assert isinstance(api_result.data, Comment)
    assert api_result.data.postId == comment_data["postId"]
    assert api_result.data.name == comment_data["name"]
    assert api_result.data.email == comment_data["email"]
    assert api_result.data.body == comment_data["body"]

    assert api_result.data.id is not None
    assert isinstance(api_result.data.id, int)
    assert api_result.data.id > 0