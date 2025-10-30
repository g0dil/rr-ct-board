from enum import Enum


class UpdateTransactionIncludeItem(str, Enum):
    BILLS = "bills"

    def __str__(self) -> str:
        return str(self.value)
