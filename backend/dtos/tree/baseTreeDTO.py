from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from helpers.enums.sex_enum import SexEnum


class BaseTreeDTO(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    surname: Optional[str]
    motherSurname: Optional[str]
    dateOfBirth: Optional[datetime]
    placeOfBirth: Optional[str]
    dateOfMarry: Optional[datetime]
    dateOfDeath: Optional[datetime]
    placeOfDeath: Optional[str]
    reasonOfDeath: Optional[str]
    sex: Optional[SexEnum]

    class Config:
        use_enum_values = True
