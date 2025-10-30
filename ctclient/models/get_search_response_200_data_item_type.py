from enum import Enum


class GetSearchResponse200DataItemType(str, Enum):
    ACTION = "action"
    DOMAINOBJECT = "domainObject"

    def __str__(self) -> str:
        return str(self.value)
