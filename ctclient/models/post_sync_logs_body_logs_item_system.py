from enum import Enum


class PostSyncLogsBodyLogsItemSystem(str, Enum):
    BOTH = "both"
    ES = "es"
    MASTER = "master"

    def __str__(self) -> str:
        return str(self.value)
