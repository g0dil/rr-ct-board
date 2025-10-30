from enum import Enum


class PostSyncLogsBodyLogsItemType(str, Enum):
    CREATE = "create"
    DELETE = "delete"
    EXECUTION = "execution"
    LINK = "link"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
