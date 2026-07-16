from typing import TypeVar
from api.api_client import ApiClient
from api.api_result import ApiResult
from models.model_parser import ModelParser

T = TypeVar("T")

class GenericApi:
    def __init__(
        self,
        client: ApiClient,
        endpoint: str,
        model: type[T],
    ):
        self.client = client
        self.endpoint = endpoint
        self.model = model
    

    def get_by_id(self, entity_id: int) -> ApiResult[T]:
        response = self.client.get(f"{self.endpoint}/{entity_id}")
        model = ModelParser.parse(
            response.json(),
            self.model
        )

        return ApiResult(
            response=response,
            data=model
        )


    def get_all(self) -> ApiResult[list[T]]:
        response = self.client.get(self.endpoint)
        models = [
            ModelParser.parse(
                result ,
                self.model
            )
            for result in response.json()
        ]
    

        return ApiResult(
            response=response,
            data=models
        )
    
    def create(self, data: dict) -> ApiResult[T]:
        response = self.client.post(self.endpoint, data=data)
        model = ModelParser.parse(
            response.json(),
            self.model
        )
        #self.model.from_dict(response.json())

        return ApiResult(
            response=response,
            data=model
        )