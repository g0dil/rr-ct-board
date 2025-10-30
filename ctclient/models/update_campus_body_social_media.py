from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateCampusBodySocialMedia")


@_attrs_define
class UpdateCampusBodySocialMedia:
    """Key-Value Pair, where key is the name of the network and value is the absolute link

    Attributes:
        social_network_name (str):
    """

    social_network_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        social_network_name = self.social_network_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "socialNetworkName": social_network_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        social_network_name = d.pop("socialNetworkName")

        update_campus_body_social_media = cls(
            social_network_name=social_network_name,
        )

        update_campus_body_social_media.additional_properties = d
        return update_campus_body_social_media

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
