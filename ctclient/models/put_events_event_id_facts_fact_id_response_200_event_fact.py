from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.put_events_event_id_facts_fact_id_response_200_event_fact_meta import (
        PutEventsEventIdFactsFactIdResponse200EventFactMeta,
    )


T = TypeVar("T", bound="PutEventsEventIdFactsFactIdResponse200EventFact")


@_attrs_define
class PutEventsEventIdFactsFactIdResponse200EventFact:
    """Fact entry for an event

    Attributes:
        event_id (int):
        fact_id (int):
        meta (PutEventsEventIdFactsFactIdResponse200EventFactMeta):  Example: {'createdDate': '2020-01-01T00:00:00Z',
            'createdPerson': {'id': 1}, 'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
        modified_date (datetime.datetime): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
            2022-10-19T12:00:00Z.
        modified_pid (int):
        value (float | str):
    """

    event_id: int
    fact_id: int
    meta: PutEventsEventIdFactsFactIdResponse200EventFactMeta
    modified_date: datetime.datetime
    modified_pid: int
    value: float | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_id = self.event_id

        fact_id = self.fact_id

        meta = self.meta.to_dict()

        modified_date = self.modified_date.isoformat()

        modified_pid = self.modified_pid

        value: float | str
        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventId": event_id,
                "factId": fact_id,
                "meta": meta,
                "modifiedDate": modified_date,
                "modifiedPid": modified_pid,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_events_event_id_facts_fact_id_response_200_event_fact_meta import (
            PutEventsEventIdFactsFactIdResponse200EventFactMeta,
        )

        d = dict(src_dict)
        event_id = d.pop("eventId")

        fact_id = d.pop("factId")

        meta = PutEventsEventIdFactsFactIdResponse200EventFactMeta.from_dict(
            d.pop("meta")
        )

        modified_date = isoparse(d.pop("modifiedDate"))

        modified_pid = d.pop("modifiedPid")

        def _parse_value(data: object) -> float | str:
            return cast(float | str, data)

        value = _parse_value(d.pop("value"))

        put_events_event_id_facts_fact_id_response_200_event_fact = cls(
            event_id=event_id,
            fact_id=fact_id,
            meta=meta,
            modified_date=modified_date,
            modified_pid=modified_pid,
            value=value,
        )

        put_events_event_id_facts_fact_id_response_200_event_fact.additional_properties = d
        return put_events_event_id_facts_fact_id_response_200_event_fact

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
