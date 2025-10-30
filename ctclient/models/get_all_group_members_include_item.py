from enum import Enum


class GetAllGroupMembersIncludeItem(str, Enum):
    AGGREGATIONS = "aggregations"
    TAGS = "tags"

    def __str__(self) -> str:
        return str(self.value)
