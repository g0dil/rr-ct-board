from enum import Enum


class PatchRoutinesRoutineIdResponse200DataDomainType(str, Enum):
    GROUP_MEMBERSHIP = "group_membership"

    def __str__(self) -> str:
        return str(self.value)
