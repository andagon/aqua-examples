from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_import_error_type import ApiImportErrorType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiImportErrorReportItem")


@attr.s(auto_attribs=True)
class ApiImportErrorReportItem:
    """An individual error during import

    Attributes:
        error_type (Union[Unset, ApiImportErrorType]): Represents reason of a failure of import operation
            Note that some of these errors can be caused by using the wrong culture
            This enum has the following values:
              - `CreateAttachmentError` Never used
              - `CreateDateTimeError` Invalid Datetime: value could not be parsed
              - `CreateDependencyError` Invalid Depenceny
              - `CreateEnclosureError` No Id column to match Enclosures to Defect
              - `CreateEnclosureItemError` Invalid type supplied for enclosure
              - `CreateHierarchyError` Error while matching requirement to parent
              - `CreateListError` Invalid MultiChoiceDropDown: value could not be matched to a list of valid values
              - `CreateNumberError` Invalid Number: value could not be parsed
              - `CreateTestJobNoRelatedTestCaseImportedError` The TestCase for a TestScenario's TestJob was not imported
            during this import
              - `CreateTestJobsError` No Id column to match Testjobs to testscenario
              - `CreateTestStepError` No Id column to match Teststep to TestCase
              - `CreateTestStepItemError` Invalid type supplied for TestStep
              - `CreateUserError` Invalid User: value could not be matched to a single user
              - `DefectNoFieldMatchedError` No data in Row to import into Defect
              - `DuplicateId` The same id is given to several objects (has to be unique across all worksheets)
              - `DuplicateUser` Value from import-file denotes more than one user
              - `ImportFileInvalid` xls file can not be read as such
              - `InvalidArchive` corrupt zip file
              - `InvalidColumnNameError` Column mapped to not importable property of object
              - `InvalidSheetName` Worksheetname is not recognized to relate to an objecttype.
              - `NoDataInWorkSheet` No data to import found after header row/No columns found besides id column
              - `NoKeyColumn` No Id column found in worksheet
              - `NoPermissionToCreateItem` Importing user has not the permission to create object in destined folder
              - `NoValidFileInArchive` Zip-archive contains not xls on root level
              - `RequirementNoFieldMathchedError` No data in Row to import into Requirement
              - `ScreenShotNotFoundError` Rich client only - linked Screenshot in rtf not found in import data
              - `ServerError` An internal server error occured
              - `TestCaseNoFieldMatchedError` No data in Row to import into Testcase
              - `TestScenarioNoFieldMatchedError` No data in Row to import into testscenario
        import_key (Union[Unset, None, str]): The column header
        row (Union[Unset, int]): The row number on the Worksheet the error occured on
        property_name (Union[Unset, None, str]): Target property of the baseobject (or subitem like teststep,enclosure
            etc)
        incorrect_value (Union[Unset, None, str]): Invalid value from worksheet
        error_message (Union[Unset, None, str]): The Error Message
        column (Union[Unset, int]): The column number on the Worksheet the error occured on
        work_sheet_name (Union[Unset, None, str]): The Worksheet the error occured on
    """

    error_type: Union[Unset, ApiImportErrorType] = UNSET
    import_key: Union[Unset, None, str] = UNSET
    row: Union[Unset, int] = UNSET
    property_name: Union[Unset, None, str] = UNSET
    incorrect_value: Union[Unset, None, str] = UNSET
    error_message: Union[Unset, None, str] = UNSET
    column: Union[Unset, int] = UNSET
    work_sheet_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        error_type: Union[Unset, str] = UNSET
        if not isinstance(self.error_type, Unset):
            error_type = self.error_type.value

        import_key = self.import_key
        row = self.row
        property_name = self.property_name
        incorrect_value = self.incorrect_value
        error_message = self.error_message
        column = self.column
        work_sheet_name = self.work_sheet_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if error_type is not UNSET:
            field_dict["ErrorType"] = error_type
        if import_key is not UNSET:
            field_dict["ImportKey"] = import_key
        if row is not UNSET:
            field_dict["Row"] = row
        if property_name is not UNSET:
            field_dict["PropertyName"] = property_name
        if incorrect_value is not UNSET:
            field_dict["IncorrectValue"] = incorrect_value
        if error_message is not UNSET:
            field_dict["ErrorMessage"] = error_message
        if column is not UNSET:
            field_dict["Column"] = column
        if work_sheet_name is not UNSET:
            field_dict["WorkSheetName"] = work_sheet_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _error_type = d.pop("ErrorType", UNSET)
        error_type: Union[Unset, ApiImportErrorType]
        if isinstance(_error_type, Unset):
            error_type = UNSET
        else:
            error_type = ApiImportErrorType(_error_type)

        import_key = d.pop("ImportKey", UNSET)

        row = d.pop("Row", UNSET)

        property_name = d.pop("PropertyName", UNSET)

        incorrect_value = d.pop("IncorrectValue", UNSET)

        error_message = d.pop("ErrorMessage", UNSET)

        column = d.pop("Column", UNSET)

        work_sheet_name = d.pop("WorkSheetName", UNSET)

        api_import_error_report_item = cls(
            error_type=error_type,
            import_key=import_key,
            row=row,
            property_name=property_name,
            incorrect_value=incorrect_value,
            error_message=error_message,
            column=column,
            work_sheet_name=work_sheet_name,
        )

        return api_import_error_report_item
