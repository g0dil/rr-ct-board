from enum import Enum


class RoutineStepCreateEditGroupMembershipActionKey(str, Enum):
    EDIT_GROUP_MEMBERSHIP = "edit-group-membership"

    def __str__(self) -> str:
        return str(self.value)
