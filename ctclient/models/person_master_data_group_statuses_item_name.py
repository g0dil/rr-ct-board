from enum import Enum


class PersonMasterDataGroupStatusesItemName(str, Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    FINISHED = "finished"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
