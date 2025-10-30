from enum import Enum


class PutFactsIdBodyFieldType(str, Enum):
    NUMBER = "number"
    SELECT = "select"

    def __str__(self) -> str:
        return str(self.value)
