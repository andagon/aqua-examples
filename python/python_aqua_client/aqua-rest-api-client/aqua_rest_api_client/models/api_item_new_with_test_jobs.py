from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_attachment_new import ApiAttachmentNew
    from ..models.api_field_update import ApiFieldUpdate
    from ..models.api_item_location_update import ApiItemLocationUpdate
    from ..models.api_rich_text import ApiRichText
    from ..models.api_test_job_new import ApiTestJobNew


T = TypeVar("T", bound="ApiItemNewWithTestJobs")


@attr.s(auto_attribs=True)
class ApiItemNewWithTestJobs:
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
        test_jobs (Union[Unset, None, List['ApiTestJobNew']]): A list with the new test jobs which should be added.
    """

    location: Union[Unset, None, "ApiItemLocationUpdate"] = UNSET
    details: Union[Unset, None, List["ApiFieldUpdate"]] = UNSET
    attachments: Union[Unset, None, List["ApiAttachmentNew"]] = UNSET
    description: Union[Unset, None, "ApiRichText"] = UNSET
    test_jobs: Union[Unset, None, List["ApiTestJobNew"]] = UNSET
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

        test_jobs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.test_jobs, Unset):
            if self.test_jobs is None:
                test_jobs = None
            else:
                test_jobs = []
                for test_jobs_item_data in self.test_jobs:
                    test_jobs_item = test_jobs_item_data.to_dict()

                    test_jobs.append(test_jobs_item)

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
        if test_jobs is not UNSET:
            field_dict["TestJobs"] = test_jobs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_attachment_new import ApiAttachmentNew
        from ..models.api_field_update import ApiFieldUpdate
        from ..models.api_item_location_update import ApiItemLocationUpdate
        from ..models.api_rich_text import ApiRichText
        from ..models.api_test_job_new import ApiTestJobNew

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

        test_jobs = []
        _test_jobs = d.pop("TestJobs", UNSET)
        for test_jobs_item_data in _test_jobs or []:
            test_jobs_item = ApiTestJobNew.from_dict(test_jobs_item_data)

            test_jobs.append(test_jobs_item)

        api_item_new_with_test_jobs = cls(
            location=location,
            details=details,
            attachments=attachments,
            description=description,
            test_jobs=test_jobs,
        )

        api_item_new_with_test_jobs.additional_properties = d
        return api_item_new_with_test_jobs

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
