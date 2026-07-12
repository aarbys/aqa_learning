


from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Comment:
    postId: int
    id: int
    name: str
    email: str
    body: str

    @classmethod
    def from_dict(cls, data: dict) -> Comment:
        return cls(**data
        )