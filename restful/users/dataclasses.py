from dataclasses import dataclass
from typing import Optional, List
from datetime import date




@dataclass
class CreateUser:
    username: str
    password: str

@dataclass
class UpdateUser:
    username: str
    password: str
