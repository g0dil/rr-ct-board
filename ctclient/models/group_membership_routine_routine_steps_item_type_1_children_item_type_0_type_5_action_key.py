from enum import Enum


class GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type5ActionKey(
    str, Enum
):
    CHANGE_MEMBER_STATUS_ACTIVE_REQUESTED = "change-member-status-active-requested"
    CHANGE_MEMBER_STATUS_ACTIVE_TO_DELETE = "change-member-status-active-to_delete"
    CHANGE_MEMBER_STATUS_ACTIVE_WAITING = "change-member-status-active-waiting"
    CHANGE_MEMBER_STATUS_REQUESTED_ACTIVE = "change-member-status-requested-active"
    CHANGE_MEMBER_STATUS_REQUESTED_TO_DELETE = (
        "change-member-status-requested-to_delete"
    )
    CHANGE_MEMBER_STATUS_REQUESTED_WAITING = "change-member-status-requested-waiting"
    CHANGE_MEMBER_STATUS_TO_DELETE_ACTIVE = "change-member-status-to_delete-active"
    CHANGE_MEMBER_STATUS_TO_DELETE_REQUESTED = (
        "change-member-status-to_delete-requested"
    )
    CHANGE_MEMBER_STATUS_TO_DELETE_WAITING = "change-member-status-to_delete-waiting"
    CHANGE_MEMBER_STATUS_WAITING_ACTIVE = "change-member-status-waiting-active"
    CHANGE_MEMBER_STATUS_WAITING_TO_DELETE = "change-member-status-waiting-to_delete"

    def __str__(self) -> str:
        return str(self.value)
