from enum import IntEnum


class GetCalendarsCalendarIdAppointmentsResponse200DataItemBaseRepeatId(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_7 = 7
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_365 = 365
    VALUE_999 = 999

    def __str__(self) -> str:
        return str(self.value)
