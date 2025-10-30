from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GlobalPermissionsChurchcheckin")


@_attrs_define
class GlobalPermissionsChurchcheckin:
    """
    Attributes:
        create_person (bool):
        edit_masterdata (bool):
        view (bool):
    """

    create_person: bool
    edit_masterdata: bool
    view: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_person = self.create_person

        edit_masterdata = self.edit_masterdata

        view = self.view

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "create person": create_person,
                "edit masterdata": edit_masterdata,
                "view": view,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create_person = d.pop("create person")

        edit_masterdata = d.pop("edit masterdata")

        view = d.pop("view")

        global_permissions_churchcheckin = cls(
            create_person=create_person,
            edit_masterdata=edit_masterdata,
            view=view,
        )

        global_permissions_churchcheckin.additional_properties = d
        return global_permissions_churchcheckin

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
