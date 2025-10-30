from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.address_update_color_type_0 import AddressUpdateColorType0
from ..models.address_update_color_type_1 import AddressUpdateColorType1

T = TypeVar("T", bound="AddressUpdate")


@_attrs_define
class AddressUpdate:
    """
    Attributes:
        addition (None | str):
        city (None | str):  Example: Hamburg.
        color (AddressUpdateColorType0 | AddressUpdateColorType1 | None):
        country (None | str): A country's ISO-code Example: DE.
        district (None | str):
        domain_identifier (str):
        domain_type (str):
        icon (None | str):  Example: house.
        latitude (None | str):  Example: 47.145.
        longitude (None | str):  Example: 23.179.
        name (None | str):  Example: Retreat Center.
        street (None | str):  Example: 14 Main St.
        zip_ (None | str):  Example: 12345.
        id (int):
    """

    addition: None | str
    city: None | str
    color: AddressUpdateColorType0 | AddressUpdateColorType1 | None
    country: None | str
    district: None | str
    domain_identifier: str
    domain_type: str
    icon: None | str
    latitude: None | str
    longitude: None | str
    name: None | str
    street: None | str
    zip_: None | str
    id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        addition: None | str
        addition = self.addition

        city: None | str
        city = self.city

        color: None | str
        if isinstance(self.color, AddressUpdateColorType0):
            color = self.color.value
        elif isinstance(self.color, AddressUpdateColorType1):
            color = self.color.value
        else:
            color = self.color

        country: None | str
        country = self.country

        district: None | str
        district = self.district

        domain_identifier = self.domain_identifier

        domain_type = self.domain_type

        icon: None | str
        icon = self.icon

        latitude: None | str
        latitude = self.latitude

        longitude: None | str
        longitude = self.longitude

        name: None | str
        name = self.name

        street: None | str
        street = self.street

        zip_: None | str
        zip_ = self.zip_

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "addition": addition,
                "city": city,
                "color": color,
                "country": country,
                "district": district,
                "domainIdentifier": domain_identifier,
                "domainType": domain_type,
                "icon": icon,
                "latitude": latitude,
                "longitude": longitude,
                "name": name,
                "street": street,
                "zip": zip_,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_addition(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        addition = _parse_addition(d.pop("addition"))

        def _parse_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        city = _parse_city(d.pop("city"))

        def _parse_color(
            data: object,
        ) -> AddressUpdateColorType0 | AddressUpdateColorType1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                color_type_0 = AddressUpdateColorType0(data)

                return color_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                color_type_1 = AddressUpdateColorType1(data)

                return color_type_1
            except:  # noqa: E722
                pass
            return cast(AddressUpdateColorType0 | AddressUpdateColorType1 | None, data)

        color = _parse_color(d.pop("color"))

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        def _parse_district(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        district = _parse_district(d.pop("district"))

        domain_identifier = d.pop("domainIdentifier")

        domain_type = d.pop("domainType")

        def _parse_icon(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        icon = _parse_icon(d.pop("icon"))

        def _parse_latitude(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        latitude = _parse_latitude(d.pop("latitude"))

        def _parse_longitude(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        longitude = _parse_longitude(d.pop("longitude"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_street(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        street = _parse_street(d.pop("street"))

        def _parse_zip_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        zip_ = _parse_zip_(d.pop("zip"))

        id = d.pop("id")

        address_update = cls(
            addition=addition,
            city=city,
            color=color,
            country=country,
            district=district,
            domain_identifier=domain_identifier,
            domain_type=domain_type,
            icon=icon,
            latitude=latitude,
            longitude=longitude,
            name=name,
            street=street,
            zip_=zip_,
            id=id,
        )

        address_update.additional_properties = d
        return address_update

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
