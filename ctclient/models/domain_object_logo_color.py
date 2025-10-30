from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_object_logo_color_key import DomainObjectLogoColorKey
from ..models.domain_object_logo_color_shade import DomainObjectLogoColorShade

T = TypeVar("T", bound="DomainObjectLogoColor")


@_attrs_define
class DomainObjectLogoColor:
    """Value for Tailwind color

    Attributes:
        key (DomainObjectLogoColorKey): A color in ChurchTools
        shade (DomainObjectLogoColorShade):  Example: 500.
    """

    key: DomainObjectLogoColorKey
    shade: DomainObjectLogoColorShade
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key.value

        shade = self.shade.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "shade": shade,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = DomainObjectLogoColorKey(d.pop("key"))

        shade = DomainObjectLogoColorShade(d.pop("shade"))

        domain_object_logo_color = cls(
            key=key,
            shade=shade,
        )

        domain_object_logo_color.additional_properties = d
        return domain_object_logo_color

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
