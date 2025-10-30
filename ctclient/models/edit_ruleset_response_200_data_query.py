from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_ruleset_response_200_data_query_method import (
    EditRulesetResponse200DataQueryMethod,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edit_ruleset_response_200_data_query_params import (
        EditRulesetResponse200DataQueryParams,
    )


T = TypeVar("T", bound="EditRulesetResponse200DataQuery")


@_attrs_define
class EditRulesetResponse200DataQuery:
    """
    Attributes:
        description (str | Unset):
        method (EditRulesetResponse200DataQueryMethod | Unset):
        params (EditRulesetResponse200DataQueryParams | Unset):
    """

    description: str | Unset = UNSET
    method: EditRulesetResponse200DataQueryMethod | Unset = UNSET
    params: EditRulesetResponse200DataQueryParams | Unset = UNSET
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
        from ..models.edit_ruleset_response_200_data_query_params import (
            EditRulesetResponse200DataQueryParams,
        )

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _method = d.pop("method", UNSET)
        method: EditRulesetResponse200DataQueryMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = EditRulesetResponse200DataQueryMethod(_method)

        _params = d.pop("params", UNSET)
        params: EditRulesetResponse200DataQueryParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = EditRulesetResponse200DataQueryParams.from_dict(_params)

        edit_ruleset_response_200_data_query = cls(
            description=description,
            method=method,
            params=params,
        )

        edit_ruleset_response_200_data_query.additional_properties = d
        return edit_ruleset_response_200_data_query

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
