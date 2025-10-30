from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linking_base_fetch_status import LinkingBaseFetchStatus

T = TypeVar("T", bound="LinkingBase")


@_attrs_define
class LinkingBase:
    """
    Attributes:
        fetch_status (LinkingBaseFetchStatus):
        url (str):
    """

    fetch_status: LinkingBaseFetchStatus
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fetch_status = self.fetch_status.value

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fetchStatus": fetch_status,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fetch_status = LinkingBaseFetchStatus(d.pop("fetchStatus"))

        url = d.pop("url")

        linking_base = cls(
            fetch_status=fetch_status,
            url=url,
        )

        linking_base.additional_properties = d
        return linking_base

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
