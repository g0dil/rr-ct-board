from enum import Enum


class GetGroupsGroupIdResponse200DataInformationChatStatus(str, Enum):
    NOT_STARTED = "NOT_STARTED"
    STARTED = "STARTED"
    STARTING = "STARTING"
    STOPPED = "STOPPED"

    def __str__(self) -> str:
        return str(self.value)
