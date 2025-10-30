from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgendaExportResponse200Data")


@_attrs_define
class AgendaExportResponse200Data:
    """
    Attributes:
        songs_with_multiple_files (list[str] | Unset):
        url (str | Unset):
    """

    songs_with_multiple_files: list[str] | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        songs_with_multiple_files: list[str] | Unset = UNSET
        if not isinstance(self.songs_with_multiple_files, Unset):
            songs_with_multiple_files = self.songs_with_multiple_files

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if songs_with_multiple_files is not UNSET:
            field_dict["songsWithMultipleFiles"] = songs_with_multiple_files
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        songs_with_multiple_files = cast(
            list[str], d.pop("songsWithMultipleFiles", UNSET)
        )

        url = d.pop("url", UNSET)

        agenda_export_response_200_data = cls(
            songs_with_multiple_files=songs_with_multiple_files,
            url=url,
        )

        agenda_export_response_200_data.additional_properties = d
        return agenda_export_response_200_data

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
