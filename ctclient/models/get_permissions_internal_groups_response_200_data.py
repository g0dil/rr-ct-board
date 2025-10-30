from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_permissions_internal_groups_response_200_data_churchdb import (
        GetPermissionsInternalGroupsResponse200DataChurchdb,
    )


T = TypeVar("T", bound="GetPermissionsInternalGroupsResponse200Data")


@_attrs_define
class GetPermissionsInternalGroupsResponse200Data:
    """
    Attributes:
        churchdb (GetPermissionsInternalGroupsResponse200DataChurchdb): Group Internal Permission, which Affect a Person
    """

    churchdb: GetPermissionsInternalGroupsResponse200DataChurchdb
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        churchdb = self.churchdb.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "churchdb": churchdb,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_permissions_internal_groups_response_200_data_churchdb import (
            GetPermissionsInternalGroupsResponse200DataChurchdb,
        )

        d = dict(src_dict)
        churchdb = GetPermissionsInternalGroupsResponse200DataChurchdb.from_dict(
            d.pop("churchdb")
        )

        get_permissions_internal_groups_response_200_data = cls(
            churchdb=churchdb,
        )

        get_permissions_internal_groups_response_200_data.additional_properties = d
        return get_permissions_internal_groups_response_200_data

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
