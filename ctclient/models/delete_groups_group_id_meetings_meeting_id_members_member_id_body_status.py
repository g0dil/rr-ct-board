from enum import Enum


class DeleteGroupsGroupIdMeetingsMeetingIdMembersMemberIdBodyStatus(str, Enum):
    ABSENT = "absent"
    UNSURE = "unsure"

    def __str__(self) -> str:
        return str(self.value)
