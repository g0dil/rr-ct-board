from enum import Enum


class PutConfigResponse200EmailServer(str, Enum):
    CHURCHTOOLS = "churchtools"
    OWN = "own"

    def __str__(self) -> str:
        return str(self.value)
