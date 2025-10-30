from enum import Enum


class GetSearchDomainTypesItem(str, Enum):
    ACTION = "action"
    GROUP = "group"
    PERSON = "person"
    SONG = "song"
    WIKI_PAGE = "wiki_page"

    def __str__(self) -> str:
        return str(self.value)
