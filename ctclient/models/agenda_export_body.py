from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgendaExportBody")


@_attrs_define
class AgendaExportBody:
    """
    Attributes:
        append_arrangement (bool | Unset):
        export_song (bool | Unset):
        with_category (bool | Unset):
    """

    append_arrangement: bool | Unset = UNSET
    export_song: bool | Unset = UNSET
    with_category: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        append_arrangement = self.append_arrangement

        export_song = self.export_song

        with_category = self.with_category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if append_arrangement is not UNSET:
            field_dict["appendArrangement"] = append_arrangement
        if export_song is not UNSET:
            field_dict["exportSong"] = export_song
        if with_category is not UNSET:
            field_dict["withCategory"] = with_category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        append_arrangement = d.pop("appendArrangement", UNSET)

        export_song = d.pop("exportSong", UNSET)

        with_category = d.pop("withCategory", UNSET)

        agenda_export_body = cls(
            append_arrangement=append_arrangement,
            export_song=export_song,
            with_category=with_category,
        )

        agenda_export_body.additional_properties = d
        return agenda_export_body

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
