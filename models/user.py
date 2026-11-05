from __future__ import annotations
from dataclasses import dataclass

@dataclass
class User:
    login: str
    role: str
    first_name: str
    last_name: str
    middle_name: str
    email: str
    
    
    date_of_birth: str | None = None
    coins : int | None = None
    password: str| None = None
    id: int | None = None

@dataclass
class TeacherDTO:
    id: int
    fullName: str
    login: str
        
        
@dataclass
class StudentDTO:
    id: int
    fullName: str
    login: str
    date_of_birth: str
    coins: str