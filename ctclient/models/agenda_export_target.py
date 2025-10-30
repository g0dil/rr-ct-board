from enum import Enum


class AgendaExportTarget(str, Enum):
    PRO_PRESENTER_6 = "PRO_PRESENTER_6"
    PRO_PRESENTER_7 = "PRO_PRESENTER_7"
    SONG_BEAMER = "SONG_BEAMER"

    def __str__(self) -> str:
        return str(self.value)
