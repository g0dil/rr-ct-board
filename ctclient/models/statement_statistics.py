from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StatementStatistics")


@_attrs_define
class StatementStatistics:
    """
    Attributes:
        all_ (int):
        booked (int):
        ignored (int):
        open_ (int):
    """

    all_: int
    booked: int
    ignored: int
    open_: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_ = self.all_

        booked = self.booked

        ignored = self.ignored

        open_ = self.open_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "all": all_,
                "booked": booked,
                "ignored": ignored,
                "open": open_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        all_ = d.pop("all")

        booked = d.pop("booked")

        ignored = d.pop("ignored")

        open_ = d.pop("open")

        statement_statistics = cls(
            all_=all_,
            booked=booked,
            ignored=ignored,
            open_=open_,
        )

        statement_statistics.additional_properties = d
        return statement_statistics

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
