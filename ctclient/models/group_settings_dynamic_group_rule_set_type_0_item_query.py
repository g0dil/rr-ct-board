from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.group_settings_dynamic_group_rule_set_type_0_item_query_method import (
    GroupSettingsDynamicGroupRuleSetType0ItemQueryMethod,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_settings_dynamic_group_rule_set_type_0_item_query_params import (
        GroupSettingsDynamicGroupRuleSetType0ItemQueryParams,
    )


T = TypeVar("T", bound="GroupSettingsDynamicGroupRuleSetType0ItemQuery")


@_attrs_define
class GroupSettingsDynamicGroupRuleSetType0ItemQuery:
    """
    Attributes:
        description (str | Unset):
        method (GroupSettingsDynamicGroupRuleSetType0ItemQueryMethod | Unset):
        params (GroupSettingsDynamicGroupRuleSetType0ItemQueryParams | Unset):
    """

    description: str | Unset = UNSET
    method: GroupSettingsDynamicGroupRuleSetType0ItemQueryMethod | Unset = UNSET
    params: GroupSettingsDynamicGroupRuleSetType0ItemQueryParams | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if method is not UNSET:
            field_dict["method"] = method
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_settings_dynamic_group_rule_set_type_0_item_query_params import (
            GroupSettingsDynamicGroupRuleSetType0ItemQueryParams,
        )

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _method = d.pop("method", UNSET)
        method: GroupSettingsDynamicGroupRuleSetType0ItemQueryMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = GroupSettingsDynamicGroupRuleSetType0ItemQueryMethod(_method)

        _params = d.pop("params", UNSET)
        params: GroupSettingsDynamicGroupRuleSetType0ItemQueryParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = GroupSettingsDynamicGroupRuleSetType0ItemQueryParams.from_dict(
                _params
            )

        group_settings_dynamic_group_rule_set_type_0_item_query = cls(
            description=description,
            method=method,
            params=params,
        )

        group_settings_dynamic_group_rule_set_type_0_item_query.additional_properties = d
        return group_settings_dynamic_group_rule_set_type_0_item_query

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
