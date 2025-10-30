from enum import Enum


class FollowUp2Origin(str, Enum):
    BULK_JOB = "bulk-job"
    DEFAULT = "default"
    MIGRATION = "migration"
    ROUTINE = "routine"

    def __str__(self) -> str:
        return str(self.value)
