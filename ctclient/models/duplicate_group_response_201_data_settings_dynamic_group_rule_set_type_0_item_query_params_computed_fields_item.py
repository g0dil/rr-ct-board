from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duplicate_group_response_201_data_settings_dynamic_group_rule_set_type_0_item_query_params_computed_fields_item_value import (
        DuplicateGroupResponse201DataSettingsDynamicGroupRuleSetType0ItemQueryParamsComputedFieldsItemValue,
    )


T = TypeVar(
    "T",
    bound="DuplicateGroupResponse201DataSettingsDynamicGroupRuleSetType0ItemQueryParamsComputedFieldsItem",
)


@_attrs_define
class DuplicateGroupResponse201DataSettingsDynamicGroupRuleSetType0ItemQueryParamsComputedFieldsItem:
    """
    Attributes:
        name (str | Unset):
        value (DuplicateGroupResponse201DataSettingsDynamicGroupRuleSetType0ItemQueryParamsComputedFieldsItemValue |
            Unset):
    """

    name: str | Unset = UNSET
    value: (
        DuplicateGroupResponse201DataSettingsDynamicGroupRuleSetType0ItemQueryParamsComputedFieldsItemValue
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.duplicate_group_response_201_data_settings_dynamic_group_rule_set_type_0_item_query_params_computed_fields_item_value import (
            DuplicateGroupResponse201DataSettingsDynamicGroupRuleSetType0ItemQueryParamsComputedFieldsItemValue,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _value = d.pop("value", UNSET)
        value: (
            DuplicateGroupResponse201DataSettingsDynamicGroupRuleSetType0ItemQueryParamsComputedFieldsItemValue
            | Unset
        )
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = DuplicateGroupResponse201DataSettingsDynamicGroupRuleSetType0ItemQueryParamsComputedFieldsItemValue.from_dict(
                _value
            )

        duplicate_group_response_201_data_settings_dynamic_group_rule_set_type_0_item_query_params_computed_fields_item = cls(
            name=name,
            value=value,
        )

        duplicate_group_response_201_data_settings_dynamic_group_rule_set_type_0_item_query_params_computed_fields_item.additional_properties = d
        return duplicate_group_response_201_data_settings_dynamic_group_rule_set_type_0_item_query_params_computed_fields_item

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
