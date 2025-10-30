from enum import IntEnum


class CalculateUpdatedBookingConflictsResponse200DataItemStatusId(IntEnum):
    PENDING = 1
    CONFIRMED = 2
    CANCELED = 3
    DELETED = 99

    def __str__(self) -> str:
        return str(self.value)
