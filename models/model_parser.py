from dataclasses import fields
from typing import TypeVar



T = TypeVar("T")

class ModelParser:
    @staticmethod
    def parse(data: dict, model: type[T]) -> T:
        model_fields = {
            field.name
            for field in fields(model)
        }

        filtered_data = {
            key: value
            for key, value in data.items()
            if key in model_fields
        }

        return model(**filtered_data)