import requests
from requests import Response

from config import BASE_URL
from typing import TypeVar

T = TypeVar("T")

class ApiClient:
    def __init__(self, token: str | None = None, 
                 base_url: str = BASE_URL, 
                 timeout: int = 30):
        self.base_url = base_url
        self.headers = {}
        self.timeout = timeout

        if token:
            self.headers["Authorization"] = f"Bearer {token}"
    
    def build_url(self, endpoint: str, *url_parts: str | int) -> str:
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        if url_parts:
            additional_path = "/".join(str(part) for part in url_parts)
            url = f"{url}/{additional_path}"
        return url


    def get(self, endpoint:str, *url_parts: str| int, params: dict | None = None) -> Response:
        response = requests.get(
            self.build_url(endpoint, *url_parts),
            headers=self.headers,
            params=params,
            timeout=self.timeout,
        )
        return response
    
    
    def post(self, endpoint:str, *url_parts: str| int, data: dict) -> Response:
        response = requests.post(
            self.build_url(endpoint, *url_parts),
            headers=self.headers,
            json=data,
            timeout=self.timeout,
        )
        return response
    
    def put(self,endpoint:str, *url_parts: str| int, data:dict) -> Response:
        response = requests.put(
            self.build_url(endpoint, *url_parts),
            headers=self.headers,
            json=data,
            timeout=self.timeout,
        )
        return response
    
    def delete(self,endpoint: str, *url_parts: str| int) -> Response:
        response = requests.delete(
            self.build_url(endpoint, *url_parts),
            headers=self.headers,
            timeout=self.timeout,
        )
        return response