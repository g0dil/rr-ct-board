from enum import Enum


class ReportStatus(str, Enum):
    ACCEPTED = "accepted"
    DECLINED = "declined"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
