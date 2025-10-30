from enum import Enum


class PutPostReportsAnswerBodyResponse(str, Enum):
    ACCEPT = "accept"
    DECLINE = "decline"

    def __str__(self) -> str:
        return str(self.value)
