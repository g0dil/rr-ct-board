from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalPersonPermissionsChurchservice")


@_attrs_define
class InternalPersonPermissionsChurchservice:
    """
    Attributes:
        see_workload (bool | Unset):
    """

    see_workload: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        see_workload = self.see_workload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if see_workload is not UNSET:
            field_dict["+see workload"] = see_workload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        see_workload = d.pop("+see workload", UNSET)

        internal_person_permissions_churchservice = cls(
            see_workload=see_workload,
        )

        internal_person_permissions_churchservice.additional_properties = d
        return internal_person_permissions_churchservice

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
