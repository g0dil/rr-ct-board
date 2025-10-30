from enum import Enum


class PostFollowupsFollowUpIdPostponeResponse200DataSuccessGroupMemberStatusType0(
    str, Enum
):
    ACTIVE = "active"
    REQUESTED = "requested"
    TO_DELETE = "to_delete"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
