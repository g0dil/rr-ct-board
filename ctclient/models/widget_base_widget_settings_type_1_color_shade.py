from enum import IntEnum


class WidgetBaseWidgetSettingsType1ColorShade(IntEnum):
    VALUE_50 = 50
    VALUE_100 = 100
    VALUE_200 = 200
    VALUE_300 = 300
    VALUE_400 = 400
    VALUE_500 = 500
    VALUE_600 = 600
    VALUE_700 = 700
    VALUE_800 = 800
    VALUE_900 = 900

    def __str__(self) -> str:
        return str(self.value)
