from enum import Enum


class GetUserRulesResponse200DataItemOperator(str, Enum):
    CONTAINS = "contains"
    EQUALS = "equals"
    REGEX = "regex"

    def __str__(self) -> str:
        return str(self.value)
