from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edit_ruleset_response_200_data_process_query_result_only_none import (
        EditRulesetResponse200DataProcessQueryResultOnlyNone,
    )


T = TypeVar("T", bound="EditRulesetResponse200DataProcessQueryResultOnly")


@_attrs_define
class EditRulesetResponse200DataProcessQueryResultOnly:
    """
    Attributes:
        none (EditRulesetResponse200DataProcessQueryResultOnlyNone | Unset):
    """

    none: EditRulesetResponse200DataProcessQueryResultOnlyNone | Unset = UNSET
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
        from ..models.edit_ruleset_response_200_data_process_query_result_only_none import (
            EditRulesetResponse200DataProcessQueryResultOnlyNone,
        )

        d = dict(src_dict)
        _none = d.pop("none", UNSET)
        none: EditRulesetResponse200DataProcessQueryResultOnlyNone | Unset
        if isinstance(_none, Unset):
            none = UNSET
        else:
            none = EditRulesetResponse200DataProcessQueryResultOnlyNone.from_dict(_none)

        edit_ruleset_response_200_data_process_query_result_only = cls(
            none=none,
        )

        edit_ruleset_response_200_data_process_query_result_only.additional_properties = d
        return edit_ruleset_response_200_data_process_query_result_only

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
