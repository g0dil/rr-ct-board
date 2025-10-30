from enum import Enum


class PutConfigResponse200Brand(str, Enum):
    CHURCHTOOLS = "ChurchTools"
    VEREINTOOLS = "VereinTools"

    def __str__(self) -> str:
        return str(self.value)
