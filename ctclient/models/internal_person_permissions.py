from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.internal_person_permissions_churchdb import (
        InternalPersonPermissionsChurchdb,
    )
    from ..models.internal_person_permissions_churchservice import (
        InternalPersonPermissionsChurchservice,
    )


T = TypeVar("T", bound="InternalPersonPermissions")


@_attrs_define
class InternalPersonPermissions:
    """
    Attributes:
        churchdb (InternalPersonPermissionsChurchdb):
        churchservice (InternalPersonPermissionsChurchservice):
    """

    churchdb: InternalPersonPermissionsChurchdb
    churchservice: InternalPersonPermissionsChurchservice
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
        from ..models.internal_person_permissions_churchdb import (
            InternalPersonPermissionsChurchdb,
        )
        from ..models.internal_person_permissions_churchservice import (
            InternalPersonPermissionsChurchservice,
        )

        d = dict(src_dict)
        churchdb = InternalPersonPermissionsChurchdb.from_dict(d.pop("churchdb"))

        churchservice = InternalPersonPermissionsChurchservice.from_dict(
            d.pop("churchservice")
        )

        internal_person_permissions = cls(
            churchdb=churchdb,
            churchservice=churchservice,
        )

        internal_person_permissions.additional_properties = d
        return internal_person_permissions

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
