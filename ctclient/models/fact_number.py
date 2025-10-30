from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fact_number_type import FactNumberType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FactNumber")


@_attrs_define
class FactNumber:
    """
    Attributes:
        id (float):
        name (str):
        name_translated (str):
        sort_key (int):
        type_ (FactNumberType):
        unit (str | Unset):
    """

    id: float
    name: str
    name_translated: str
    sort_key: int
    type_: FactNumberType
    unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        name_translated = self.name_translated

        sort_key = self.sort_key

        type_ = self.type_.value

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "nameTranslated": name_translated,
                "sortKey": sort_key,
                "type": type_,
            }
        )
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        name_translated = d.pop("nameTranslated")

        sort_key = d.pop("sortKey")

        type_ = FactNumberType(d.pop("type"))

        unit = d.pop("unit", UNSET)

        fact_number = cls(
            id=id,
            name=name,
            name_translated=name_translated,
            sort_key=sort_key,
            type_=type_,
            unit=unit,
        )

        fact_number.additional_properties = d
        return fact_number

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
