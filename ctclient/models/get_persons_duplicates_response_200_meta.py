from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPersonsDuplicatesResponse200Meta")


@_attrs_define
class GetPersonsDuplicatesResponse200Meta:
    """
    Attributes:
        count (int | Unset):
        duration (int | Unset):
        evaluations (int | Unset):
        memory_used (str | Unset):
    """

    count: int | Unset = UNSET
    duration: int | Unset = UNSET
    evaluations: int | Unset = UNSET
    memory_used: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        duration = self.duration

        evaluations = self.evaluations

        memory_used = self.memory_used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if duration is not UNSET:
            field_dict["duration"] = duration
        if evaluations is not UNSET:
            field_dict["evaluations"] = evaluations
        if memory_used is not UNSET:
            field_dict["memory_used"] = memory_used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        duration = d.pop("duration", UNSET)

        evaluations = d.pop("evaluations", UNSET)

        memory_used = d.pop("memory_used", UNSET)

        get_persons_duplicates_response_200_meta = cls(
            count=count,
            duration=duration,
            evaluations=evaluations,
            memory_used=memory_used,
        )

        get_persons_duplicates_response_200_meta.additional_properties = d
        return get_persons_duplicates_response_200_meta

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
