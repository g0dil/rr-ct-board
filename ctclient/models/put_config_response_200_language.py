from enum import Enum


class PutConfigResponse200Language(str, Enum):
    CN = "cn"
    DE = "de"
    EN = "en"
    ES = "es"
    FA = "fa"
    FI = "fi"
    FR = "fr"
    IT = "it"
    NL = "nl"
    PL = "pl"
    PT = "pt"
    RU = "ru"
    TW = "tw"

    def __str__(self) -> str:
        return str(self.value)
