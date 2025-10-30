from enum import Enum


class AccountTypeBalanceTypeType2Type1(str, Enum):
    ASSETS = "assets"
    LIABILITIES = "liabilities"

    def __str__(self) -> str:
        return str(self.value)
