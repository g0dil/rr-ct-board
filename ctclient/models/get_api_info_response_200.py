from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_info_response_200_address import GetApiInfoResponse200Address


T = TypeVar("T", bound="GetApiInfoResponse200")


@_attrs_define
class GetApiInfoResponse200:
    """
    Attributes:
        address (GetApiInfoResponse200Address | Unset):
        build (str | Unset): Database Build Version Example: 31843.
        short_name (None | str | Unset):  Example: CT Church.
        site_name (str | Unset):  Example: ChuToo Church.
        version (str | Unset): ChurchTools Version Example: 3.123.0.
    """

    address: GetApiInfoResponse200Address | Unset = UNSET
    build: str | Unset = UNSET
    short_name: None | str | Unset = UNSET
    site_name: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        build = self.build

        short_name: None | str | Unset
        if isinstance(self.short_name, Unset):
            short_name = UNSET
        else:
            short_name = self.short_name

        site_name = self.site_name

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if build is not UNSET:
            field_dict["build"] = build
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_info_response_200_address import (
            GetApiInfoResponse200Address,
        )

        d = dict(src_dict)
        _address = d.pop("address", UNSET)
        address: GetApiInfoResponse200Address | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = GetApiInfoResponse200Address.from_dict(_address)

        build = d.pop("build", UNSET)

        def _parse_short_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        short_name = _parse_short_name(d.pop("shortName", UNSET))

        site_name = d.pop("siteName", UNSET)

        version = d.pop("version", UNSET)

        get_api_info_response_200 = cls(
            address=address,
            build=build,
            short_name=short_name,
            site_name=site_name,
            version=version,
        )

        get_api_info_response_200.additional_properties = d
        return get_api_info_response_200

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
