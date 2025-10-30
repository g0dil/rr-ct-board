from enum import Enum


class PostFactsBodyFieldType(str, Enum):
    NUMBER = "number"
    SELECT = "select"

    def __str__(self) -> str:
        return str(self.value)
