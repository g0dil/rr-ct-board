from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.put_checkin_persons_response_409_data import (
        PutCheckinPersonsResponse409Data,
    )


T = TypeVar("T", bound="PutCheckinPersonsResponse409")


@_attrs_define
class PutCheckinPersonsResponse409:
    """
    Attributes:
        data (PutCheckinPersonsResponse409Data):
    """

    data: PutCheckinPersonsResponse409Data
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_checkin_persons_response_409_data import (
            PutCheckinPersonsResponse409Data,
        )

        d = dict(src_dict)
        data = PutCheckinPersonsResponse409Data.from_dict(d.pop("data"))

        put_checkin_persons_response_409 = cls(
            data=data,
        )

        put_checkin_persons_response_409.additional_properties = d
        return put_checkin_persons_response_409

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
