from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_test_job_preview import ApiTestJobPreview


T = TypeVar("T", bound="ApiTestJobPreviewResponse")


@attr.s(auto_attribs=True)
class ApiTestJobPreviewResponse:
    """
    Attributes:
        not_accessible_test_cases (Union[Unset, None, List[int]]): The list of not accessible test case ids.
        test_job_preview (Union[Unset, None, List['ApiTestJobPreview']]): The preview list of the test jobs.
    """

    not_accessible_test_cases: Union[Unset, None, List[int]] = UNSET
    test_job_preview: Union[Unset, None, List["ApiTestJobPreview"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        not_accessible_test_cases: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.not_accessible_test_cases, Unset):
            if self.not_accessible_test_cases is None:
                not_accessible_test_cases = None
            else:
                not_accessible_test_cases = self.not_accessible_test_cases

        test_job_preview: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.test_job_preview, Unset):
            if self.test_job_preview is None:
                test_job_preview = None
            else:
                test_job_preview = []
                for test_job_preview_item_data in self.test_job_preview:
                    test_job_preview_item = test_job_preview_item_data.to_dict()

                    test_job_preview.append(test_job_preview_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if not_accessible_test_cases is not UNSET:
            field_dict["NotAccessibleTestCases"] = not_accessible_test_cases
        if test_job_preview is not UNSET:
            field_dict["TestJobPreview"] = test_job_preview

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_test_job_preview import ApiTestJobPreview

        d = src_dict.copy()
        not_accessible_test_cases = cast(List[int], d.pop("NotAccessibleTestCases", UNSET))

        test_job_preview = []
        _test_job_preview = d.pop("TestJobPreview", UNSET)
        for test_job_preview_item_data in _test_job_preview or []:
            test_job_preview_item = ApiTestJobPreview.from_dict(test_job_preview_item_data)

            test_job_preview.append(test_job_preview_item)

        api_test_job_preview_response = cls(
            not_accessible_test_cases=not_accessible_test_cases,
            test_job_preview=test_job_preview,
        )

        return api_test_job_preview_response
