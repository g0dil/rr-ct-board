from enum import Enum


class DomainObjectWikiPageDomainType(str, Enum):
    WIKI_PAGE = "wiki_page"

    def __str__(self) -> str:
        return str(self.value)
