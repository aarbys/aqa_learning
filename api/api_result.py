from dataclasses import dataclass
from typing import Generic, TypeVar

from requests import Response

T = TypeVar('T')

@dataclass
class ApiResult(Generic[T]):
    response: Response
    data: T | None