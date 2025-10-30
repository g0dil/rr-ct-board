from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetGlobalPermissionsResponse200DataChurchresource")


@_attrs_define
class GetGlobalPermissionsResponse200DataChurchresource:
    """
    Attributes:
        administer_bookings (list[float]):
        assistance_mode (bool):
        create_bookings (list[float]):
        create_virtual_bookings (bool):
        edit_masterdata (bool):
        view (bool):
        view_resource (list[float]):
    """

    administer_bookings: list[float]
    assistance_mode: bool
    create_bookings: list[float]
    create_virtual_bookings: bool
    edit_masterdata: bool
    view: bool
    view_resource: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        administer_bookings = self.administer_bookings

        assistance_mode = self.assistance_mode

        create_bookings = self.create_bookings

        create_virtual_bookings = self.create_virtual_bookings

        edit_masterdata = self.edit_masterdata

        view = self.view

        view_resource = self.view_resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "administer bookings": administer_bookings,
                "assistance mode": assistance_mode,
                "create bookings": create_bookings,
                "create virtual bookings": create_virtual_bookings,
                "edit masterdata": edit_masterdata,
                "view": view,
                "view resource": view_resource,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        administer_bookings = cast(list[float], d.pop("administer bookings"))

        assistance_mode = d.pop("assistance mode")

        create_bookings = cast(list[float], d.pop("create bookings"))

        create_virtual_bookings = d.pop("create virtual bookings")

        edit_masterdata = d.pop("edit masterdata")

        view = d.pop("view")

        view_resource = cast(list[float], d.pop("view resource"))

        get_global_permissions_response_200_data_churchresource = cls(
            administer_bookings=administer_bookings,
            assistance_mode=assistance_mode,
            create_bookings=create_bookings,
            create_virtual_bookings=create_virtual_bookings,
            edit_masterdata=edit_masterdata,
            view=view,
            view_resource=view_resource,
        )

        get_global_permissions_response_200_data_churchresource.additional_properties = d
        return get_global_permissions_response_200_data_churchresource

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
