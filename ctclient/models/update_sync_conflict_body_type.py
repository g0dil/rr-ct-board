from enum import Enum


class UpdateSyncConflictBodyType(str, Enum):
    CREATE = "create"
    DELETE_OR_CREATE = "delete or create"
    DUPLICATE_IN_CT = "duplicate in CT"
    DUPLICATE_IN_SOURCE = "duplicate in source"
    LINK_AN_DUPDATE = "link an dupdate"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
