from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edit_ruleset_body_dynamic_group_rule_set import (
        EditRulesetBodyDynamicGroupRuleSet,
    )


T = TypeVar("T", bound="EditRulesetBody")


@_attrs_define
class EditRulesetBody:
    """
    Attributes:
        dynamic_group_rule_set (EditRulesetBodyDynamicGroupRuleSet | Unset):
    """

    dynamic_group_rule_set: EditRulesetBodyDynamicGroupRuleSet | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dynamic_group_rule_set: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dynamic_group_rule_set, Unset):
            dynamic_group_rule_set = self.dynamic_group_rule_set.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dynamic_group_rule_set is not UNSET:
            field_dict["dynamicGroupRuleSet"] = dynamic_group_rule_set

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edit_ruleset_body_dynamic_group_rule_set import (
            EditRulesetBodyDynamicGroupRuleSet,
        )

        d = dict(src_dict)
        _dynamic_group_rule_set = d.pop("dynamicGroupRuleSet", UNSET)
        dynamic_group_rule_set: EditRulesetBodyDynamicGroupRuleSet | Unset
        if isinstance(_dynamic_group_rule_set, Unset):
            dynamic_group_rule_set = UNSET
        else:
            dynamic_group_rule_set = EditRulesetBodyDynamicGroupRuleSet.from_dict(
                _dynamic_group_rule_set
            )

        edit_ruleset_body = cls(
            dynamic_group_rule_set=dynamic_group_rule_set,
        )

        edit_ruleset_body.additional_properties = d
        return edit_ruleset_body

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
