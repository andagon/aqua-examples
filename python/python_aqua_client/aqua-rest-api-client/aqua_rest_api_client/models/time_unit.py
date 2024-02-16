from enum import Enum


class TimeUnit(str, Enum):
    DAY = "Day"
    MINUTE = "Minute"
    HOUR = "Hour"
    SECOND = "Second"
    WEEK = "Week"
    MONTH = "Month"

    def __str__(self) -> str:
        return str(self.value)
