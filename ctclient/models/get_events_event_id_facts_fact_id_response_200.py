from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_events_event_id_facts_fact_id_response_200_event_fact import (
        GetEventsEventIdFactsFactIdResponse200EventFact,
    )


T = TypeVar("T", bound="GetEventsEventIdFactsFactIdResponse200")


@_attrs_define
class GetEventsEventIdFactsFactIdResponse200:
    """
    Attributes:
        data (GetEventsEventIdFactsFactIdResponse200EventFact | Unset): Fact entry for an event
    """

    data: GetEventsEventIdFactsFactIdResponse200EventFact | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_events_event_id_facts_fact_id_response_200_event_fact import (
            GetEventsEventIdFactsFactIdResponse200EventFact,
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: GetEventsEventIdFactsFactIdResponse200EventFact | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GetEventsEventIdFactsFactIdResponse200EventFact.from_dict(_data)

        get_events_event_id_facts_fact_id_response_200 = cls(
            data=data,
        )

        get_events_event_id_facts_fact_id_response_200.additional_properties = d
        return get_events_event_id_facts_fact_id_response_200

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
