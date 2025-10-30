from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutEventsEventIdFactsFactIdResponse400ErrorsItemArgs")


@_attrs_define
class PutEventsEventIdFactsFactIdResponse400ErrorsItemArgs:
    """
    Attributes:
        compare_identical (bool | Unset):
        haystack (list[str] | Unset):
        input_ (str | Unset):
    """

    compare_identical: bool | Unset = UNSET
    haystack: list[str] | Unset = UNSET
    input_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        compare_identical = self.compare_identical

        haystack: list[str] | Unset = UNSET
        if not isinstance(self.haystack, Unset):
            haystack = self.haystack

        input_ = self.input_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compare_identical is not UNSET:
            field_dict["compareIdentical"] = compare_identical
        if haystack is not UNSET:
            field_dict["haystack"] = haystack
        if input_ is not UNSET:
            field_dict["input"] = input_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        compare_identical = d.pop("compareIdentical", UNSET)

        haystack = cast(list[str], d.pop("haystack", UNSET))

        input_ = d.pop("input", UNSET)

        put_events_event_id_facts_fact_id_response_400_errors_item_args = cls(
            compare_identical=compare_identical,
            haystack=haystack,
            input_=input_,
        )

        put_events_event_id_facts_fact_id_response_400_errors_item_args.additional_properties = d
        return put_events_event_id_facts_fact_id_response_400_errors_item_args

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
