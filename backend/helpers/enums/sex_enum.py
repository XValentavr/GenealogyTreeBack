from enum import Enum


class SexEnum(Enum):
    MALE = 'М'
    FEMALE = 'Ж'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
