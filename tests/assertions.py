from dataclasses import fields  


from typing import TypeVar

T = TypeVar("T")

def assert_models_equal(model:T, expected_model: T, ignore_fields:set[str]|None = None):
    ignore_fields = ignore_fields or set()
    for field in fields(model):  
        if field.name in ignore_fields:
            continue
        expected = getattr(expected_model,field.name)
        actual = getattr(model,field.name)
        assert expected == actual, f"Field: {field.name}\nexpected:{expected}\nactual{actual}"





def assert_status(api_result: T, expected_status_code:int):
    assert api_result.response.status_code == expected_status_code, \
    f"Incorrect status code. Expected: {expected_status_code}\nActual: {api_result.response.status_code}"
    
    
    
def assert_model_list(api_result,expected_model:T):
    assert isinstance(api_result, list)
    assert len(api_result) > 0, \
        'Empty data'
    
    for model in api_result:
        assert isinstance(model, expected_model)
        for field in fields(model):
            assert getattr(model, field.name) is not None


def assert_valid_id(result_id):
    assert isinstance(result_id, int)
    assert result_id > 0
