from enum import Enum


class ApiFileUploadUrlType(str, Enum):
    AQUA = "Aqua"
    AZUREBLOBSTORAGE = "AzureBlobStorage"

    def __str__(self) -> str:
        return str(self.value)
