from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_settings_dynamic_group_rule_set_type_0_item_process_query_result_only_none import (
        GroupSettingsDynamicGroupRuleSetType0ItemProcessQueryResultOnlyNone,
    )


T = TypeVar(
    "T", bound="GroupSettingsDynamicGroupRuleSetType0ItemProcessQueryResultOnly"
)


@_attrs_define
class GroupSettingsDynamicGroupRuleSetType0ItemProcessQueryResultOnly:
    """
    Attributes:
        none (GroupSettingsDynamicGroupRuleSetType0ItemProcessQueryResultOnlyNone | Unset):
    """

    none: (
        GroupSettingsDynamicGroupRuleSetType0ItemProcessQueryResultOnlyNone | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        none: dict[str, Any] | Unset = UNSET
        if not isinstance(self.none, Unset):
            none = self.none.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if none is not UNSET:
            field_dict["none"] = none

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_settings_dynamic_group_rule_set_type_0_item_process_query_result_only_none import (
            GroupSettingsDynamicGroupRuleSetType0ItemProcessQueryResultOnlyNone,
        )

        d = dict(src_dict)
        _none = d.pop("none", UNSET)
        none: (
            GroupSettingsDynamicGroupRuleSetType0ItemProcessQueryResultOnlyNone | Unset
        )
        if isinstance(_none, Unset):
            none = UNSET
        else:
            none = GroupSettingsDynamicGroupRuleSetType0ItemProcessQueryResultOnlyNone.from_dict(
                _none
            )

        group_settings_dynamic_group_rule_set_type_0_item_process_query_result_only = (
            cls(
                none=none,
            )
        )

        group_settings_dynamic_group_rule_set_type_0_item_process_query_result_only.additional_properties = d
        return (
            group_settings_dynamic_group_rule_set_type_0_item_process_query_result_only
        )

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
