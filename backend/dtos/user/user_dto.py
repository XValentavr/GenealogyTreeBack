from typing import Optional

from pydantic import BaseModel, Field

from helpers.enums.sex_enum import SexEnum


class UserUpdateDto(BaseModel):
    userName: Optional[str] = Field(alias='userName')
    last_name: Optional[str] = Field(alias='lastName')
    avatar: Optional[str] = Field(alias='avatar')
    telegram: Optional[str] = Field(alias='telegram')
    facebook: Optional[str] = Field(alias='facebook')
    linkedin: Optional[str] = Field(alias='linkedin')
    whatsapp: Optional[str] = Field(alias='whatsapp')
    twitter: Optional[str] = Field(alias='twitter')
    photoUrl: Optional[str] = Field(alias='photoUrl')
    email: Optional[str] = Field(alias='email')
    sex: Optional[SexEnum] = Field(alias='sex')
