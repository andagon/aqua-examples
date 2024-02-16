from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.api_report_options_new import ApiReportOptionsNew


T = TypeVar("T", bound="ApiReportCreateRequest")


@attr.s(auto_attribs=True)
class ApiReportCreateRequest:
    """Represent the report to be created.
    Note: the report layout is not included here (report is created with default layout).

        Attributes:
            project_id (int): Id of the project where report should be created.
            options (ApiReportOptionsNew): Represents new report options.
    """

    project_id: int
    options: "ApiReportOptionsNew"

    def to_dict(self) -> Dict[str, Any]:
        project_id = self.project_id
        options = self.options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "ProjectId": project_id,
                "Options": options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_report_options_new import ApiReportOptionsNew

        d = src_dict.copy()
        project_id = d.pop("ProjectId")

        options = ApiReportOptionsNew.from_dict(d.pop("Options"))

        api_report_create_request = cls(
            project_id=project_id,
            options=options,
        )

        return api_report_create_request
