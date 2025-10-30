from enum import Enum


class MovementState(str, Enum):
    BOOKED = "booked"
    IGNORED = "ignored"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
