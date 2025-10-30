from enum import Enum


class GetPersonsPersonIdPostsFilterItem(str, Enum):
    BANNED = "banned"
    EXPIRATION_FUTURE = "expiration_future"
    EXPIRATION_PAST = "expiration_past"
    PUBLICATION_FUTURE = "publication_future"
    PUBLISHED = "published"

    def __str__(self) -> str:
        return str(self.value)
