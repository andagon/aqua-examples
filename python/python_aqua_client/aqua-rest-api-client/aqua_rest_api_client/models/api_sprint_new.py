import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSprintNew")


@attr.s(auto_attribs=True)
class ApiSprintNew:
    """Contains necessery information to create a new sprint.

    Attributes:
        name (Union[Unset, None, str]): The name of the sprint.
        project_id (Union[Unset, int]): The project id.
        available_story_points (Union[Unset, int]): The number of story points per sprint.
        start (Union[Unset, None, datetime.datetime]): The date of the sprint start.
        end (Union[Unset, None, datetime.datetime]): The date of the sprint end.
        active (Union[Unset, bool]): Indicates that the sprint ist active.
        tags (Union[Unset, None, str]): Sprint tags.
        description (Union[Unset, None, str]): The description of the sprint.
    """

    name: Union[Unset, None, str] = UNSET
    project_id: Union[Unset, int] = UNSET
    available_story_points: Union[Unset, int] = UNSET
    start: Union[Unset, None, datetime.datetime] = UNSET
    end: Union[Unset, None, datetime.datetime] = UNSET
    active: Union[Unset, bool] = UNSET
    tags: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        project_id = self.project_id
        available_story_points = self.available_story_points
        start: Union[Unset, None, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat() if self.start else None

        end: Union[Unset, None, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat() if self.end else None

        active = self.active
        tags = self.tags
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if available_story_points is not UNSET:
            field_dict["AvailableStoryPoints"] = available_story_points
        if start is not UNSET:
            field_dict["Start"] = start
        if end is not UNSET:
            field_dict["End"] = end
        if active is not UNSET:
            field_dict["Active"] = active
        if tags is not UNSET:
            field_dict["Tags"] = tags
        if description is not UNSET:
            field_dict["Description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        project_id = d.pop("ProjectId", UNSET)

        available_story_points = d.pop("AvailableStoryPoints", UNSET)

        _start = d.pop("Start", UNSET)
        start: Union[Unset, None, datetime.datetime]
        if _start is None:
            start = None
        elif isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        _end = d.pop("End", UNSET)
        end: Union[Unset, None, datetime.datetime]
        if _end is None:
            end = None
        elif isinstance(_end, Unset):
            end = UNSET
        else:
            end = isoparse(_end)

        active = d.pop("Active", UNSET)

        tags = d.pop("Tags", UNSET)

        description = d.pop("Description", UNSET)

        api_sprint_new = cls(
            name=name,
            project_id=project_id,
            available_story_points=available_story_points,
            start=start,
            end=end,
            active=active,
            tags=tags,
            description=description,
        )

        return api_sprint_new
