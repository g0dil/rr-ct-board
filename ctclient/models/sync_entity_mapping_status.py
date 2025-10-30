from enum import Enum


class SyncEntityMappingStatus(str, Enum):
    CONFLICT = "conflict"
    DELETED_IN_CT = "deleted in CT"
    SYNCED = "synced"

    def __str__(self) -> str:
        return str(self.value)
