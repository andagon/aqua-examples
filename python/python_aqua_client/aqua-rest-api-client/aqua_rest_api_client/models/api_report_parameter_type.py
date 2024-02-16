from enum import Enum


class ApiReportParameterType(str, Enum):
    STRING = "String"
    DATE = "Date"
    NUMBER16 = "Number16"
    NUMBER32 = "Number32"
    NUMBER64 = "Number64"
    NUMBERFLOAT = "NumberFloat"
    NUMBERDOUBLE = "NumberDouble"
    NUMBERDECIMAL = "NumberDecimal"
    BOOLEAN = "Boolean"
    GUID = "Guid"

    def __str__(self) -> str:
        return str(self.value)
