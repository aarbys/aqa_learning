from __future__ import annotations
from dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str
    phone: str
    id: int | None = None
    # @classmethod
    # def from_dict(cls, data: dict) -> User:
    #     return cls(**data
    #     )