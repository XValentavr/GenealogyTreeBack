from enum import Enum


class StatusEnum(Enum):
    IN_PROCESS = 'В процесі'
    DONE = 'Зроблено'
    CHECKING = 'На перевірці'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
