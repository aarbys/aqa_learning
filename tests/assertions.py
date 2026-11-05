from dataclasses import fields, is_dataclass


from typing import TypeVar

T = TypeVar("T")

def assert_models_equal(model:T,
                        expected_model: T, 
                        ignore_fields:set[str]|None = None) -> None:
    ignore_fields = ignore_fields or set()
    
    
    assert is_dataclass(model), "Not a dataclass"
    
    for field in fields(model):  
        if field.name in ignore_fields:
            continue
        expected = getattr(expected_model,field.name)
        actual = getattr(model,field.name)
        assert expected == actual, f"Field: {field.name}\nexpected:{expected}\nactual{actual}"





def assert_status(status_code: int, 
                  expected_status_code:int) -> None:
    assert status_code == expected_status_code, \
    f"Incorrect status code. Expected: {expected_status_code}\nActual: {status_code}"
    
    
    
    
def assert_model_list(api_result:list[T],
                      expected_model:type[T]) -> None:
    assert isinstance(api_result, list)
    assert len(api_result) > 0, \
        'Empty data'
    
    for model in api_result:
        assert isinstance(model, expected_model)
        assert is_dataclass(model), "Not a dataclass"
        
        for field in fields(model):
            assert getattr(model, field.name) is not None


def assert_valid_id(result_id) -> None:
    assert isinstance(result_id, int)
    assert result_id > 0


def assert_error_type(error_type,expected_error_type) -> None:
    assert error_type.lower() == expected_error_type.lower()
    
    
    
def assert_is_none(data):
    assert data is None, f"Returned data is {data}\nExpected NONE"

def assert_is_not_none(data):
    assert data is not None, f"Returned data is {data}\nExpected not NONE"


def assert_message(expected_message, fact_message):
    assert expected_message.lower() == fact_message.lower(), \
        f"Field: Response message\nexpected:{expected_message}\nactual{fact_message}"
        
        
def assert_size(actual_size, expected_size):
     assert actual_size == expected_size, \
            f"Field: Wrong size response\nexpected:{expected_size}\nactual: {actual_size}"
            
def assert_page(actual_page, expected_page):
     assert actual_page == expected_page, \
            f"Field: Wrong page response\nexpected:{expected_page}\nactual: {actual_page}"

def assert_is_empty(data):
    assert getattr(data, "empty") is False, "Список учителей пуст"
    