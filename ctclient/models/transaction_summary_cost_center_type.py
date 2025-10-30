from enum import Enum


class TransactionSummaryCostCenterType(str, Enum):
    COSTCENTER_SUM = "costcenter-sum"

    def __str__(self) -> str:
        return str(self.value)
