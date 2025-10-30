from enum import Enum


class GetAllMeetingsIncludeItem(str, Enum):
    ATTENDANCES = "attendances"

    def __str__(self) -> str:
        return str(self.value)
