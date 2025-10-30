from enum import Enum


class GetGroupsGroupIdMembersRoutinesResponse200DataItemRoutineStepsItemType1ChildrenItemType0Type0ActionKey(
    str, Enum
):
    SEND_MEMBER_EMAIL = "send-member-email"

    def __str__(self) -> str:
        return str(self.value)
