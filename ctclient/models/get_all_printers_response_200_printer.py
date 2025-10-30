from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_all_printers_response_200_printer_meta import (
        GetAllPrintersResponse200PrinterMeta,
    )


T = TypeVar("T", bound="GetAllPrintersResponse200Printer")


@_attrs_define
class GetAllPrintersResponse200Printer:
    """A printer designated to print check-in codes

    Attributes:
        id (int | Unset):  Example: 42.
        location (str | Unset):  Example: Im Eingang.
        meta (GetAllPrintersResponse200PrinterMeta | Unset):  Example: {'createdDate': '2020-01-01T00:00:00Z',
            'createdPerson': {'id': 1}, 'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
        title (str | Unset):  Example: DruckerName.
    """

    id: int | Unset = UNSET
    location: str | Unset = UNSET
    meta: GetAllPrintersResponse200PrinterMeta | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        location = self.location

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if location is not UNSET:
            field_dict["location"] = location
        if meta is not UNSET:
            field_dict["meta"] = meta
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_all_printers_response_200_printer_meta import (
            GetAllPrintersResponse200PrinterMeta,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        location = d.pop("location", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: GetAllPrintersResponse200PrinterMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = GetAllPrintersResponse200PrinterMeta.from_dict(_meta)

        title = d.pop("title", UNSET)

        get_all_printers_response_200_printer = cls(
            id=id,
            location=location,
            meta=meta,
            title=title,
        )

        get_all_printers_response_200_printer.additional_properties = d
        return get_all_printers_response_200_printer

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
