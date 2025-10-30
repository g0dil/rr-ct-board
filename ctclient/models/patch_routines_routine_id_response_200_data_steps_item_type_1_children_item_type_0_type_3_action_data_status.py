from enum import Enum


class PatchRoutinesRoutineIdResponse200DataStepsItemType1ChildrenItemType0Type3ActionDataStatus(
    str, Enum
):
    ACTIVE = "active"
    REQUESTED = "requested"
    TO_DELETE = "to_delete"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
