from enum import Enum


class GetTransactionsCSVTarget(str, Enum):
    DEFAULT = "default"
    SAGE100 = "sage100"

    def __str__(self) -> str:
        return str(self.value)
