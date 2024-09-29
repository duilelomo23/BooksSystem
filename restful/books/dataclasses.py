from dataclasses import dataclass
from typing import Optional, List
from datetime import date



#判斷sql傳入型別
@dataclass
class CreateBooks:
    title: str
    author: str
    year : Optional[int] = None


    
@dataclass
class UpdateBooks:
    title: str
    author: str
    year : Optional[int] = None
