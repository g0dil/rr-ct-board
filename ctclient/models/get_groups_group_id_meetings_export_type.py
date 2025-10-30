from enum import Enum


class GetGroupsGroupIdMeetingsExportType(str, Enum):
    MEETINGS_MEMBERS = "meetings_members"
    MEETINGS_OVERVIEW = "meetings_overview"

    def __str__(self) -> str:
        return str(self.value)
