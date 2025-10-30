from enum import Enum


class PostGroupRolesBodyType(str, Enum):
    LEADER = "leader"
    PARTICIPANT = "participant"

    def __str__(self) -> str:
        return str(self.value)
