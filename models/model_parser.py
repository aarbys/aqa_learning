from dataclasses import fields
from typing import TypeVar



T = TypeVar("T")

class ModelParser:
    @staticmethod
    def parse(data: dict, model: type[T], list_key: str | None = None, inner_model: type | None = None) -> T:
        model_fields = {
            field.name
            for field in fields(model)
        }

        filtered_data = {
            key: value
            for key, value in data.items()
            if key in model_fields
        }

        if inner_model:
            raw_data = data[list_key]
            filtered_data[list_key] = [
                ModelParser.parse(item, model=inner_model) for item in raw_data
            ]
        
        return model(**filtered_data)