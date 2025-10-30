from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutImageOptionsResponse200Data")


@_attrs_define
class PutImageOptionsResponse200Data:
    """
    Attributes:
        domain_identifier (str):
        domain_type (str):
        filename (str):
        id (int):
        name (str):
        security_level_id (int):
        size (int):
        url (str):
    """

    domain_identifier: str
    domain_type: str
    filename: str
    id: int
    name: str
    security_level_id: int
    size: int
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_identifier = self.domain_identifier

        domain_type = self.domain_type

        filename = self.filename

        id = self.id

        name = self.name

        security_level_id = self.security_level_id

        size = self.size

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domainIdentifier": domain_identifier,
                "domainType": domain_type,
                "filename": filename,
                "id": id,
                "name": name,
                "securityLevelId": security_level_id,
                "size": size,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain_identifier = d.pop("domainIdentifier")

        domain_type = d.pop("domainType")

        filename = d.pop("filename")

        id = d.pop("id")

        name = d.pop("name")

        security_level_id = d.pop("securityLevelId")

        size = d.pop("size")

        url = d.pop("url")

        put_image_options_response_200_data = cls(
            domain_identifier=domain_identifier,
            domain_type=domain_type,
            filename=filename,
            id=id,
            name=name,
            security_level_id=security_level_id,
            size=size,
            url=url,
        )

        put_image_options_response_200_data.additional_properties = d
        return put_image_options_response_200_data

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
