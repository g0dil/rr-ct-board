from enum import Enum


class GetAllGroupMembersOrderDirectionsItem(str, Enum):
    ASC = "ASC"
    DESC = "DESC"

    def __str__(self) -> str:
        return str(self.value)
