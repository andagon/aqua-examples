from enum import Enum


class ApiFieldType(str, Enum):
    DATETIME = "DateTime"
    DECIMAL = "Decimal"
    DICTIONARY = "Dictionary"
    DICTIONARYMULTICHOICE = "DictionaryMultiChoice"
    SPRINT = "Sprint"
    STRING = "String"
    TEXT = "Text"
    TIMESPAN = "TimeSpan"
    USER = "User"
    USERMULTICHOICE = "UserMultiChoice"
    STRINGAUTOCOMPLETE = "StringAutoComplete"
    ID = "Id"
    FLAG = "Flag"
    EXECUTIONHISTORY = "ExecutionHistory"
    TESTSCENARIOS = "TestScenarios"
    TESTJOBSTATISTICS = "TestJobStatistics"
    STRINGLIST = "StringList"
    JSON = "Json"

    def __str__(self) -> str:
        return str(self.value)
