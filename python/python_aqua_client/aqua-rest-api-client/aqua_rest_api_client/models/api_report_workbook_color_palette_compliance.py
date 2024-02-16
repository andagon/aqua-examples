from enum import Enum


class ApiReportWorkbookColorPaletteCompliance(str, Enum):
    ADJUSTCOLORSTODEFAULTPALETTE = "AdjustColorsToDefaultPalette"
    REDUCEPALETTEFOREXACTCOLORS = "ReducePaletteForExactColors"

    def __str__(self) -> str:
        return str(self.value)
