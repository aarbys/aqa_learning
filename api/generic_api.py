from typing import TypeVar
from api.api_client import ApiClient
from api.api_result import ApiResult

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
        model = self.model.from_dict(
            response.json()
        )

        return ApiResult(
            response=response,
            data=model
        )


    def get_all(self) -> ApiResult[list[T]]:
        response = self.client.get(self.endpoint)
        models = [self.model.from_dict(result)
                  for result in self.client.get(self.endpoint).json()
                  ]

        return ApiResult(
            response=response,
            data=models
        )
    
    def create(self, data: dict) -> ApiResult[T]:
        response = self.client.post(self.endpoint, data=data)
        model = self.model.from_dict(response.json())

        return ApiResult(
            response=response,
            data=model
        )