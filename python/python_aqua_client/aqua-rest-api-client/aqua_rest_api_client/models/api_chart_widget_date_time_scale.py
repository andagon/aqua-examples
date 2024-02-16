from enum import Enum


class ApiChartWidgetDateTimeScale(str, Enum):
    DAY = "Day"
    CALENDARWEEK = "CalendarWeek"
    MONTH = "Month"

    def __str__(self) -> str:
        return str(self.value)
