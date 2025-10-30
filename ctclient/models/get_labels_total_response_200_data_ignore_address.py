from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetLabelsTotalResponse200DataIgnoreAddress")


@_attrs_define
class GetLabelsTotalResponse200DataIgnoreAddress:
    """
    Attributes:
        combined_labels (int | Unset):
        total_labels (int | Unset):
    """

    combined_labels: int | Unset = UNSET
    total_labels: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        combined_labels = self.combined_labels

        total_labels = self.total_labels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if combined_labels is not UNSET:
            field_dict["combinedLabels"] = combined_labels
        if total_labels is not UNSET:
            field_dict["totalLabels"] = total_labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        combined_labels = d.pop("combinedLabels", UNSET)

        total_labels = d.pop("totalLabels", UNSET)

        get_labels_total_response_200_data_ignore_address = cls(
            combined_labels=combined_labels,
            total_labels=total_labels,
        )

        get_labels_total_response_200_data_ignore_address.additional_properties = d
        return get_labels_total_response_200_data_ignore_address

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
