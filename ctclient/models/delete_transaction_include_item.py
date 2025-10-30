from enum import Enum


class DeleteTransactionIncludeItem(str, Enum):
    BILLS = "bills"

    def __str__(self) -> str:
        return str(self.value)
