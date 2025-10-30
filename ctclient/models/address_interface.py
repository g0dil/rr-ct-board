from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddressInterface")


@_attrs_define
class AddressInterface:
    """
    Attributes:
        city (None | str):
        country (None | str):
        district (None | str):
        latitude (None | str):
        longitude (None | str):
        name (None | str):
        street (None | str):
        zip_ (None | str):
    """

    city: None | str
    country: None | str
    district: None | str
    latitude: None | str
    longitude: None | str
    name: None | str
    street: None | str
    zip_: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        city: None | str
        city = self.city

        country: None | str
        country = self.country

        district: None | str
        district = self.district

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "city": city,
                "country": country,
                "district": district,
                "latitude": latitude,
                "longitude": longitude,
                "name": name,
                "street": street,
                "zip": zip_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        city = _parse_city(d.pop("city"))

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

        address_interface = cls(
            city=city,
            country=country,
            district=district,
            latitude=latitude,
            longitude=longitude,
            name=name,
            street=street,
            zip_=zip_,
        )

        address_interface.additional_properties = d
        return address_interface

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
