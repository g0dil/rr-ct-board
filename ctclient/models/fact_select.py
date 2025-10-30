from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fact_select_type import FactSelectType

T = TypeVar("T", bound="FactSelect")


@_attrs_define
class FactSelect:
    """
    Attributes:
        id (float):
        name (str):
        name_translated (str):
        sort_key (int):
        options (list[str]):
        type_ (FactSelectType):
    """

    id: float
    name: str
    name_translated: str
    sort_key: int
    options: list[str]
    type_: FactSelectType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        name_translated = self.name_translated

        sort_key = self.sort_key

        options = self.options

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "nameTranslated": name_translated,
                "sortKey": sort_key,
                "options": options,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        name_translated = d.pop("nameTranslated")

        sort_key = d.pop("sortKey")

        options = cast(list[str], d.pop("options"))

        type_ = FactSelectType(d.pop("type"))

        fact_select = cls(
            id=id,
            name=name,
            name_translated=name_translated,
            sort_key=sort_key,
            options=options,
            type_=type_,
        )

        fact_select.additional_properties = d
        return fact_select

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
