from enum import Enum


class GetBookingsIncludeItem(str, Enum):
    CONFLICTS = "conflicts"
    INVOLVEDPERSONSDOMAINOBJECTS = "involvedPersonsDomainObjects"

    def __str__(self) -> str:
        return str(self.value)
