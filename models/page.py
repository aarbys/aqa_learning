from typing import Generic, TypeVar, List
from dataclasses import dataclass

T = TypeVar('T')

@dataclass
class Page(Generic[T]):
    content: List[T]
    totalElements: int
    totalPages: int
    size: int
    number: int
    first: bool
    last: bool
    empty: bool
