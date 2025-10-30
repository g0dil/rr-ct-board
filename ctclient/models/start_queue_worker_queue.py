from enum import Enum


class StartQueueWorkerQueue(str, Enum):
    DEFAULT = "default"

    def __str__(self) -> str:
        return str(self.value)
