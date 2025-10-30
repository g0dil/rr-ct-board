from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="EditRulesetBodyDynamicGroupRuleSetQueryParamsComputedFieldsItemValue"
)


@_attrs_define
class EditRulesetBodyDynamicGroupRuleSetQueryParamsComputedFieldsItemValue:
    """
    Attributes:
        stereotype (list[str] | Unset):
        title (str | Unset):
    """

    stereotype: list[str] | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stereotype: list[str] | Unset = UNSET
        if not isinstance(self.stereotype, Unset):
            stereotype = self.stereotype

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stereotype is not UNSET:
            field_dict["stereotype"] = stereotype
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stereotype = cast(list[str], d.pop("stereotype", UNSET))

        title = d.pop("title", UNSET)

        edit_ruleset_body_dynamic_group_rule_set_query_params_computed_fields_item_value = cls(
            stereotype=stereotype,
            title=title,
        )

        edit_ruleset_body_dynamic_group_rule_set_query_params_computed_fields_item_value.additional_properties = d
        return edit_ruleset_body_dynamic_group_rule_set_query_params_computed_fields_item_value

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
