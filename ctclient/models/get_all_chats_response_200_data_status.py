from enum import Enum


class GetAllChatsResponse200DataStatus(str, Enum):
    NOT_STARTED = "NOT_STARTED"
    STARTED = "STARTED"
    STARTING = "STARTING"
    STOPPED = "STOPPED"

    def __str__(self) -> str:
        return str(self.value)
