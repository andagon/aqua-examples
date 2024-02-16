from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.api_batch_operation_type import ApiBatchOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiBatchOperation")


@attr.s(auto_attribs=True)
class ApiBatchOperation:
    """Represents a batch operation. A batch operation performs
    the same change on multiple items.

        Attributes:
            type (Union[Unset, ApiBatchOperationType]): The type of batch operation.
                This enum has the following values:
                  - `Unlock` Remove any edit locks by the current user on the specified items.
            ids (Union[Unset, None, List[int]]): Specifies the items which should be modified with this batch operation.
    """

    type: Union[Unset, ApiBatchOperationType] = UNSET
    ids: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.ids, Unset):
            if self.ids is None:
                ids = None
            else:
                ids = self.ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["Type"] = type
        if ids is not UNSET:
            field_dict["Ids"] = ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("Type", UNSET)
        type: Union[Unset, ApiBatchOperationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ApiBatchOperationType(_type)

        ids = cast(List[int], d.pop("Ids", UNSET))

        api_batch_operation = cls(
            type=type,
            ids=ids,
        )

        return api_batch_operation
