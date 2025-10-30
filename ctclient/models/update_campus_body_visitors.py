from enum import IntEnum


class UpdateCampusBodyVisitors(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_50 = 50
    VALUE_100 = 100
    VALUE_250 = 250
    VALUE_500 = 500
    VALUE_1000 = 1000

    def __str__(self) -> str:
        return str(self.value)
