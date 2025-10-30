from enum import Enum


class PatchRoutinesRoutineIdResponse200DataStepsItemType1ChildrenItemType0Type0ActionKey(
    str, Enum
):
    SEND_MEMBER_EMAIL = "send-member-email"

    def __str__(self) -> str:
        return str(self.value)
