from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Product:
    id: int
    title: str
    body: str


    # @classmethod
    # def from_dict(cls, data: dict) -> Product:
    #     return cls(**data
    #     )