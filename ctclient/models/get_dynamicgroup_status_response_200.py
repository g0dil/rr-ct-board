from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_dynamicgroup_status_response_200_dynamic_group_status import (
    GetDynamicgroupStatusResponse200DynamicGroupStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetDynamicgroupStatusResponse200")


@_attrs_define
class GetDynamicgroupStatusResponse200:
    """
    Attributes:
        dynamic_group_status (GetDynamicgroupStatusResponse200DynamicGroupStatus | Unset):
    """

    dynamic_group_status: GetDynamicgroupStatusResponse200DynamicGroupStatus | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dynamic_group_status: str | Unset = UNSET
        if not isinstance(self.dynamic_group_status, Unset):
            dynamic_group_status = self.dynamic_group_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dynamic_group_status is not UNSET:
            field_dict["dynamicGroupStatus"] = dynamic_group_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _dynamic_group_status = d.pop("dynamicGroupStatus", UNSET)
        dynamic_group_status: GetDynamicgroupStatusResponse200DynamicGroupStatus | Unset
        if isinstance(_dynamic_group_status, Unset):
            dynamic_group_status = UNSET
        else:
            dynamic_group_status = GetDynamicgroupStatusResponse200DynamicGroupStatus(
                _dynamic_group_status
            )

        get_dynamicgroup_status_response_200 = cls(
            dynamic_group_status=dynamic_group_status,
        )

        get_dynamicgroup_status_response_200.additional_properties = d
        return get_dynamicgroup_status_response_200

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
