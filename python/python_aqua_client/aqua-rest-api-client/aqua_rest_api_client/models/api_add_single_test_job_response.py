from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiAddSingleTestJobResponse")


@attr.s(auto_attribs=True)
class ApiAddSingleTestJobResponse:
    """Contains information about created test job.

    Attributes:
        test_job_id (int): The id of the created test job.
    """

    test_job_id: int

    def to_dict(self) -> Dict[str, Any]:
        test_job_id = self.test_job_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "TestJobId": test_job_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        test_job_id = d.pop("TestJobId")

        api_add_single_test_job_response = cls(
            test_job_id=test_job_id,
        )

        return api_add_single_test_job_response
