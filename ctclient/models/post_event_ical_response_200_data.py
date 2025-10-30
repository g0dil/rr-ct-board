from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostEventIcalResponse200Data")


@_attrs_define
class PostEventIcalResponse200Data:
    """
    Attributes:
        attribute (str | Unset):  Example: rosterICalSecret.
        module (str | Unset):  Example: churchservice.
        value (str | Unset):  Example: QOkVUp7JVLf5Mg3s9ynS.
    """

    attribute: str | Unset = UNSET
    module: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute = self.attribute

        module = self.module

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute is not UNSET:
            field_dict["attribute"] = attribute
        if module is not UNSET:
            field_dict["module"] = module
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attribute = d.pop("attribute", UNSET)

        module = d.pop("module", UNSET)

        value = d.pop("value", UNSET)

        post_event_ical_response_200_data = cls(
            attribute=attribute,
            module=module,
            value=value,
        )

        post_event_ical_response_200_data.additional_properties = d
        return post_event_ical_response_200_data

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
