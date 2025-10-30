from enum import Enum


class ActionKey(str, Enum):
    ADD_MEMBER_TO_GROUP = "add-member-to-group"
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
    CREATE_FOLLOW_UP = "create-follow-up"
    EDIT_GROUP_MEMBERSHIP = "edit-group-membership"
    SEND_MEMBER_EMAIL = "send-member-email"
    SPECIALREPEAT = "special:repeat"
    SPECIALWAIT = "special:wait"

    def __str__(self) -> str:
        return str(self.value)
