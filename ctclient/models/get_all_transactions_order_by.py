from enum import Enum


class GetAllTransactionsOrderBy(str, Enum):
    AMOUNT = "amount"
    DATE = "date"
    MODIFIED = "modified"

    def __str__(self) -> str:
        return str(self.value)
