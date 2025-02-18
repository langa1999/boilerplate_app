from pydantic import BaseModel
from typing import List


class Laureate(BaseModel):
    id: str
    firstname: str
    surname: str
    motivation: str
    share: str


class Prize(BaseModel):
    year: str
    category: str
    laureates: List[Laureate]
