from typing import Optional

from pydantic import BaseModel, Field


class UpdateProfileDTO(BaseModel):
    avatar: Optional[str]
    telegram: Optional[str]
    facebook: Optional[str]
    linkedin: Optional[str]
    whatsapp: Optional[str]
    twitter: Optional[str]
    avatar: Optional[str]
