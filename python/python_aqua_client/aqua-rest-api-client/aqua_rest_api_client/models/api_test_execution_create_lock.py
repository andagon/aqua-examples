from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_lock_new import ApiLockNew


T = TypeVar("T", bound="ApiTestExecutionCreateLock")


@attr.s(auto_attribs=True)
class ApiTestExecutionCreateLock:
    """Represents necessary information for creating an test execution lock.

    Attributes:
        test_execution_id (Union[Unset, int]): The id of the test execution.
        lock_info (Union[Unset, None, ApiLockNew]): Contains the information necessary to lock an item for
            exclusive editing.
    """

    test_execution_id: Union[Unset, int] = UNSET
    lock_info: Union[Unset, None, "ApiLockNew"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        test_execution_id = self.test_execution_id
        lock_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.lock_info, Unset):
            lock_info = self.lock_info.to_dict() if self.lock_info else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if test_execution_id is not UNSET:
            field_dict["TestExecutionId"] = test_execution_id
        if lock_info is not UNSET:
            field_dict["LockInfo"] = lock_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_lock_new import ApiLockNew

        d = src_dict.copy()
        test_execution_id = d.pop("TestExecutionId", UNSET)

        _lock_info = d.pop("LockInfo", UNSET)
        lock_info: Union[Unset, None, ApiLockNew]
        if _lock_info is None:
            lock_info = None
        elif isinstance(_lock_info, Unset):
            lock_info = UNSET
        else:
            lock_info = ApiLockNew.from_dict(_lock_info)

        api_test_execution_create_lock = cls(
            test_execution_id=test_execution_id,
            lock_info=lock_info,
        )

        return api_test_execution_create_lock
