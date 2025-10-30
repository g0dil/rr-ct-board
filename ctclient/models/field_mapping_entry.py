from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_mapping_entry_system import FieldMappingEntrySystem
from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldMappingEntry")


@_attrs_define
class FieldMappingEntry:
    """
    Attributes:
        from_ (str):
        id (int):
        system (FieldMappingEntrySystem):  Example: master.
        to (str):
        from_filter (str | Unset):
        others (list[Any] | Unset):
        to_filter (str | Unset):
        value_mapping (list[Any] | Unset):
    """

    from_: str
    id: int
    system: FieldMappingEntrySystem
    to: str
    from_filter: str | Unset = UNSET
    others: list[Any] | Unset = UNSET
    to_filter: str | Unset = UNSET
    value_mapping: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        id = self.id

        system = self.system.value

        to = self.to

        from_filter = self.from_filter

        others: list[Any] | Unset = UNSET
        if not isinstance(self.others, Unset):
            others = self.others

        to_filter = self.to_filter

        value_mapping: list[Any] | Unset = UNSET
        if not isinstance(self.value_mapping, Unset):
            value_mapping = self.value_mapping

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "id": id,
                "system": system,
                "to": to,
            }
        )
        if from_filter is not UNSET:
            field_dict["fromFilter"] = from_filter
        if others is not UNSET:
            field_dict["others"] = others
        if to_filter is not UNSET:
            field_dict["toFilter"] = to_filter
        if value_mapping is not UNSET:
            field_dict["valueMapping"] = value_mapping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = d.pop("from")

        id = d.pop("id")

        system = FieldMappingEntrySystem(d.pop("system"))

        to = d.pop("to")

        from_filter = d.pop("fromFilter", UNSET)

        others = cast(list[Any], d.pop("others", UNSET))

        to_filter = d.pop("toFilter", UNSET)

        value_mapping = cast(list[Any], d.pop("valueMapping", UNSET))

        field_mapping_entry = cls(
            from_=from_,
            id=id,
            system=system,
            to=to,
            from_filter=from_filter,
            others=others,
            to_filter=to_filter,
            value_mapping=value_mapping,
        )

        field_mapping_entry.additional_properties = d
        return field_mapping_entry

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
