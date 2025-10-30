from enum import Enum


class PostFinanceTurnoverReportBodyPeriod(str, Enum):
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"

    def __str__(self) -> str:
        return str(self.value)
