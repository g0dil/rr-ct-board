from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dynamic_group_rule_process_group_and_query_result import (
        DynamicGroupRuleProcessGroupAndQueryResult,
    )
    from ..models.dynamic_group_rule_process_group_only import (
        DynamicGroupRuleProcessGroupOnly,
    )
    from ..models.dynamic_group_rule_process_query_result_only import (
        DynamicGroupRuleProcessQueryResultOnly,
    )


T = TypeVar("T", bound="DynamicGroupRuleProcess")


@_attrs_define
class DynamicGroupRuleProcess:
    """
    Attributes:
        group_and_query_result (DynamicGroupRuleProcessGroupAndQueryResult | Unset):
        group_only (DynamicGroupRuleProcessGroupOnly | Unset):
        query_result_only (DynamicGroupRuleProcessQueryResultOnly | Unset):
    """

    group_and_query_result: DynamicGroupRuleProcessGroupAndQueryResult | Unset = UNSET
    group_only: DynamicGroupRuleProcessGroupOnly | Unset = UNSET
    query_result_only: DynamicGroupRuleProcessQueryResultOnly | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_and_query_result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_and_query_result, Unset):
            group_and_query_result = self.group_and_query_result.to_dict()

        group_only: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_only, Unset):
            group_only = self.group_only.to_dict()

        query_result_only: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_result_only, Unset):
            query_result_only = self.query_result_only.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_and_query_result is not UNSET:
            field_dict["groupAndQueryResult"] = group_and_query_result
        if group_only is not UNSET:
            field_dict["groupOnly"] = group_only
        if query_result_only is not UNSET:
            field_dict["queryResultOnly"] = query_result_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dynamic_group_rule_process_group_and_query_result import (
            DynamicGroupRuleProcessGroupAndQueryResult,
        )
        from ..models.dynamic_group_rule_process_group_only import (
            DynamicGroupRuleProcessGroupOnly,
        )
        from ..models.dynamic_group_rule_process_query_result_only import (
            DynamicGroupRuleProcessQueryResultOnly,
        )

        d = dict(src_dict)
        _group_and_query_result = d.pop("groupAndQueryResult", UNSET)
        group_and_query_result: DynamicGroupRuleProcessGroupAndQueryResult | Unset
        if isinstance(_group_and_query_result, Unset):
            group_and_query_result = UNSET
        else:
            group_and_query_result = (
                DynamicGroupRuleProcessGroupAndQueryResult.from_dict(
                    _group_and_query_result
                )
            )

        _group_only = d.pop("groupOnly", UNSET)
        group_only: DynamicGroupRuleProcessGroupOnly | Unset
        if isinstance(_group_only, Unset):
            group_only = UNSET
        else:
            group_only = DynamicGroupRuleProcessGroupOnly.from_dict(_group_only)

        _query_result_only = d.pop("queryResultOnly", UNSET)
        query_result_only: DynamicGroupRuleProcessQueryResultOnly | Unset
        if isinstance(_query_result_only, Unset):
            query_result_only = UNSET
        else:
            query_result_only = DynamicGroupRuleProcessQueryResultOnly.from_dict(
                _query_result_only
            )

        dynamic_group_rule_process = cls(
            group_and_query_result=group_and_query_result,
            group_only=group_only,
            query_result_only=query_result_only,
        )

        dynamic_group_rule_process.additional_properties = d
        return dynamic_group_rule_process

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
