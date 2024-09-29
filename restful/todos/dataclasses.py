from dataclasses import dataclass
from typing import Optional, List
from datetime import date




@dataclass
class CreateTodo:
    title: str
    description: str

@dataclass
class UpdateTodo:
    title: str
    description: str
