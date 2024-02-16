from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_registered_file_editor import ApiRegisteredFileEditor


T = TypeVar("T", bound="ApiRegisteredFileEditorsRepository")


@attr.s(auto_attribs=True)
class ApiRegisteredFileEditorsRepository:
    """Contains repository of registered file editors (used in automation).

    Attributes:
        meta (Union[Unset, None, List['ApiRegisteredFileEditor']]): Editors meta-data
        scripts (Union[Unset, None, List[str]]): Editors scripts (javascript content)
    """

    meta: Union[Unset, None, List["ApiRegisteredFileEditor"]] = UNSET
    scripts: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        meta: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.meta, Unset):
            if self.meta is None:
                meta = None
            else:
                meta = []
                for meta_item_data in self.meta:
                    meta_item = meta_item_data.to_dict()

                    meta.append(meta_item)

        scripts: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.scripts, Unset):
            if self.scripts is None:
                scripts = None
            else:
                scripts = self.scripts

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if meta is not UNSET:
            field_dict["Meta"] = meta
        if scripts is not UNSET:
            field_dict["Scripts"] = scripts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_registered_file_editor import ApiRegisteredFileEditor

        d = src_dict.copy()
        meta = []
        _meta = d.pop("Meta", UNSET)
        for meta_item_data in _meta or []:
            meta_item = ApiRegisteredFileEditor.from_dict(meta_item_data)

            meta.append(meta_item)

        scripts = cast(List[str], d.pop("Scripts", UNSET))

        api_registered_file_editors_repository = cls(
            meta=meta,
            scripts=scripts,
        )

        return api_registered_file_editors_repository
