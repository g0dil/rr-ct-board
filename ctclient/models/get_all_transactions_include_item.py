from enum import Enum


class GetAllTransactionsIncludeItem(str, Enum):
    BILLS = "bills"

    def __str__(self) -> str:
        return str(self.value)
