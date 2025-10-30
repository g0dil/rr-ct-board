from enum import Enum


class PutBookingsBookingIdAnswerAnswer(str, Enum):
    APPROVE = "approve"
    REJECT = "reject"
    RESET = "reset"

    def __str__(self) -> str:
        return str(self.value)
