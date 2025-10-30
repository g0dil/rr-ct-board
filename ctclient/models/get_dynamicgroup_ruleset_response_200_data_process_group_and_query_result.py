from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_dynamicgroup_ruleset_response_200_data_process_group_and_query_result_active import (
        GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultActive,
    )
    from ..models.get_dynamicgroup_ruleset_response_200_data_process_group_and_query_result_none import (
        GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultNone,
    )
    from ..models.get_dynamicgroup_ruleset_response_200_data_process_group_and_query_result_requested import (
        GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultRequested,
    )
    from ..models.get_dynamicgroup_ruleset_response_200_data_process_group_and_query_result_to_delete import (
        GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultToDelete,
    )
    from ..models.get_dynamicgroup_ruleset_response_200_data_process_group_and_query_result_waiting import (
        GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultWaiting,
    )


T = TypeVar(
    "T", bound="GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResult"
)


@_attrs_define
class GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResult:
    """
    Attributes:
        active (GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultActive | Unset):
        none (GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultNone | Unset):
        requested (GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultRequested | Unset):
        to_delete (GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultToDelete | Unset):
        waiting (GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultWaiting | Unset):
    """

    active: (
        GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultActive | Unset
    ) = UNSET
    none: (
        GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultNone | Unset
    ) = UNSET
    requested: (
        GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultRequested | Unset
    ) = UNSET
    to_delete: (
        GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultToDelete | Unset
    ) = UNSET
    waiting: (
        GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultWaiting | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active: dict[str, Any] | Unset = UNSET
        if not isinstance(self.active, Unset):
            active = self.active.to_dict()

        none: dict[str, Any] | Unset = UNSET
        if not isinstance(self.none, Unset):
            none = self.none.to_dict()

        requested: dict[str, Any] | Unset = UNSET
        if not isinstance(self.requested, Unset):
            requested = self.requested.to_dict()

        to_delete: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_delete, Unset):
            to_delete = self.to_delete.to_dict()

        waiting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.waiting, Unset):
            waiting = self.waiting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if none is not UNSET:
            field_dict["none"] = none
        if requested is not UNSET:
            field_dict["requested"] = requested
        if to_delete is not UNSET:
            field_dict["to_delete"] = to_delete
        if waiting is not UNSET:
            field_dict["waiting"] = waiting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_dynamicgroup_ruleset_response_200_data_process_group_and_query_result_active import (
            GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultActive,
        )
        from ..models.get_dynamicgroup_ruleset_response_200_data_process_group_and_query_result_none import (
            GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultNone,
        )
        from ..models.get_dynamicgroup_ruleset_response_200_data_process_group_and_query_result_requested import (
            GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultRequested,
        )
        from ..models.get_dynamicgroup_ruleset_response_200_data_process_group_and_query_result_to_delete import (
            GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultToDelete,
        )
        from ..models.get_dynamicgroup_ruleset_response_200_data_process_group_and_query_result_waiting import (
            GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultWaiting,
        )

        d = dict(src_dict)
        _active = d.pop("active", UNSET)
        active: (
            GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultActive
            | Unset
        )
        if isinstance(_active, Unset):
            active = UNSET
        else:
            active = GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultActive.from_dict(
                _active
            )

        _none = d.pop("none", UNSET)
        none: (
            GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultNone | Unset
        )
        if isinstance(_none, Unset):
            none = UNSET
        else:
            none = GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultNone.from_dict(
                _none
            )

        _requested = d.pop("requested", UNSET)
        requested: (
            GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultRequested
            | Unset
        )
        if isinstance(_requested, Unset):
            requested = UNSET
        else:
            requested = GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultRequested.from_dict(
                _requested
            )

        _to_delete = d.pop("to_delete", UNSET)
        to_delete: (
            GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultToDelete
            | Unset
        )
        if isinstance(_to_delete, Unset):
            to_delete = UNSET
        else:
            to_delete = GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultToDelete.from_dict(
                _to_delete
            )

        _waiting = d.pop("waiting", UNSET)
        waiting: (
            GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultWaiting
            | Unset
        )
        if isinstance(_waiting, Unset):
            waiting = UNSET
        else:
            waiting = GetDynamicgroupRulesetResponse200DataProcessGroupAndQueryResultWaiting.from_dict(
                _waiting
            )

        get_dynamicgroup_ruleset_response_200_data_process_group_and_query_result = cls(
            active=active,
            none=none,
            requested=requested,
            to_delete=to_delete,
            waiting=waiting,
        )

        get_dynamicgroup_ruleset_response_200_data_process_group_and_query_result.additional_properties = d
        return get_dynamicgroup_ruleset_response_200_data_process_group_and_query_result

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
