from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_website_data_body_domain_type import PostWebsiteDataBodyDomainType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostWebsiteDataBody")


@_attrs_define
class PostWebsiteDataBody:
    """
    Attributes:
        domain_id (int):
        domain_type (PostWebsiteDataBodyDomainType):
        additional_id (int | Unset):
    """

    domain_id: int
    domain_type: PostWebsiteDataBodyDomainType
    additional_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_id = self.domain_id

        domain_type = self.domain_type.value

        additional_id = self.additional_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domainId": domain_id,
                "domainType": domain_type,
            }
        )
        if additional_id is not UNSET:
            field_dict["additionalId"] = additional_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain_id = d.pop("domainId")

        domain_type = PostWebsiteDataBodyDomainType(d.pop("domainType"))

        additional_id = d.pop("additionalId", UNSET)

        post_website_data_body = cls(
            domain_id=domain_id,
            domain_type=domain_type,
            additional_id=additional_id,
        )

        post_website_data_body.additional_properties = d
        return post_website_data_body

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
