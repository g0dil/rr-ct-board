from enum import Enum


class CreateHtmlTemplateBodyDomainType(str, Enum):
    BULKLETTER = "bulkletter"
    EMAIL = "email"

    def __str__(self) -> str:
        return str(self.value)
