from enum import Enum


class PutDynamicgrouopStatusResponse200DataQueryMethod(str, Enum):
    CHURCHQUERY = "ChurchQuery"

    def __str__(self) -> str:
        return str(self.value)
