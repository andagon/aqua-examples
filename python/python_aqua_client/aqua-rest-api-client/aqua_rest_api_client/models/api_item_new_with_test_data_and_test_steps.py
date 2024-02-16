from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_attachment_new import ApiAttachmentNew
    from ..models.api_field_update import ApiFieldUpdate
    from ..models.api_item_location_update import ApiItemLocationUpdate
    from ..models.api_rich_text import ApiRichText
    from ..models.api_test_data_new import ApiTestDataNew
    from ..models.api_test_step_new import ApiTestStepNew


T = TypeVar("T", bound="ApiItemNewWithTestDataAndTestSteps")


@attr.s(auto_attribs=True)
class ApiItemNewWithTestDataAndTestSteps:
    """
    Attributes:
        location (Union[Unset, None, ApiItemLocationUpdate]):
        details (Union[Unset, None, List['ApiFieldUpdate']]): The list values which should be set when creating the
            item.
        attachments (Union[Unset, None, List['ApiAttachmentNew']]): The list of attachments which should be added to the
            new item.
        description (Union[Unset, None, ApiRichText]): Contains some rich text. The rich text is provided in several
            different formats.
            When sending rich text to the server, the rich text must be provided in exactly
            one format.
        test_data (Union[Unset, None, ApiTestDataNew]): Base class for models used when providing test data during test
            case creation.
            This class is abstract, not intended to be used directly.
        test_steps (Union[Unset, None, List['ApiTestStepNew']]): Contains the test steps.
    """

    location: Union[Unset, None, "ApiItemLocationUpdate"] = UNSET
    details: Union[Unset, None, List["ApiFieldUpdate"]] = UNSET
    attachments: Union[Unset, None, List["ApiAttachmentNew"]] = UNSET
    description: Union[Unset, None, "ApiRichText"] = UNSET
    test_data: Union[Unset, None, "ApiTestDataNew"] = UNSET
    test_steps: Union[Unset, None, List["ApiTestStepNew"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict() if self.location else None

        details: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            if self.details is None:
                details = None
            else:
                details = []
                for details_item_data in self.details:
                    details_item = details_item_data.to_dict()

                    details.append(details_item)

        attachments: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            if self.attachments is None:
                attachments = None
            else:
                attachments = []
                for attachments_item_data in self.attachments:
                    attachments_item = attachments_item_data.to_dict()

                    attachments.append(attachments_item)

        description: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict() if self.description else None

        test_data: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.test_data, Unset):
            test_data = self.test_data.to_dict() if self.test_data else None

        test_steps: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.test_steps, Unset):
            if self.test_steps is None:
                test_steps = None
            else:
                test_steps = []
                for test_steps_item_data in self.test_steps:
                    test_steps_item = test_steps_item_data.to_dict()

                    test_steps.append(test_steps_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location is not UNSET:
            field_dict["Location"] = location
        if details is not UNSET:
            field_dict["Details"] = details
        if attachments is not UNSET:
            field_dict["Attachments"] = attachments
        if description is not UNSET:
            field_dict["Description"] = description
        if test_data is not UNSET:
            field_dict["TestData"] = test_data
        if test_steps is not UNSET:
            field_dict["TestSteps"] = test_steps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_attachment_new import ApiAttachmentNew
        from ..models.api_field_update import ApiFieldUpdate
        from ..models.api_item_location_update import ApiItemLocationUpdate
        from ..models.api_rich_text import ApiRichText
        from ..models.api_test_data_new import ApiTestDataNew
        from ..models.api_test_step_new import ApiTestStepNew

        d = src_dict.copy()
        _location = d.pop("Location", UNSET)
        location: Union[Unset, None, ApiItemLocationUpdate]
        if _location is None:
            location = None
        elif isinstance(_location, Unset):
            location = UNSET
        else:
            location = ApiItemLocationUpdate.from_dict(_location)

        details = []
        _details = d.pop("Details", UNSET)
        for details_item_data in _details or []:
            details_item = ApiFieldUpdate.from_dict(details_item_data)

            details.append(details_item)

        attachments = []
        _attachments = d.pop("Attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = ApiAttachmentNew.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        _description = d.pop("Description", UNSET)
        description: Union[Unset, None, ApiRichText]
        if _description is None:
            description = None
        elif isinstance(_description, Unset):
            description = UNSET
        else:
            description = ApiRichText.from_dict(_description)

        _test_data = d.pop("TestData", UNSET)
        test_data: Union[Unset, None, ApiTestDataNew]
        if _test_data is None:
            test_data = None
        elif isinstance(_test_data, Unset):
            test_data = UNSET
        else:
            test_data = ApiTestDataNew.from_dict(_test_data)

        test_steps = []
        _test_steps = d.pop("TestSteps", UNSET)
        for test_steps_item_data in _test_steps or []:
            test_steps_item = ApiTestStepNew.from_dict(test_steps_item_data)

            test_steps.append(test_steps_item)

        api_item_new_with_test_data_and_test_steps = cls(
            location=location,
            details=details,
            attachments=attachments,
            description=description,
            test_data=test_data,
            test_steps=test_steps,
        )

        api_item_new_with_test_data_and_test_steps.additional_properties = d
        return api_item_new_with_test_data_and_test_steps

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
