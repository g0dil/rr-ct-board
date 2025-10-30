from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_internal_permissions_for_person_response_200_data_churchdb import (
        GetInternalPermissionsForPersonResponse200DataChurchdb,
    )
    from ..models.get_internal_permissions_for_person_response_200_data_churchservice import (
        GetInternalPermissionsForPersonResponse200DataChurchservice,
    )


T = TypeVar("T", bound="GetInternalPermissionsForPersonResponse200Data")


@_attrs_define
class GetInternalPermissionsForPersonResponse200Data:
    """
    Attributes:
        churchdb (GetInternalPermissionsForPersonResponse200DataChurchdb):
        churchservice (GetInternalPermissionsForPersonResponse200DataChurchservice):
    """

    churchdb: GetInternalPermissionsForPersonResponse200DataChurchdb
    churchservice: GetInternalPermissionsForPersonResponse200DataChurchservice
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        churchdb = self.churchdb.to_dict()

        churchservice = self.churchservice.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "churchdb": churchdb,
                "churchservice": churchservice,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_internal_permissions_for_person_response_200_data_churchdb import (
            GetInternalPermissionsForPersonResponse200DataChurchdb,
        )
        from ..models.get_internal_permissions_for_person_response_200_data_churchservice import (
            GetInternalPermissionsForPersonResponse200DataChurchservice,
        )

        d = dict(src_dict)
        churchdb = GetInternalPermissionsForPersonResponse200DataChurchdb.from_dict(
            d.pop("churchdb")
        )

        churchservice = (
            GetInternalPermissionsForPersonResponse200DataChurchservice.from_dict(
                d.pop("churchservice")
            )
        )

        get_internal_permissions_for_person_response_200_data = cls(
            churchdb=churchdb,
            churchservice=churchservice,
        )

        get_internal_permissions_for_person_response_200_data.additional_properties = d
        return get_internal_permissions_for_person_response_200_data

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
