from enum import Enum


class WebsiteDataCreateDomainType(str, Enum):
    CALENDAR = "calendar"
    PERSON = "person"
    POSTS_IN_GROUP = "posts-in-group"
    STAFF = "staff"

    def __str__(self) -> str:
        return str(self.value)
