from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetFinanceDonatorsDonatorCoupleIdResponse200Data")


@_attrs_define
class GetFinanceDonatorsDonatorCoupleIdResponse200Data:
    """
    Attributes:
        attachments (str | Unset): URL to the attachment of the donation receipt Example:
            https://example.org/sites/default/files/downloader/4zqEyozpDElNMVYNdrr7.pdf.
        cover_letters (str | Unset): URL to the cover letter of the donation receipt Example:
            https://example.org/sites/default/files/downloader/t3wxiDIe00xcuXQjCbWl.pdf.
    """

    attachments: str | Unset = UNSET
    cover_letters: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attachments = self.attachments

        cover_letters = self.cover_letters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if cover_letters is not UNSET:
            field_dict["coverLetters"] = cover_letters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attachments = d.pop("attachments", UNSET)

        cover_letters = d.pop("coverLetters", UNSET)

        get_finance_donators_donator_couple_id_response_200_data = cls(
            attachments=attachments,
            cover_letters=cover_letters,
        )

        get_finance_donators_donator_couple_id_response_200_data.additional_properties = d
        return get_finance_donators_donator_couple_id_response_200_data

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
