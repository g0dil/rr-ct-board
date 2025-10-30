from enum import Enum


class TransactionSummaryCreditDebitType(str, Enum):
    CREDIT_DEBIT = "credit-debit"

    def __str__(self) -> str:
        return str(self.value)
