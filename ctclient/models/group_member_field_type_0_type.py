from enum import Enum


class GroupMemberFieldType0Type(str, Enum):
    PERSON = "person"

    def __str__(self) -> str:
        return str(self.value)
