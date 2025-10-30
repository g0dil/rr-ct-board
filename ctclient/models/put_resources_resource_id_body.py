from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutResourcesResourceIdBody")


@_attrs_define
class PutResourcesResourceIdBody:
    """
    Attributes:
        name (str):  Example: Main Hall.
        resource_type_id (int):  Example: 2.
        sort_key (int):  Example: 1.
        admin_ids (list[int] | None | Unset):
        description (None | str | Unset):  Example: Car with 7 seats.
        i_cal_location (None | str | Unset):  Example: Location for iCal.
        is_auto_accept (bool | Unset):
        is_virtual (bool | Unset):
        location (None | str | Unset):  Example: Basement.
        needs_appointment (bool | Unset):
        random_string (None | str | Unset):  Example: vqLheW8SUGW3sUN10YVW.
    """

    name: str
    resource_type_id: int
    sort_key: int
    admin_ids: list[int] | None | Unset = UNSET
    description: None | str | Unset = UNSET
    i_cal_location: None | str | Unset = UNSET
    is_auto_accept: bool | Unset = UNSET
    is_virtual: bool | Unset = UNSET
    location: None | str | Unset = UNSET
    needs_appointment: bool | Unset = UNSET
    random_string: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        resource_type_id = self.resource_type_id

        sort_key = self.sort_key

        admin_ids: list[int] | None | Unset
        if isinstance(self.admin_ids, Unset):
            admin_ids = UNSET
        elif isinstance(self.admin_ids, list):
            admin_ids = self.admin_ids

        else:
            admin_ids = self.admin_ids

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        i_cal_location: None | str | Unset
        if isinstance(self.i_cal_location, Unset):
            i_cal_location = UNSET
        else:
            i_cal_location = self.i_cal_location

        is_auto_accept = self.is_auto_accept

        is_virtual = self.is_virtual

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        needs_appointment = self.needs_appointment

        random_string: None | str | Unset
        if isinstance(self.random_string, Unset):
            random_string = UNSET
        else:
            random_string = self.random_string

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "resourceTypeId": resource_type_id,
                "sortKey": sort_key,
            }
        )
        if admin_ids is not UNSET:
            field_dict["adminIds"] = admin_ids
        if description is not UNSET:
            field_dict["description"] = description
        if i_cal_location is not UNSET:
            field_dict["iCalLocation"] = i_cal_location
        if is_auto_accept is not UNSET:
            field_dict["isAutoAccept"] = is_auto_accept
        if is_virtual is not UNSET:
            field_dict["isVirtual"] = is_virtual
        if location is not UNSET:
            field_dict["location"] = location
        if needs_appointment is not UNSET:
            field_dict["needsAppointment"] = needs_appointment
        if random_string is not UNSET:
            field_dict["randomString"] = random_string

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        resource_type_id = d.pop("resourceTypeId")

        sort_key = d.pop("sortKey")

        def _parse_admin_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                admin_ids_type_0 = cast(list[int], data)

                return admin_ids_type_0
            except:  # noqa: E722
                pass
            return cast(list[int] | None | Unset, data)

        admin_ids = _parse_admin_ids(d.pop("adminIds", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_i_cal_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        i_cal_location = _parse_i_cal_location(d.pop("iCalLocation", UNSET))

        is_auto_accept = d.pop("isAutoAccept", UNSET)

        is_virtual = d.pop("isVirtual", UNSET)

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        needs_appointment = d.pop("needsAppointment", UNSET)

        def _parse_random_string(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        random_string = _parse_random_string(d.pop("randomString", UNSET))

        put_resources_resource_id_body = cls(
            name=name,
            resource_type_id=resource_type_id,
            sort_key=sort_key,
            admin_ids=admin_ids,
            description=description,
            i_cal_location=i_cal_location,
            is_auto_accept=is_auto_accept,
            is_virtual=is_virtual,
            location=location,
            needs_appointment=needs_appointment,
            random_string=random_string,
        )

        put_resources_resource_id_body.additional_properties = d
        return put_resources_resource_id_body

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
