from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostEvangelischetermineValidatesettingsBody")


@_attrs_define
class PostEvangelischetermineValidatesettingsBody:
    """
    Attributes:
        api_key (str | Unset):
        url (str | Unset):
        vid (str | Unset):
    """

    api_key: str | Unset = UNSET
    url: str | Unset = UNSET
    vid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        url = self.url

        vid = self.vid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if url is not UNSET:
            field_dict["url"] = url
        if vid is not UNSET:
            field_dict["vid"] = vid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey", UNSET)

        url = d.pop("url", UNSET)

        vid = d.pop("vid", UNSET)

        post_evangelischetermine_validatesettings_body = cls(
            api_key=api_key,
            url=url,
            vid=vid,
        )

        post_evangelischetermine_validatesettings_body.additional_properties = d
        return post_evangelischetermine_validatesettings_body

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
