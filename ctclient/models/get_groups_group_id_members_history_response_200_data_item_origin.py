from enum import Enum


class GetGroupsGroupIdMembersHistoryResponse200DataItemOrigin(str, Enum):
    AUTOMATIC = "automatic"
    BULK_JOB = "bulk-job"
    CHECK_IN = "check-in"
    CRON = "cron"
    DEFAULT = "default"
    DUPLICATE_GROUP = "duplicate-group"
    FOLLOW_UP = "follow-up"
    GROUP_CREATION = "group-creation"
    PERSON_DELETION = "person-deletion"
    ROUTINE = "routine"
    SELF_REGISTRATION = "self-registration"
    SIGN_UP = "sign-up"
    WAITINGLIST = "waitinglist"

    def __str__(self) -> str:
        return str(self.value)
