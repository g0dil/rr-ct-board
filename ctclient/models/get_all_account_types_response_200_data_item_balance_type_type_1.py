from enum import Enum


class GetAllAccountTypesResponse200DataItemBalanceTypeType1(str, Enum):
    ASSETS = "assets"
    LIABILITIES = "liabilities"

    def __str__(self) -> str:
        return str(self.value)
