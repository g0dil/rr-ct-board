from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_groups_response_201_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_active import (
        PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultActive,
    )
    from ..models.post_groups_response_201_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_none import (
        PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultNone,
    )
    from ..models.post_groups_response_201_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_requested import (
        PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultRequested,
    )
    from ..models.post_groups_response_201_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_to_delete import (
        PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultToDelete,
    )
    from ..models.post_groups_response_201_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_waiting import (
        PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultWaiting,
    )


T = TypeVar(
    "T",
    bound="PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResult",
)


@_attrs_define
class PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResult:
    """
    Attributes:
        active (PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultActive | Unset):
        none (PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultNone | Unset):
        requested (PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultRequested |
            Unset):
        to_delete (PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultToDelete |
            Unset):
        waiting (PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultWaiting |
            Unset):
    """

    active: (
        PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultActive
        | Unset
    ) = UNSET
    none: (
        PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultNone
        | Unset
    ) = UNSET
    requested: (
        PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultRequested
        | Unset
    ) = UNSET
    to_delete: (
        PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultToDelete
        | Unset
    ) = UNSET
    waiting: (
        PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultWaiting
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
        from ..models.post_groups_response_201_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_active import (
            PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultActive,
        )
        from ..models.post_groups_response_201_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_none import (
            PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultNone,
        )
        from ..models.post_groups_response_201_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_requested import (
            PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultRequested,
        )
        from ..models.post_groups_response_201_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_to_delete import (
            PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultToDelete,
        )
        from ..models.post_groups_response_201_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result_waiting import (
            PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultWaiting,
        )

        d = dict(src_dict)
        _active = d.pop("active", UNSET)
        active: (
            PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultActive
            | Unset
        )
        if isinstance(_active, Unset):
            active = UNSET
        else:
            active = PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultActive.from_dict(
                _active
            )

        _none = d.pop("none", UNSET)
        none: (
            PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultNone
            | Unset
        )
        if isinstance(_none, Unset):
            none = UNSET
        else:
            none = PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultNone.from_dict(
                _none
            )

        _requested = d.pop("requested", UNSET)
        requested: (
            PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultRequested
            | Unset
        )
        if isinstance(_requested, Unset):
            requested = UNSET
        else:
            requested = PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultRequested.from_dict(
                _requested
            )

        _to_delete = d.pop("to_delete", UNSET)
        to_delete: (
            PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultToDelete
            | Unset
        )
        if isinstance(_to_delete, Unset):
            to_delete = UNSET
        else:
            to_delete = PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultToDelete.from_dict(
                _to_delete
            )

        _waiting = d.pop("waiting", UNSET)
        waiting: (
            PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultWaiting
            | Unset
        )
        if isinstance(_waiting, Unset):
            waiting = UNSET
        else:
            waiting = PostGroupsResponse201DataSettingsDynamicGroupRuleSetType0ItemProcessGroupAndQueryResultWaiting.from_dict(
                _waiting
            )

        post_groups_response_201_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result = cls(
            active=active,
            none=none,
            requested=requested,
            to_delete=to_delete,
            waiting=waiting,
        )

        post_groups_response_201_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result.additional_properties = d
        return post_groups_response_201_data_settings_dynamic_group_rule_set_type_0_item_process_group_and_query_result

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
