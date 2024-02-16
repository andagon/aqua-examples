from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_customized_strings_english import ApiCustomizedStringsEnglish
    from ..models.api_customized_strings_german import ApiCustomizedStringsGerman


T = TypeVar("T", bound="ApiCustomizedStrings")


@attr.s(auto_attribs=True)
class ApiCustomizedStrings:
    """Contains the string which are customized for each server. This is primarily the case
    for item names which can be customized for each server.

        Attributes:
            german (Union[Unset, None, ApiCustomizedStringsGerman]): Customized strings which should be used for the German
                localization.
            english (Union[Unset, None, ApiCustomizedStringsEnglish]): Customized strings which should be used for the
                English localization.
    """

    german: Union[Unset, None, "ApiCustomizedStringsGerman"] = UNSET
    english: Union[Unset, None, "ApiCustomizedStringsEnglish"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        german: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.german, Unset):
            german = self.german.to_dict() if self.german else None

        english: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.english, Unset):
            english = self.english.to_dict() if self.english else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if german is not UNSET:
            field_dict["German"] = german
        if english is not UNSET:
            field_dict["English"] = english

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_customized_strings_english import ApiCustomizedStringsEnglish
        from ..models.api_customized_strings_german import ApiCustomizedStringsGerman

        d = src_dict.copy()
        _german = d.pop("German", UNSET)
        german: Union[Unset, None, ApiCustomizedStringsGerman]
        if _german is None:
            german = None
        elif isinstance(_german, Unset):
            german = UNSET
        else:
            german = ApiCustomizedStringsGerman.from_dict(_german)

        _english = d.pop("English", UNSET)
        english: Union[Unset, None, ApiCustomizedStringsEnglish]
        if _english is None:
            english = None
        elif isinstance(_english, Unset):
            english = UNSET
        else:
            english = ApiCustomizedStringsEnglish.from_dict(_english)

        api_customized_strings = cls(
            german=german,
            english=english,
        )

        return api_customized_strings
