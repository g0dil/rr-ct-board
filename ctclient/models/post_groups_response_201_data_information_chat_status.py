from enum import Enum


class PostGroupsResponse201DataInformationChatStatus(str, Enum):
    NOT_STARTED = "NOT_STARTED"
    STARTED = "STARTED"
    STARTING = "STARTING"
    STOPPED = "STOPPED"

    def __str__(self) -> str:
        return str(self.value)
