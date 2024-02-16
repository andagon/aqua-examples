from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTestScenarioExecutionStatistics")


@attr.s(auto_attribs=True)
class ApiTestScenarioExecutionStatistics:
    """
    Attributes:
        not_run (Union[Unset, int]):
        incomplete (Union[Unset, int]):
        failed (Union[Unset, int]):
        pass_ (Union[Unset, int]):
        queued (Union[Unset, int]):
        in_progress (Union[Unset, int]):
        aborted (Union[Unset, int]):
        blocked (Union[Unset, int]):
        waiting (Union[Unset, int]):
        not_applicable (Union[Unset, int]):
    """

    not_run: Union[Unset, int] = UNSET
    incomplete: Union[Unset, int] = UNSET
    failed: Union[Unset, int] = UNSET
    pass_: Union[Unset, int] = UNSET
    queued: Union[Unset, int] = UNSET
    in_progress: Union[Unset, int] = UNSET
    aborted: Union[Unset, int] = UNSET
    blocked: Union[Unset, int] = UNSET
    waiting: Union[Unset, int] = UNSET
    not_applicable: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        not_run = self.not_run
        incomplete = self.incomplete
        failed = self.failed
        pass_ = self.pass_
        queued = self.queued
        in_progress = self.in_progress
        aborted = self.aborted
        blocked = self.blocked
        waiting = self.waiting
        not_applicable = self.not_applicable

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if not_run is not UNSET:
            field_dict["NotRun"] = not_run
        if incomplete is not UNSET:
            field_dict["Incomplete"] = incomplete
        if failed is not UNSET:
            field_dict["Failed"] = failed
        if pass_ is not UNSET:
            field_dict["Pass"] = pass_
        if queued is not UNSET:
            field_dict["Queued"] = queued
        if in_progress is not UNSET:
            field_dict["InProgress"] = in_progress
        if aborted is not UNSET:
            field_dict["Aborted"] = aborted
        if blocked is not UNSET:
            field_dict["Blocked"] = blocked
        if waiting is not UNSET:
            field_dict["Waiting"] = waiting
        if not_applicable is not UNSET:
            field_dict["NotApplicable"] = not_applicable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        not_run = d.pop("NotRun", UNSET)

        incomplete = d.pop("Incomplete", UNSET)

        failed = d.pop("Failed", UNSET)

        pass_ = d.pop("Pass", UNSET)

        queued = d.pop("Queued", UNSET)

        in_progress = d.pop("InProgress", UNSET)

        aborted = d.pop("Aborted", UNSET)

        blocked = d.pop("Blocked", UNSET)

        waiting = d.pop("Waiting", UNSET)

        not_applicable = d.pop("NotApplicable", UNSET)

        api_test_scenario_execution_statistics = cls(
            not_run=not_run,
            incomplete=incomplete,
            failed=failed,
            pass_=pass_,
            queued=queued,
            in_progress=in_progress,
            aborted=aborted,
            blocked=blocked,
            waiting=waiting,
            not_applicable=not_applicable,
        )

        return api_test_scenario_execution_statistics
