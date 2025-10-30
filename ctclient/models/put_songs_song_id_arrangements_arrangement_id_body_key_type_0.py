from enum import Enum


class PutSongsSongIdArrangementsArrangementIdBodyKeyType0(str, Enum):
    A = "A"
    AB = "Ab"
    AM = "Am"
    B = "B"
    BB = "Bb"
    BBM = "Bbm"
    BM = "Bm"
    C = "C"
    CM = "C#m"
    D = "D"
    DB = "Db"
    DM = "D#m"
    E = "E"
    EB = "Eb"
    EBM = "Ebm"
    EM = "Em"
    F = "F#"
    FM = "F#m"
    G = "G"
    GB = "Gb"
    GM = "G#m"

    def __str__(self) -> str:
        return str(self.value)
