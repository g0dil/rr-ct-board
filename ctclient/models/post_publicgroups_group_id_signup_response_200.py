from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostPublicgroupsGroupIdSignupResponse200")


@_attrs_define
class PostPublicgroupsGroupIdSignupResponse200:
    """
    Attributes:
        group_homepage_hash (str | Unset): The hash of the group homepage. This allows the client to return to the group
            homepage.
    """

    group_homepage_hash: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_homepage_hash = self.group_homepage_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_homepage_hash is not UNSET:
            field_dict["groupHomepageHash"] = group_homepage_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_homepage_hash = d.pop("groupHomepageHash", UNSET)

        post_publicgroups_group_id_signup_response_200 = cls(
            group_homepage_hash=group_homepage_hash,
        )

        post_publicgroups_group_id_signup_response_200.additional_properties = d
        return post_publicgroups_group_id_signup_response_200

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
