from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiRichText")


@attr.s(auto_attribs=True)
class ApiRichText:
    """Contains some rich text. The rich text is provided in several different formats.
    When sending rich text to the server, the rich text must be provided in exactly
    one format.

        Attributes:
            html (Union[Unset, None, str]): Contains the description rendered as HTML. Images are included with standard
                image tags.
                When sending HTML to server, all images must be uploaded to the server first by posting
                to /api/Image. The returned URLs can then be included into the HTML.
            incompatible_rich_text_features (Union[Unset, bool]): Indicates that rich text features are used which are not
                supported by the REST API,
                e.g. comments. Information from the rich text might be missing in the HTML and
                plain text provided by the REST API. The rich text cannot be modified via the REST API.
            plain_text (Union[Unset, None, str]): Contains the description as plain text. The plain text does not contain
                any formatting or images.
    """

    html: Union[Unset, None, str] = UNSET
    incompatible_rich_text_features: Union[Unset, bool] = UNSET
    plain_text: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        html = self.html
        incompatible_rich_text_features = self.incompatible_rich_text_features
        plain_text = self.plain_text

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if html is not UNSET:
            field_dict["Html"] = html
        if incompatible_rich_text_features is not UNSET:
            field_dict["IncompatibleRichTextFeatures"] = incompatible_rich_text_features
        if plain_text is not UNSET:
            field_dict["PlainText"] = plain_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        html = d.pop("Html", UNSET)

        incompatible_rich_text_features = d.pop("IncompatibleRichTextFeatures", UNSET)

        plain_text = d.pop("PlainText", UNSET)

        api_rich_text = cls(
            html=html,
            incompatible_rich_text_features=incompatible_rich_text_features,
            plain_text=plain_text,
        )

        return api_rich_text
