from typing import TypeVar, Generic, Any
from api.api_client import ApiClient
from api.api_result import ApiResult
from models.model_parser import ModelParser

T = TypeVar("T")

class GenericApi(Generic[T]):
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
        response = self.client.get(self.endpoint, entity_id)
        model = None
        
        if 200<=response.status_code <300:
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
    
    def update(self, item_id : int|str, data: dict) -> ApiResult[T]:
        response = self.client.put(self.endpoint,
                                   item_id, data=data)
        model = None
        
        if 200<=response.status_code <300:
            model = ModelParser.parse(
                response.json(),
                self.model
            )
        return ApiResult(
            response=response,
            data=model
        )
    
    def delete(self, item_id: int | str) -> ApiResult[T]:
        response = self.client.delete(self.endpoint, item_id)
        model = None
        
        if 200<=response.status_code <300:
            try:
                model = ModelParser.parse(
                    response.json(),
                    self.model
                    )
            except Exception as e:
                model = None
                
        
        return ApiResult(
            response=response,
            data=model
            )
        
    def create(self, data: dict) -> ApiResult[T]:
        response = self.client.post(self.endpoint, data=data)
        model = None
        
        if 200<=response.status_code <300:
            model = ModelParser.parse(
                response.json(),
                self.model
            )
        

        return ApiResult(
            response=response,
            data=model
        )
        
    def get_page(self, sub_endpoint: str, params: dict, list_key: str, inner_model: type) -> ApiResult[T]:
        response = self.client.get(self.endpoint, sub_endpoint, params=params)
        model = None
        
        if 200<=response.status_code <300:
            model = ModelParser.parse(
                response.json(),
                self.model,
                list_key=list_key,
                inner_model=inner_model
            )
        

        return ApiResult(
            response=response,
            data=model
        )