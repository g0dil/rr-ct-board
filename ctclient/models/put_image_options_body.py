from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutImageOptionsBody")


@_attrs_define
class PutImageOptionsBody:
    """
    Attributes:
        image_options (str | Unset):  Example:
            {"crop":{"top":"0.0","left":"0.0","bottom":"0.0","right":"0.4"},"focus":{"x":"0.5","y":"0.5"}}.
    """

    image_options: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_options = self.image_options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_options is not UNSET:
            field_dict["image_options"] = image_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_options = d.pop("image_options", UNSET)

        put_image_options_body = cls(
            image_options=image_options,
        )

        put_image_options_body.additional_properties = d
        return put_image_options_body

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
