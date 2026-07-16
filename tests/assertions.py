from dataclasses import fields  

from api.api_result import Response
from typing import TypeVar

T = TypeVar("T")

def assert_models_equal(model:T, expected_model: T, ignore_fields:list):
    for field in fields(model):  
        if field in ignore_fields:
            continue
        expected = getattr(expected_model,field.name)
        actual = getattr(model,field.name)
        assert expected == actual, f"Field: {field.name}\nexpected:{expected}\nactual{actual}"





def assert_status(api_result: type[T], expected_status_code:int):
    assert api_result.response.status_code == expected_status_code, \
    f"Incorrect status code. Expected: {expected_status_code}\nActual: {api_result.response.status_code}"
    
    
    
def assert_model_list(api_result:type[T],expected_model:T):
    assert isinstance(api_result.data, list)
    assert len(api_result.data) > 0, \
        'Empty data'
    
    for model in api_result.data:
        assert isinstance(model, expected_model)
        assert model.id is not None
        assert model.name is not None
        assert model.email is not None


def assert_valid_id(api_result:type[T]):
    assert isinstance(api_result.data.id, int)
    assert api_result.data.id > 0
# (...)
# (...)
# assert_valid_id(...)