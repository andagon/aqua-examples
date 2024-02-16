from enum import Enum


class ApiImportErrorType(str, Enum):
    CREATEDATETIMEERROR = "CreateDateTimeError"
    CREATENUMBERERROR = "CreateNumberError"
    CREATEUSERERROR = "CreateUserError"
    CREATELISTERROR = "CreateListError"
    CREATEHIERARCHYERROR = "CreateHierarchyError"
    CREATEDEPENDENCYERROR = "CreateDependencyError"
    CREATEENCLOSUREERROR = "CreateEnclosureError"
    CREATEATTACHMENTERROR = "CreateAttachmentError"
    CREATETESTSTEPERROR = "CreateTestStepError"
    INVALIDCOLUMNNAMEERROR = "InvalidColumnNameError"
    DEFECTNOFIELDMATCHEDERROR = "DefectNoFieldMatchedError"
    REQUIREMENTNOFIELDMATHCHEDERROR = "RequirementNoFieldMathchedError"
    TESTCASENOFIELDMATCHEDERROR = "TestCaseNoFieldMatchedError"
    SCREENSHOTNOTFOUNDERROR = "ScreenShotNotFoundError"
    CREATETESTSTEPITEMERROR = "CreateTestStepItemError"
    CREATEENCLOSUREITEMERROR = "CreateEnclosureItemError"
    TESTSCENARIONOFIELDMATCHEDERROR = "TestScenarioNoFieldMatchedError"
    CREATETESTJOBSERROR = "CreateTestJobsError"
    CREATETESTJOBNORELATEDTESTCASEIMPORTEDERROR = "CreateTestJobNoRelatedTestCaseImportedError"
    NOPERMISSIONTOCREATEITEM = "NoPermissionToCreateItem"
    NOKEYCOLUMN = "NoKeyColumn"
    NODATAINWORKSHEET = "NoDataInWorkSheet"
    INVALIDSHEETNAME = "InvalidSheetName"
    DUPLICATEUSER = "DuplicateUser"
    DUPLICATEID = "DuplicateId"
    NOVALIDFILEINARCHIVE = "NoValidFileInArchive"
    IMPORTFILEINVALID = "ImportFileInvalid"
    INVALIDARCHIVE = "InvalidArchive"
    SERVERERROR = "ServerError"

    def __str__(self) -> str:
        return str(self.value)
