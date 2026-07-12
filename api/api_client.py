import requests
from requests import Response

from config import BASE_URL
from typing import TypeVar

T = TypeVar("T")

class ApiClient:
    def __init__(self, token: str | None = None, 
                 base_url: str = BASE_URL, 
                 timeout: int = 5):
        self.base_url = base_url
        self.headers = {}
        self.timeout = timeout

        if token:
            self.headers["Authorization"] = f"Bearer {token}"
    
    def build_url(self, endpoint: str) -> str:
        return f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"

    def get(self, endpoint:str) -> Response:
        response = requests.get(
            self.build_url(endpoint),
            headers=self.headers,
            timeout=self.timeout,
        )
        return response
    
    def post(self, endpoint:str, data: dict) -> Response:
        response = requests.post(
            self.build_url(endpoint),
            headers=self.headers,
            json=data,
            timeout=self.timeout,
        )
        return response