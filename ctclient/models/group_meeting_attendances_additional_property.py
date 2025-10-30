from enum import Enum


class GroupMeetingAttendancesAdditionalProperty(str, Enum):
    ABSENT = "absent"
    NOT_IN_GROUP = "not-in-group"
    PRESENT = "present"
    UNSURE = "unsure"

    def __str__(self) -> str:
        return str(self.value)
