from enum import Enum


class GetWebsiteDataIncludeItem(str, Enum):
    DOMAINDATA = "domainData"

    def __str__(self) -> str:
        return str(self.value)
