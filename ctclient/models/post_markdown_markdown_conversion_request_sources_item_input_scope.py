from enum import Enum


class PostMarkdownMarkdownConversionRequestSourcesItemInputScope(str, Enum):
    DESCRIPTION = "description"
    DOCUMENT = "document"
    PLAINTEXT = "plaintext"
    RICHLINE = "richline"

    def __str__(self) -> str:
        return str(self.value)
