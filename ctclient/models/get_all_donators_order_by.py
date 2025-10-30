from enum import Enum


class GetAllDonatorsOrderBy(str, Enum):
    COUNT = "count"
    LAST = "last"
    NAME = "name"
    SUM = "sum"

    def __str__(self) -> str:
        return str(self.value)
