from __future__ import annotations
from dataclasses import dataclass


@dataclass
class BaseModel:
    id: int
    title: str
    body: str


    @classmethod
    def from_dict(cls, data: dict) -> BaseModel:
        return cls(
            id = data["id"],
            title = data["title"],
            body = data["body"]
        )