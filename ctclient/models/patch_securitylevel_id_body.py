from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchSecuritylevelIdBody")


@_attrs_define
class PatchSecuritylevelIdBody:
    """
    Attributes:
        forcereorder (bool | Unset):
        name (str | Unset):
        newid (int | Unset):
    """

    forcereorder: bool | Unset = UNSET
    name: str | Unset = UNSET
    newid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        forcereorder = self.forcereorder

        name = self.name

        newid = self.newid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if forcereorder is not UNSET:
            field_dict["forcereorder"] = forcereorder
        if name is not UNSET:
            field_dict["name"] = name
        if newid is not UNSET:
            field_dict["newid"] = newid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        forcereorder = d.pop("forcereorder", UNSET)

        name = d.pop("name", UNSET)

        newid = d.pop("newid", UNSET)

        patch_securitylevel_id_body = cls(
            forcereorder=forcereorder,
            name=name,
            newid=newid,
        )

        patch_securitylevel_id_body.additional_properties = d
        return patch_securitylevel_id_body

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
