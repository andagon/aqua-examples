from enum import Enum


class ApiRichTextIncludeType(str, Enum):
    HTML = "HTML"
    PLAINTEXT = "PlainText"
    ALL = "All"

    def __str__(self) -> str:
        return str(self.value)
