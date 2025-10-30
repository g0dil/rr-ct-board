from enum import Enum


class RoleUpdateType(str, Enum):
    LEADER = "leader"
    PARTICIPANT = "participant"

    def __str__(self) -> str:
        return str(self.value)
