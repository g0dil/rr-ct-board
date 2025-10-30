from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_website_data_response_200_data_domain_type import (
    PostWebsiteDataResponse200DataDomainType,
)

T = TypeVar("T", bound="PostWebsiteDataResponse200Data")


@_attrs_define
class PostWebsiteDataResponse200Data:
    """
    Attributes:
        domain_id (int):
        id (int):
        additional_id (int | None):
        domain_type (PostWebsiteDataResponse200DataDomainType):
    """

    domain_id: int
    id: int
    additional_id: int | None
    domain_type: PostWebsiteDataResponse200DataDomainType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_id = self.domain_id

        id = self.id

        additional_id: int | None
        additional_id = self.additional_id

        domain_type = self.domain_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domainId": domain_id,
                "id": id,
                "additionalId": additional_id,
                "domainType": domain_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain_id = d.pop("domainId")

        id = d.pop("id")

        def _parse_additional_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        additional_id = _parse_additional_id(d.pop("additionalId"))

        domain_type = PostWebsiteDataResponse200DataDomainType(d.pop("domainType"))

        post_website_data_response_200_data = cls(
            domain_id=domain_id,
            id=id,
            additional_id=additional_id,
            domain_type=domain_type,
        )

        post_website_data_response_200_data.additional_properties = d
        return post_website_data_response_200_data

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
