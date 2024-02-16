from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_dashboard_ng_widget_binding import ApiDashboardNGWidgetBinding
    from ..models.api_widget_data import ApiWidgetData
    from ..models.api_widget_model import ApiWidgetModel


T = TypeVar("T", bound="ApiDashboardNGWidget")


@attr.s(auto_attribs=True)
class ApiDashboardNGWidget:
    """
    Attributes:
        id (Union[Unset, int]):
        title (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        binding (Union[Unset, None, ApiDashboardNGWidgetBinding]): Specifies the binding (project and folder) as well as
            recursive flag of a widget.
        model (Union[Unset, None, ApiWidgetModel]): Base class for all widget models.
        data (Union[Unset, None, ApiWidgetData]): Base class for all widget data classes.
    """

    id: Union[Unset, int] = UNSET
    title: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    binding: Union[Unset, None, "ApiDashboardNGWidgetBinding"] = UNSET
    model: Union[Unset, None, "ApiWidgetModel"] = UNSET
    data: Union[Unset, None, "ApiWidgetData"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        type = self.type
        binding: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.binding, Unset):
            binding = self.binding.to_dict() if self.binding else None

        model: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.to_dict() if self.model else None

        data: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict() if self.data else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if title is not UNSET:
            field_dict["Title"] = title
        if type is not UNSET:
            field_dict["Type"] = type
        if binding is not UNSET:
            field_dict["Binding"] = binding
        if model is not UNSET:
            field_dict["Model"] = model
        if data is not UNSET:
            field_dict["Data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_dashboard_ng_widget_binding import ApiDashboardNGWidgetBinding
        from ..models.api_widget_data import ApiWidgetData
        from ..models.api_widget_model import ApiWidgetModel

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        title = d.pop("Title", UNSET)

        type = d.pop("Type", UNSET)

        _binding = d.pop("Binding", UNSET)
        binding: Union[Unset, None, ApiDashboardNGWidgetBinding]
        if _binding is None:
            binding = None
        elif isinstance(_binding, Unset):
            binding = UNSET
        else:
            binding = ApiDashboardNGWidgetBinding.from_dict(_binding)

        _model = d.pop("Model", UNSET)
        model: Union[Unset, None, ApiWidgetModel]
        if _model is None:
            model = None
        elif isinstance(_model, Unset):
            model = UNSET
        else:
            model = ApiWidgetModel.from_dict(_model)

        _data = d.pop("Data", UNSET)
        data: Union[Unset, None, ApiWidgetData]
        if _data is None:
            data = None
        elif isinstance(_data, Unset):
            data = UNSET
        else:
            data = ApiWidgetData.from_dict(_data)

        api_dashboard_ng_widget = cls(
            id=id,
            title=title,
            type=type,
            binding=binding,
            model=model,
            data=data,
        )

        return api_dashboard_ng_widget
