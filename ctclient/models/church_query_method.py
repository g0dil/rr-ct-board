from enum import Enum


class ChurchQueryMethod(str, Enum):
    CHURCHQUERY = "ChurchQuery"

    def __str__(self) -> str:
        return str(self.value)
