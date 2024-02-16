from enum import Enum


class ApiFieldSortMode(str, Enum):
    BYID = "ById"
    BYLAYOUTPOSITION = "ByLayoutPosition"
    BYTITLE = "ByTitle"

    def __str__(self) -> str:
        return str(self.value)
