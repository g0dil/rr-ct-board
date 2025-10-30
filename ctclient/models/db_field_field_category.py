from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.db_field_field_category_intern_code import DbFieldFieldCategoryInternCode

T = TypeVar("T", bound="DbFieldFieldCategory")


@_attrs_define
class DbFieldFieldCategory:
    """
    Attributes:
        id (int):
        intern_code (DbFieldFieldCategoryInternCode): The intern code of the field category the field belongs to. This
            is used to define the category of the field.
        name (str):
        table (str):
    """

    id: int
    intern_code: DbFieldFieldCategoryInternCode
    name: str
    table: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        intern_code = self.intern_code.value

        name = self.name

        table = self.table

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "internCode": intern_code,
                "name": name,
                "table": table,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        intern_code = DbFieldFieldCategoryInternCode(d.pop("internCode"))

        name = d.pop("name")

        table = d.pop("table")

        db_field_field_category = cls(
            id=id,
            intern_code=intern_code,
            name=name,
            table=table,
        )

        db_field_field_category.additional_properties = d
        return db_field_field_category

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
