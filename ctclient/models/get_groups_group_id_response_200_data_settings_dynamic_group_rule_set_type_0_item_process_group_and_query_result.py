from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_groups_group_id_response_200_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_active import (
        GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultActive,
    )
    from ..models.get_groups_group_id_response_200_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_none import (
        GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultNone,
    )
    from ..models.get_groups_group_id_response_200_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_requested import (
        GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultRequested,
    )
    from ..models.get_groups_group_id_response_200_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_to_delete import (
        GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultToDelete,
    )
    from ..models.get_groups_group_id_response_200_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_waiting import (
        GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultWaiting,
    )


T = TypeVar(
    "T",
    bound="GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResult",
)


@_attrs_define
class GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResult:
    """
    Attributes:
        active (GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultActive |
            Unset):
        none (GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultNone |
            Unset):
        requested
            (GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultRequested |
            Unset):
        to_delete (GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultToDelete
            | Unset):
        waiting (GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultWaiting |
            Unset):
    """

    active: (
        GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultActive
        | Unset
    ) = UNSET
    none: (
        GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultNone
        | Unset
    ) = UNSET
    requested: (
        GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultRequested
        | Unset
    ) = UNSET
    to_delete: (
        GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultToDelete
        | Unset
    ) = UNSET
    waiting: (
        GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultWaiting
        | Unset
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
        from ..models.get_groups_group_id_response_200_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_active import (
            GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultActive,
        )
        from ..models.get_groups_group_id_response_200_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_none import (
            GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultNone,
        )
        from ..models.get_groups_group_id_response_200_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_requested import (
            GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultRequested,
        )
        from ..models.get_groups_group_id_response_200_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_to_delete import (
            GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultToDelete,
        )
        from ..models.get_groups_group_id_response_200_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_waiting import (
            GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultWaiting,
        )

        d = dict(src_dict)
        _active = d.pop("active", UNSET)
        active: (
            GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultActive
            | Unset
        )
        if isinstance(_active, Unset):
            active = UNSET
        else:
            active = GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultActive.from_dict(
                _active
            )

        _none = d.pop("none", UNSET)
        none: (
            GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultNone
            | Unset
        )
        if isinstance(_none, Unset):
            none = UNSET
        else:
            none = GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultNone.from_dict(
                _none
            )

        _requested = d.pop("requested", UNSET)
        requested: (
            GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultRequested
            | Unset
        )
        if isinstance(_requested, Unset):
            requested = UNSET
        else:
            requested = GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultRequested.from_dict(
                _requested
            )

        _to_delete = d.pop("to_delete", UNSET)
        to_delete: (
            GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultToDelete
            | Unset
        )
        if isinstance(_to_delete, Unset):
            to_delete = UNSET
        else:
            to_delete = GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultToDelete.from_dict(
                _to_delete
            )

        _waiting = d.pop("waiting", UNSET)
        waiting: (
            GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultWaiting
            | Unset
        )
        if isinstance(_waiting, Unset):
            waiting = UNSET
        else:
            waiting = GetGroupsGroupIdResponse200DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultWaiting.from_dict(
                _waiting
            )

        get_groups_group_id_response_200_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result = cls(
            active=active,
            none=none,
            requested=requested,
            to_delete=to_delete,
            waiting=waiting,
        )

        get_groups_group_id_response_200_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result.additional_properties = d
        return get_groups_group_id_response_200_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result

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
