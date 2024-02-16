from enum import Enum


class ApiPdfChangingPermissions(str, Enum):
    NONE = "None"
    INSERTINGDELETINGROTATING = "InsertingDeletingRotating"
    FILLINGSIGNING = "FillingSigning"
    COMMENTINGFILLINGSIGNING = "CommentingFillingSigning"
    ANYEXCEPTEXTRACTINGPAGES = "AnyExceptExtractingPages"

    def __str__(self) -> str:
        return str(self.value)
