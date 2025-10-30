from enum import Enum


class FollowUp2SuccessGroupMemberStatusType0(str, Enum):
    ACTIVE = "active"
    REQUESTED = "requested"
    TO_DELETE = "to_delete"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
