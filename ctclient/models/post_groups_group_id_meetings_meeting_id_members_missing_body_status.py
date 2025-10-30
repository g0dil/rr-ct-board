from enum import Enum


class PostGroupsGroupIdMeetingsMeetingIdMembersMissingBodyStatus(str, Enum):
    ABSENT = "absent"
    PRESENT = "present"

    def __str__(self) -> str:
        return str(self.value)
