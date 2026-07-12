from dataclasses import dataclass
from typing import Generic, TypeVar

from requests import Response

T = TypeVar('T')

@dataclass
class ApiResult(Generic[T]):
    response: Response
    data: T
    def __init__(self, status_code: int, data: T):
        self.status_code = status_code
        self.data = data