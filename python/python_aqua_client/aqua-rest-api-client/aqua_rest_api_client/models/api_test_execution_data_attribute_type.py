from enum import Enum


class ApiTestExecutionDataAttributeType(str, Enum):
    STRING = "String"
    INTEGER = "Integer"
    FLOAT = "Float"

    def __str__(self) -> str:
        return str(self.value)
