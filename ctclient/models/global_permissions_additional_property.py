from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GlobalPermissionsAdditionalProperty")


@_attrs_define
class GlobalPermissionsAdditionalProperty:
    """A permission object for a specific custom module.

    Attributes:
        create_custom_category (bool):
        create_custom_data (list[float]):
        delete_custom_category (list[float]):
        delete_custom_data (list[float]):
        edit_custom_category (list[float]):
        edit_custom_data (list[float]):
        view (bool):
        view_custom_category (list[float]):
        view_custom_data (list[float]):
    """

    create_custom_category: bool
    create_custom_data: list[float]
    delete_custom_category: list[float]
    delete_custom_data: list[float]
    edit_custom_category: list[float]
    edit_custom_data: list[float]
    view: bool
    view_custom_category: list[float]
    view_custom_data: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_custom_category = self.create_custom_category

        create_custom_data = self.create_custom_data

        delete_custom_category = self.delete_custom_category

        delete_custom_data = self.delete_custom_data

        edit_custom_category = self.edit_custom_category

        edit_custom_data = self.edit_custom_data

        view = self.view

        view_custom_category = self.view_custom_category

        view_custom_data = self.view_custom_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "create custom category": create_custom_category,
                "create custom data": create_custom_data,
                "delete custom category": delete_custom_category,
                "delete custom data": delete_custom_data,
                "edit custom category": edit_custom_category,
                "edit custom data": edit_custom_data,
                "view": view,
                "view custom category": view_custom_category,
                "view custom data": view_custom_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create_custom_category = d.pop("create custom category")

        create_custom_data = cast(list[float], d.pop("create custom data"))

        delete_custom_category = cast(list[float], d.pop("delete custom category"))

        delete_custom_data = cast(list[float], d.pop("delete custom data"))

        edit_custom_category = cast(list[float], d.pop("edit custom category"))

        edit_custom_data = cast(list[float], d.pop("edit custom data"))

        view = d.pop("view")

        view_custom_category = cast(list[float], d.pop("view custom category"))

        view_custom_data = cast(list[float], d.pop("view custom data"))

        global_permissions_additional_property = cls(
            create_custom_category=create_custom_category,
            create_custom_data=create_custom_data,
            delete_custom_category=delete_custom_category,
            delete_custom_data=delete_custom_data,
            edit_custom_category=edit_custom_category,
            edit_custom_data=edit_custom_data,
            view=view,
            view_custom_category=view_custom_category,
            view_custom_data=view_custom_data,
        )

        global_permissions_additional_property.additional_properties = d
        return global_permissions_additional_property

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
