from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.api_argument_error_type import ApiArgumentErrorType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiErrorInformation")


@attr.s(auto_attribs=True)
class ApiErrorInformation:
    """Contains information about an error which occurred during an API call.

    Attributes:
        argument_error_type (Union[Unset, ApiArgumentErrorType]): Identifies the type of "argument error" which
            occurred.
            Arument error is a situation when information received from the caller
            is invalid (e.g. does not fit into expected limits, is of invalid type etc.)
            or does not correspond to system state (e.g. trying to update a locked item).
            Argument errors are not system errors, but rather client errors.
            This enum has the following values:
              - `ActualResultsMissing` The actual results are not specified but are required.
              - `AgentNotFound` The agent does not exist.
              - `ArchiveJobAlreadyStarted` Archive job is already running, cannot start new one.
              - `AssignmentDeleteFailed` Delete the user assignment failed.
              - `AttachmentMaxSizeExceeded` Attachment size exceeds maximum size.
              - `AttachmentMaxTransferSizeExceeded` Attachments size exceeds maximum transfer size for one upload.
              - `AttachmentNotFound` Attachment does not exist.
              - `AutomationInTestStepNotPresentOrInvalid` Automation in given step was not present or was invalid (not as
            expected).
              - `AutomationScriptUnsupportedTechnologySave` The save for automation script technology is not supported.
              - `CalculatedFieldModified` The request tries to set the value of a field which is set to a calculated
            value by the workflow. Such a field cannot be modified by the end user.
              - `CannotModifyAutomaticDependencies` Automatic dependencies cannot be deleted or modified
              - `CannotUpdateReferencedTestData` It is not possible update test data which is referenced. Please update it
            in the other test case (owner of test data).
              - `CustomFilterAcceptedStatusesNotRecognized` Custom filter accepted statuses contains unrecognized value.
              - `CustomFilterOptionsNotEmpty` Custom filter options are not empty.
              - `DefaultEntriesUserIdNotAllowed` Default configuration data (global or project) must not
            contain a user id.
              - `DictionaryEntryNotFound` The dictionary entry with the given id was not found.
              - `DuplicateAgentCode` The agent code must be unique in the project.
              - `DuplicateAgentName` An agent name must be unique in the project.
              - `DuplicateDictionary` The name or id of a dictionary is not unique.
              - `DuplicateDictionaryEntry` The name or id of a dictionary entry is not unique.
              - `DuplicateProjectFolderFavourite` There is already a project folder favourite for given project & folder
              - `DuplicateProjectName` The name of the project is not unique.
              - `DuplicateReportParameter` Duplicate report parameter.
              - `DuplicateRoleName` The name of a role is not unique.
              - `DuplicateSprintName` The name of a sprint entry is not unique.
              - `DuplicateUserName` The name of a user entry is not unique.
              - `EmptyAgentName` Agent name is empty.
              - `EmptyDashboardTitle` The dashboard title must be set.
              - `EmptyItemName` The name of the item in the request is empty.
              - `EmptyListNotAllowed` The list of elements is expected to be non empty.
              - `EmptySprintName` The sprint name is empty.
              - `EnclosureNotFound` The enclosure with the given id does not exist.
              - `ExecutableFilesUploadBlocked` The upload of executable files is blocked..
              - `ExecuteAllWithTestJobIds` If a automated execution for all Testjobs in a Testscenario is to be started
            and also a List of Testjobids is provided. Only one of both can be used.
              - `ExecutionDependencyViolation` The provided execution dependencies are violated.
              - `ExecutionNotForSingleTestScenario` The test executions to save do not belong to a single
            test scenario.
              - `ExpectedLockMissing` The specified item is expected to be locked for exclusive editing by the current user
            but the edit lock is missing.
              - `ExpectedResultsMissing` The expected results are not specified but are required.
              - `ExpectedResultsNotAllowedForCondition` A condition step must not have an expected result.
              - `FieldIsNotCustomField` A field which is not a custom field is modified using the mechanism
            for custom fields.
              - `FieldNotSupported` A field specified in the request is not supported for this request.
              - `FieldRulesCycle` The requested would create a cyclic rule for the field rules.
              - `FieldRuleValueChangedNotSupported` A field rule specifies a value change for field for which changing
            the value by a field rule is not supported.
              - `FieldValueDuplicatedName` A field specified in the request has duplicated field value name.
              - `FieldValueDuplicatedPosition` A field specified in the request has duplicated field value position.
              - `FieldValueEmptyName` A field specified in the request has empty field value name.
              - `FieldValueReservedName` A field specified in the request has reserved field value name.
              - `FieldValueTooLongName` A field specified in the request has too long field value name.
              - `FileExtensionInvalid` The provided file extension for the uploaded file is invalid. Please make sure that
            file extension is not null or empty.
              - `FileInvalid` The uploaded file is invalid and cannot be processed. Either the request is not
            correctly constructed or the file content is incorrect.
              - `FileNameInvalid` The provided file name for the uploaded file is invalid. Please make sure that
            file name is not null or empty.
              - `FileNameUsedWithMultipart` The file name for the file is provided while multipart form data is used. Please
            make sure that
            file name is null or empty.
              - `FileNotFound` File does not exist.
              - `FileUploadAlreadyUploaded` The file was already uploaded. Each upload URL can only be used once.
              - `FileUploadSizeMismatch` The size uploaded file content does not match the provided file size.
              - `FileUploadWrongAzureBlobType` The blob type of the uploaded file is incorrect. Check the documentation
            regarding uploading to Azure Blob Storage
              - `FilterClauseFieldInvalid` The field part of a filter clause is invalid.
              - `FilterClauseFieldNotSupported` A field in the filter expression does not support filtering.
              - `FilterClauseIncorrectNumberOfValues` A filter clause contains an incorrect number of values
            for the given operator.
              - `FilterClauseInvalid` A clause in the filter expression is malformed.
              - `FilterClauseOperatorInvalid` A filter operator in a filter clause is invalid.
              - `FilterClauseOperatorNotSupported` A filter operator is not supported for field with
            which it is used.
              - `FilterClauseUnknownField` A field in the filter expression does not exist.
              - `FilterClauseValueInvalid` A value in a filter clause is invalid.
              - `FilterGroupInvalid` A group in the filtere expression is malformed.
              - `FilterGroupOperatorInvalid` A group in the filter expression contains an invalid
            group operator.
              - `FilterGroupOperatorsMixed` A group in the filter expression contains several different
            group operators. Each group in a filter expression must contain
            only a single type of group operator.
              - `FilterInvalid` The filter expression is malformed.
              - `FolderCycle` Cycle detected in folder path.
              - `FolderNameEmpty` Folder name is empty.
              - `FolderNameNotUnique` Folder name is not unique (there already exists a folder with same name).
              - `FolderNotEmpty` Folder is not empty.
              - `FolderNotFound` The folder does not exist.
              - `FolderNotificationRuleNotEmpty` Folder notification rule is not empty.
              - `ImageFormatInvalid` Image file format is invalid.
              - `ImageMaxSizeExceeded` Image size exceeds maximum size.
              - `InvalidAgent` The provided agent is not set or cant execute the item.
              - `InvalidAgentTypeForCopy` Only single agent supports copy operation.
              - `InvalidApiImportErrorType` Import is reporting an import error with no equivalent in ApiImportErrorType
              - `InvalidApiImportPhase` Import is reporting an import phase with no equivalent in ApiImportPhase
              - `InvalidApiItemTypeToObjectTypeMask` The type of the item is not valid for this operation.
              - `InvalidApiPermission` The permission is not valid.
              - `InvalidApplicableItemTypes` The applicable item types are not suitable for the user view.
              - `InvalidArgument` Represents generic "argument error" in situation when it is not possible
            to provide more detailed information about the problem.
              - `InvalidBodyValue` The request contains a body value which is invalid. Most likely, there is a datatype
            mismatch or the value is empty.
              - `InvalidColor` The color does not match any of the predefined colors.
              - `InvalidDependencyDependentOnItSelf` The item cannot be dependent on itself.
              - `InvalidEmail` The email is not valid.
              - `InvalidFieldValue` The request contains a field value which is invalid. Most likely, there is a datatype
            mismatch or the value specified for a dictionary field does not exist at all.
              - `InvalidFolderIdMultiProjectReport` Multi project report only possible on root folder.
              - `InvalidIntialLetters` The intial letters are invalid.
              - `InvalidItemPath` The item type does not match the path.
              - `InvalidLicenseAssignmentAlreadyAssigned` The license is already assigned to the user.
              - `InvalidLicenseAssignmentNotAssigned` The license is not assigned to the user.
              - `InvalidLicenseCode` The license with the give code does not exist.
              - `InvalidNestedTestCaseId` Invalid nested test case id.
              - `InvalidParameterValue` The provided parameter value is invalid.
              - `InvalidPatchType` The type of the patch request is not valid.
              - `InvalidProjectAssignment` The permission elevation is not allowed.
              - `InvalidProjectTreeParentFolder` The value for the parameter ParentFolder is invalid.
              - `InvalidReorderWidgets` The reorder of widgets is invalid.
              - `InvalidReportDefinitionFile` The file is not valid for report definitions.
              - `InvalidReportParameterValue` The provided value for a report parameter is invalid. Please
            check that the provided value fits to the type of the parameter.
              - `InvalidStepType` Invalid test step type.
              - `InvalidTestData` Invalid test data e.g. syntax error in formula
              - `InvalidTestDataLength` The requested test data has not equal length between values and valuesets or values
            and variables.
              - `InvalidTestJobId` The provided test job id is invalid.
              - `InvalidTestJobIndex` The provided test job index is not valid.
              - `InvalidTestJobRunDependencyIndex` The provided test job run dependency index is not valid.
              - `InvalidTestStepExecutionStatusType` Invalid test step execution status type.
              - `InvalidTestStepId` Invalid test step id.
              - `InvalidTestStepIndex` The provided test step index is not valid.
              - `InvalidUsername` The user name is not valid.
              - `InvalidValueSet` The provided value set is invalid.
              - `InvalidVersionOfProjectConfigFile` Trying to import project config of incompatible version
              - `ItemNotFound` The item does not exist.
              - `ItemTypeNotSupported` Indicates that the given item type is not supported for the given
            request.
              - `ItemTypeNotSupportedInDashboards` The ItemType is not supported in dashboards
              - `LicenseTypeNotChanged` The license has already this type.
              - `LockByAnotherUser` The item is currently locked for exclusive editing. The item is locked by
            another user.
              - `Locked` The item is currently locked for exclusive editing. The item might be locked by
            another user or by the same user.
              - `LowPasswordComplexity` The user password has low complexity.
              - `ManualExecutionsWithStatusAndWithout` Mixed executions with and without arbitrary status.
              - `ManualTestExecution` The manual test execution type is not supported.
              - `MultiChoiceFieldValueExceededMaxLength` The value of the MultiChoiceField has exceeded the maximum length.
              - `MultiPartNotOneFile` Your request body does not contain exactly one file in the multipart form data.
            Exactly one file must be provided in the multipart form data.
              - `MultipleDefaultEntries` Multiple default entries have been defined. There must be
            only one default entry.
              - `NestedTestCaseLoop` The nested test case creates an Infinite loop.
              - `NoExecutions` The list of executions is empty.
              - `NoFreeLicenses` There are no free licenses for the given type.
              - `None` Represents void argument error.
              - `NoTestData` No test data is defined.
              - `NoTestSteps` Test steps must be defined to execute a test case.
              - `NotificationTemplateInvalidLanguage` The language for the notification template is invalid.
              - `NotificationTemplateMixedLanguage` The language for the item event templates in the notification template
            is not unique.
              - `NotManualTestExecution` Test execution is not of the manual type (only manual test execution supported).
              - `NotOwnerOfProjectTemplate` You are not allowed to perform the requested operation with the template
            of the specified project as the project template is shared and the current
            project is not the owner of the template.
              - `NotSupported` Represents generic error type in situation when the feature is not supported.
              - `NoValueSetSelected` The specified test case is parameterized but no value
            set has been selected.
              - `OperationBlockedByOtherTask` The batch operation cannot be started because there is already running other
            task that prevents new one from starting
            (running on the same domain of items).
              - `OutdatedVersion` Your request included an item version which is not identical to the version
            of the item currently stored in the database. Most likely, the item was modified
            in between.
              - `ProjectConfigImportFailed` The import of the provided project configuration was not possible with the
            current import settings. Please check the provided list of errors.
              - `ProjectFolderUserIsAlreadyAssigned` The project and/or folder has already an user assignment.
              - `ProjectMaximumNumberReached` The maximum number of project is reached.
              - `ProjectNotFound` The project does not exist.
              - `ProjectRoleNotFound` The project role not found.
              - `ProjectRoleUpdateDuplicateEntry` The project update contains duplicated entries.
              - `ProjectRoleUpdateInvalidEntry` The project update contains invalid entries.
              - `ProjectTemplateDuplicateFieldOperations` The request contains duplicate operations for one or more fields.
              - `ProjectTemplateFieldIsActivated` The project template field is already activated.
            Hence the request operation is not possible.
              - `ProjectTemplateFieldIsDeactivated` The project template field is already deactivated.
            Hence the request operation is not possible.
              - `ProjectTemplateFieldOperationNotAllowed` The project template field does not allow the operation
            e.g. (FixedTitle can't be deactivated).
              - `ProjectTemplateNotIntendedLayoutChange` The last configuration of this project has been saved in desktop
            client.
            Saving in web client will work but causes significant changes to layout in desktop client accordingly.
            If this is intended, please provide the necessary parameter otherwise please change your configuration in
            desktop client.
              - `ProjectUserNotAssigned` The user is not assigned to the folder.
              - `ReportDefinitionNotFound` Report definition does not exist.
              - `ReportPluginNotRecognized` Report plugin has not been recognized. Is it deployed properly?
              - `ReportScriptingNotAllowed` Scripting in reports is not allowed
              - `RichtextInvalidImageUrl` The provided rich text contains invalid images. All images are expected to be
            uploaded to aqua before including them in the rich text. Please check the API
            documentation.
              - `RichtextMultipleFormatsProvided` The current request contains rich text in multiple formats at the same
            time.
            When saving rich text, the request must contain the rich text only in one
            format.
              - `RoleNotFound` The role with the given id does not exist.
              - `RunDependenciesMissing` Run dependencies are missing. When executing a test scenario,
            all run dependencies must be included in the execution as well.
              - `SharedDictionaryNotAllowed` The operation does not support shared dictionaries.
              - `SharedFieldValueDuplicatedName` A shared field specified in the request has duplicated field value name.
              - `SharedFieldValueDuplicatedPosition` A shared field specified in the request has duplicated field value
            position.
              - `SharedFieldValueEmptyName` A shared field specified in the request has empty field value name.
              - `SharedFieldValueSetDuplicatedName` A shared field specified in the request has duplicated field name.
              - `SharedFieldValueSetEmptyName` A shared field specified in the request has empty field name.
              - `SharedFieldValueSetTooLongName` A shared field specified in the request has too long field name.
              - `SharedFieldValueTooLongName` A shared field specified in the request has too long field value name.
              - `SortClauseDirectionInvalid` The direction specified in a sorting/grouping clause
            is invalid
              - `SortClauseFieldInvalid` The field part in a sorting/grouping is invalid.
              - `SortClauseFieldNotSupported` A field specified in a sorting/grouping clause
            does not support sorting or grouping.
              - `SortClauseInvalid` A clause in the sorting or grouping expression
            is invalid.
              - `SortClauseUnknownField` A field specified in a sorting/grouping clause
            does not exist.
              - `SortInvalid` The sorting or grouping expression is invalid.
              - `SprintStillContainsItems` There are still some items included in the sprint. Can not delete sprint.
              - `SubrequirementsCircleFound` The requested operation would create a circle in the sub requirement tree
            structure.
              - `SubrequirementsInconsistent` The sub requirement tree structure is inconsistent. Please make, sure that
            all child indexes are correct.
              - `SubrequirementsOtherLocked` The requested operation must also update other sub requirements in the
            sub requirement tree structure but at least one of them is already
            locked for exclusive editing.
              - `SubrequirementsOtherNotPermitted` The requested operation must also update other sub requirements in the
            sub requirement tree structure but the current user is not permitted to
            modify all of them.
              - `SupportOnlyAutomatedItem` The provided item is not valid for automated run.
              - `SystemFieldModified` The request tries to set the value of a field which is handled by the system
            and cannot be modified by the end user.
              - `TestCaseNotFound` One or more executions do refer to invalid test cases.
            The test case might not exist or not be accessible.
              - `TestDataExportTooManyVariablesForFileFormat` The requested file format does not support the number of
            variables contained
            in the test data.
              - `TestDataFileFormatNotSupported` The requested file format is not supported for the export or import of test
            data.
              - `TestDataImportFailed` The import of the test data failed.
              - `TestDataImportInvalidFile` The file import format is not the same as in the filename.
              - `TestDataImportInvalidXml` The XML to import is invalid.
              - `TestDataImportNoSheet` The file to import does not contain any work sheets.
              - `TestDataImportNoValueSets` The file to import does not contain any value sets.
              - `TestDataImportNoVariables` The file to import does not contain any variables.
              - `TestDataImportXmlMissingVariableName` A variable is missing in one of the value sets to import.
              - `TestDataImportXmlValueSetNotFound` A value set was not found when importing from XML.
              - `TestDataImportXmlVariableNotFound` A variable was not found when importing from XML.
              - `TestDataMisMatchVariablesNamesOrLength` The variables names or the number of variables are not the same
              - `TestDataNoValueSets` The test data does not contain any value sets.
              - `TestDataNumberOfValuesMisMatchToValueSets` The number of values does not match the number of valuesets
              - `TestDataNumberOfValuesMisMatchToVariables` The number of values does not match the number of variables
              - `TestDataRemoteTCAlreadyReferences` The other test case already references another test case, so it is not
            possible to reference test data from that test case.
              - `TestDataRemoteTCDeleted` The other test case is deleted so it is not possible to reference test data from
            that test case.
              - `TestDataRemoteTCNotAccessible` The other test case is not accessible so it is not possible to reference
            test data from that test case.
              - `TestDataRemoteTCNoTestData` The other test case has no test data so it is not possible to reference test
            data from that test case.
              - `TestDataTooManyValues` The test data contains too many values. The number of variables and/or value
            sets needs to be reduced.
              - `TestDataValueSetNameInvalid` The name of a value set is invalid.
              - `TestDataValueSetNameNotUnique` A variable name is not unique.
              - `TestDataValueSetNameTooLong` A value set name is too long.
              - `TestDataValueSetNotFound` The test data value set for a specific guid not found.
              - `TestDataValueTooLong` A value is too long.
              - `TestDataVariableNameInvalid` A variable name is invalid.
              - `TestDataVariableNameNotUnique` A variable name is not unique.
              - `TestDataVariableNameTooLong` A variable name is too long.
              - `TestExecutionFinalized` Cannot update finalized test execution.
              - `TestExecutionNotFound` Test execution does not exist.
              - `TestJobAgentNotFound` The agent specified in a test job cannot be found.
            Most likely the agent has been deleted.
              - `TestJobAgentNotSelected` The Agent for the test job is not selected.
              - `TestJobDisallowAgent` The non-automated test job forbids setting the agent.
              - `TestJobNotFound` The Testjob with the given id does not exist.
              - `TestScenarioNotFound` The test scenario with the given id does not exist.
              - `TestStepEmptyNestedTestCase` The test step of type NestedTestCase contains empty NastedCase.
              - `TestStepMandatoryExpectedResultIsEmpty` The test step contains empty mandatory expected result.
              - `TestStepNotEmptyNestedTestCase` The test step of type Condition or Step contains NestedTestCase.
              - `TestStepNotFound` The Teststep with the given id does not exist.
              - `TestStepOfTypeConditionContainsExpectedResult` The test step of type condition contains expected result.
              - `TestStepOfTypeNestedTestCaseNotEmptyValues` The test step of type NestedTestCase contains description
            and/or expected result.
              - `TooManyTestJobs` The current test scenario or test scenario execution contains
            too many test jobs.
              - `UnknownField` The request specifies a field or contains data for a field which does not exist.
              - `UnknownReportParameter` No report parameter with the specified name was found.
              - `UpdateOncePerTestExecution` Test execution already updated in this request.
              - `UserEntriesCannotBeLocked` User-level configuration data cannot be marked as Locked.
              - `UserEntriesMustHaveUserId` User-level configuration data must contain the id of the
            current user.
              - `UserNotFound` User not found.
              - `ValueTooBig` The provided value is too big for the argument.
              - `ViolatedPermissionDependencies` The permission dependencies are violated.
              - `WorkflowTransitionNotAllowed` The requested status transition is not allowed by the workflow.
              - `WorkflowViolated` The given value for a field violates the workflow.
              - `WrongDictionary` The dictionary in the request does not belong to the
            current field.
              - `WrongFieldType` The field specified in the requested is of the wrong type. Most likely,
            the current endpoint is not meant to be used with fields of this type.
              - `WrongPatchType` Wrong patch operation type is used.
        message (Union[Unset, None, str]): A human-readable description of the error.
    """

    argument_error_type: Union[Unset, ApiArgumentErrorType] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        argument_error_type: Union[Unset, str] = UNSET
        if not isinstance(self.argument_error_type, Unset):
            argument_error_type = self.argument_error_type.value

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if argument_error_type is not UNSET:
            field_dict["ArgumentErrorType"] = argument_error_type
        if message is not UNSET:
            field_dict["Message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _argument_error_type = d.pop("ArgumentErrorType", UNSET)
        argument_error_type: Union[Unset, ApiArgumentErrorType]
        if isinstance(_argument_error_type, Unset):
            argument_error_type = UNSET
        else:
            argument_error_type = ApiArgumentErrorType(_argument_error_type)

        message = d.pop("Message", UNSET)

        api_error_information = cls(
            argument_error_type=argument_error_type,
            message=message,
        )

        return api_error_information
