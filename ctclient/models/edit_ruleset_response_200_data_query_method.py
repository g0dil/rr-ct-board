from enum import Enum


class EditRulesetResponse200DataQueryMethod(str, Enum):
    CHURCHQUERY = "ChurchQuery"

    def __str__(self) -> str:
        return str(self.value)
