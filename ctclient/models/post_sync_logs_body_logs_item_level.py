from enum import Enum


class PostSyncLogsBodyLogsItemLevel(str, Enum):
    ALERT = "alert"
    CRITICAL = "critical"
    DEBUG = "debug"
    EMERGENCY = "emergency"
    ERROR = "error"
    INFO = "info"
    NOTICE = "notice"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
