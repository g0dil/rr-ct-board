from enum import Enum


class PostLoginTotpResponse200DataStatus(str, Enum):
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
