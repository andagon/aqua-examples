from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_dashboard_ng_size import ApiDashboardNGSize
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_dashboard_ng_share_project import ApiDashboardNGShareProject
    from ..models.api_dashboard_ng_widget import ApiDashboardNGWidget
    from ..models.api_user_info import ApiUserInfo


T = TypeVar("T", bound="ApiDashboardNG")


@attr.s(auto_attribs=True)
class ApiDashboardNG:
    """
    Attributes:
        id (Union[Unset, int]):
        title (Union[Unset, None, str]):
        size (Union[Unset, ApiDashboardNGSize]):
            This enum has the following values:
              - `Large`
              - `Medium`
              - `Small`
        widgets (Union[Unset, None, List['ApiDashboardNGWidget']]):
        project_shares (Union[Unset, None, List['ApiDashboardNGShareProject']]):
        owner (Union[Unset, None, ApiUserInfo]): The user information
        is_favourite (Union[Unset, bool]): True if the dashboard is marked as favourite by current user.
            Note: this property is ignored when saving. Please use specialized method instead
            (to set/unset dashboard as favourite).
    """

    id: Union[Unset, int] = UNSET
    title: Union[Unset, None, str] = UNSET
    size: Union[Unset, ApiDashboardNGSize] = UNSET
    widgets: Union[Unset, None, List["ApiDashboardNGWidget"]] = UNSET
    project_shares: Union[Unset, None, List["ApiDashboardNGShareProject"]] = UNSET
    owner: Union[Unset, None, "ApiUserInfo"] = UNSET
    is_favourite: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        size: Union[Unset, str] = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.value

        widgets: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.widgets, Unset):
            if self.widgets is None:
                widgets = None
            else:
                widgets = []
                for widgets_item_data in self.widgets:
                    widgets_item = widgets_item_data.to_dict()

                    widgets.append(widgets_item)

        project_shares: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.project_shares, Unset):
            if self.project_shares is None:
                project_shares = None
            else:
                project_shares = []
                for project_shares_item_data in self.project_shares:
                    project_shares_item = project_shares_item_data.to_dict()

                    project_shares.append(project_shares_item)

        owner: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict() if self.owner else None

        is_favourite = self.is_favourite

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if title is not UNSET:
            field_dict["Title"] = title
        if size is not UNSET:
            field_dict["Size"] = size
        if widgets is not UNSET:
            field_dict["Widgets"] = widgets
        if project_shares is not UNSET:
            field_dict["ProjectShares"] = project_shares
        if owner is not UNSET:
            field_dict["Owner"] = owner
        if is_favourite is not UNSET:
            field_dict["IsFavourite"] = is_favourite

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_dashboard_ng_share_project import ApiDashboardNGShareProject
        from ..models.api_dashboard_ng_widget import ApiDashboardNGWidget
        from ..models.api_user_info import ApiUserInfo

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        title = d.pop("Title", UNSET)

        _size = d.pop("Size", UNSET)
        size: Union[Unset, ApiDashboardNGSize]
        if isinstance(_size, Unset):
            size = UNSET
        else:
            size = ApiDashboardNGSize(_size)

        widgets = []
        _widgets = d.pop("Widgets", UNSET)
        for widgets_item_data in _widgets or []:
            widgets_item = ApiDashboardNGWidget.from_dict(widgets_item_data)

            widgets.append(widgets_item)

        project_shares = []
        _project_shares = d.pop("ProjectShares", UNSET)
        for project_shares_item_data in _project_shares or []:
            project_shares_item = ApiDashboardNGShareProject.from_dict(project_shares_item_data)

            project_shares.append(project_shares_item)

        _owner = d.pop("Owner", UNSET)
        owner: Union[Unset, None, ApiUserInfo]
        if _owner is None:
            owner = None
        elif isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = ApiUserInfo.from_dict(_owner)

        is_favourite = d.pop("IsFavourite", UNSET)

        api_dashboard_ng = cls(
            id=id,
            title=title,
            size=size,
            widgets=widgets,
            project_shares=project_shares,
            owner=owner,
            is_favourite=is_favourite,
        )

        return api_dashboard_ng
