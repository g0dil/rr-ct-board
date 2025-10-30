from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dynamic_group_rule_process_group_and_query_result_none_handle_membership import (
        DynamicGroupRuleProcessGroupAndQueryResultNoneHandleMembership,
    )


T = TypeVar("T", bound="DynamicGroupRuleProcessGroupAndQueryResultNone")


@_attrs_define
class DynamicGroupRuleProcessGroupAndQueryResultNone:
    """
    Attributes:
        handle_membership (DynamicGroupRuleProcessGroupAndQueryResultNoneHandleMembership | Unset):
    """

    handle_membership: (
        DynamicGroupRuleProcessGroupAndQueryResultNoneHandleMembership | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        handle_membership: dict[str, Any] | Unset = UNSET
        if not isinstance(self.handle_membership, Unset):
            handle_membership = self.handle_membership.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if handle_membership is not UNSET:
            field_dict["handleMembership"] = handle_membership

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dynamic_group_rule_process_group_and_query_result_none_handle_membership import (
            DynamicGroupRuleProcessGroupAndQueryResultNoneHandleMembership,
        )

        d = dict(src_dict)
        _handle_membership = d.pop("handleMembership", UNSET)
        handle_membership: (
            DynamicGroupRuleProcessGroupAndQueryResultNoneHandleMembership | Unset
        )
        if isinstance(_handle_membership, Unset):
            handle_membership = UNSET
        else:
            handle_membership = DynamicGroupRuleProcessGroupAndQueryResultNoneHandleMembership.from_dict(
                _handle_membership
            )

        dynamic_group_rule_process_group_and_query_result_none = cls(
            handle_membership=handle_membership,
        )

        dynamic_group_rule_process_group_and_query_result_none.additional_properties = d
        return dynamic_group_rule_process_group_and_query_result_none

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
