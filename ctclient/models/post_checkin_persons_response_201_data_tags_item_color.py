from enum import Enum


class PostCheckinPersonsResponse201DataTagsItemColor(str, Enum):
    ACCENT = "accent"
    AMBER = "amber"
    BASIC = "basic"
    BLUE = "blue"
    CONSTRUCTIVE = "constructive"
    CRITICAL = "critical"
    CYAN = "cyan"
    DESTRUCTIVE = "destructive"
    EMERALD = "emerald"
    ERROR = "error"
    FUCHSIA = "fuchsia"
    GREEN = "green"
    INDIGO = "indigo"
    INFO = "info"
    LIME = "lime"
    MAGIC = "magic"
    ORANGE = "orange"
    PINK = "pink"
    PURPLE = "purple"
    RED = "red"
    ROSE = "rose"
    SKY = "sky"
    SUCCESS = "success"
    TEAL = "teal"
    VIOLET = "violet"
    WARNING = "warning"
    YELLOW = "yellow"

    def __str__(self) -> str:
        return str(self.value)
