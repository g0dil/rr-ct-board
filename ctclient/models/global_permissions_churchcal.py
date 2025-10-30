from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GlobalPermissionsChurchcal")


@_attrs_define
class GlobalPermissionsChurchcal:
    """
    Attributes:
        admin_church_category (bool):
        admin_group_category (bool):
        admin_personal_category (bool):
        assistance_mode (bool):
        create_group_category (bool):
        create_personal_category (bool):
        edit_calendar_entry_template (list[float]):
        edit_category (list[float]):
        view (bool):
        view_category (list[float]):
    """

    admin_church_category: bool
    admin_group_category: bool
    admin_personal_category: bool
    assistance_mode: bool
    create_group_category: bool
    create_personal_category: bool
    edit_calendar_entry_template: list[float]
    edit_category: list[float]
    view: bool
    view_category: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin_church_category = self.admin_church_category

        admin_group_category = self.admin_group_category

        admin_personal_category = self.admin_personal_category

        assistance_mode = self.assistance_mode

        create_group_category = self.create_group_category

        create_personal_category = self.create_personal_category

        edit_calendar_entry_template = self.edit_calendar_entry_template

        edit_category = self.edit_category

        view = self.view

        view_category = self.view_category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "admin church category": admin_church_category,
                "admin group category": admin_group_category,
                "admin personal category": admin_personal_category,
                "assistance mode": assistance_mode,
                "create group category": create_group_category,
                "create personal category": create_personal_category,
                "edit calendar entry template": edit_calendar_entry_template,
                "edit category": edit_category,
                "view": view,
                "view category": view_category,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        admin_church_category = d.pop("admin church category")

        admin_group_category = d.pop("admin group category")

        admin_personal_category = d.pop("admin personal category")

        assistance_mode = d.pop("assistance mode")

        create_group_category = d.pop("create group category")

        create_personal_category = d.pop("create personal category")

        edit_calendar_entry_template = cast(
            list[float], d.pop("edit calendar entry template")
        )

        edit_category = cast(list[float], d.pop("edit category"))

        view = d.pop("view")

        view_category = cast(list[float], d.pop("view category"))

        global_permissions_churchcal = cls(
            admin_church_category=admin_church_category,
            admin_group_category=admin_group_category,
            admin_personal_category=admin_personal_category,
            assistance_mode=assistance_mode,
            create_group_category=create_group_category,
            create_personal_category=create_personal_category,
            edit_calendar_entry_template=edit_calendar_entry_template,
            edit_category=edit_category,
            view=view,
            view_category=view_category,
        )

        global_permissions_churchcal.additional_properties = d
        return global_permissions_churchcal

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
