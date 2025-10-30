from enum import Enum


class MarkdownConversionRequestSourcesItemOutputFormatsItem(str, Enum):
    HTML = "html"
    MD = "md"
    XML = "xml"

    def __str__(self) -> str:
        return str(self.value)
