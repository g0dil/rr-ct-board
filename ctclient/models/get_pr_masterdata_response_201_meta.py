from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPRMasterdataResponse201Meta")


@_attrs_define
class GetPRMasterdataResponse201Meta:
    """
    Attributes:
        associations (int | Unset):
        denominations (int | Unset):
        group_homepages (int | Unset):
        social_media (int | Unset):
        tags (int | Unset):
    """

    associations: int | Unset = UNSET
    denominations: int | Unset = UNSET
    group_homepages: int | Unset = UNSET
    social_media: int | Unset = UNSET
    tags: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        associations = self.associations

        denominations = self.denominations

        group_homepages = self.group_homepages

        social_media = self.social_media

        tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if associations is not UNSET:
            field_dict["associations"] = associations
        if denominations is not UNSET:
            field_dict["denominations"] = denominations
        if group_homepages is not UNSET:
            field_dict["groupHomepages"] = group_homepages
        if social_media is not UNSET:
            field_dict["socialMedia"] = social_media
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        associations = d.pop("associations", UNSET)

        denominations = d.pop("denominations", UNSET)

        group_homepages = d.pop("groupHomepages", UNSET)

        social_media = d.pop("socialMedia", UNSET)

        tags = d.pop("tags", UNSET)

        get_pr_masterdata_response_201_meta = cls(
            associations=associations,
            denominations=denominations,
            group_homepages=group_homepages,
            social_media=social_media,
            tags=tags,
        )

        get_pr_masterdata_response_201_meta.additional_properties = d
        return get_pr_masterdata_response_201_meta

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
