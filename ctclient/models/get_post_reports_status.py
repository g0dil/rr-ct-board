from enum import Enum


class GetPostReportsStatus(str, Enum):
    ACCEPTED = "accepted"
    DECLINED = "declined"
    PENDING = "pending"
    PENDING_AGAIN = "pending-again"

    def __str__(self) -> str:
        return str(self.value)
