from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DomainObjectPayload")


@_attrs_define
class DomainObjectPayload:
    """
    Attributes:
        domain_identifiers (list[str]):
        domain_types (list[str]):
    """

    domain_identifiers: list[str]
    domain_types: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_identifiers = self.domain_identifiers

        domain_types = self.domain_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain_identifiers": domain_identifiers,
                "domain_types": domain_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain_identifiers = cast(list[str], d.pop("domain_identifiers"))

        domain_types = cast(list[str], d.pop("domain_types"))

        domain_object_payload = cls(
            domain_identifiers=domain_identifiers,
            domain_types=domain_types,
        )

        domain_object_payload.additional_properties = d
        return domain_object_payload

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
