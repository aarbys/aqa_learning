from __future__ import annotations
from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    email: str

    # @classmethod
    # def from_dict(cls, data: dict) -> User:
    #     return cls(**data
    #     )