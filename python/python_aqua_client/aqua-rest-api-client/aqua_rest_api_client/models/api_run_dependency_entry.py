from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiRunDependencyEntry")


@attr.s(auto_attribs=True)
class ApiRunDependencyEntry:
    """
    Attributes:
        run_index (int): Dependecy on run index.
        on_success_only (bool): Describes if true this is a hard dependency otherwise this is a soft dependecy.
    """

    run_index: int
    on_success_only: bool

    def to_dict(self) -> Dict[str, Any]:
        run_index = self.run_index
        on_success_only = self.on_success_only

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "RunIndex": run_index,
                "OnSuccessOnly": on_success_only,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        run_index = d.pop("RunIndex")

        on_success_only = d.pop("OnSuccessOnly")

        api_run_dependency_entry = cls(
            run_index=run_index,
            on_success_only=on_success_only,
        )

        return api_run_dependency_entry
