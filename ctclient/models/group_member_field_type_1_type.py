from enum import Enum


class GroupMemberFieldType1Type(str, Enum):
    GROUP = "group"

    def __str__(self) -> str:
        return str(self.value)
