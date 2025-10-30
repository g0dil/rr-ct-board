from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.calendar_create_type import CalendarCreateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarCreate")


@_attrs_define
class CalendarCreate:
    """
    Attributes:
        color (str): The color of the calendar in any css3 color format. mostly hex Example: #FF0000.
        name (str):
        sort_key (int):
        type_ (CalendarCreateType):
        campus_id (int | None | Unset):
        ev_termine_event_type_id (int | None | Unset):
        event_template_id (int | None | Unset):
        i_cal_source_url (None | str | Unset):
        sync_to_ev_termine (bool | Unset):
    """

    color: str
    name: str
    sort_key: int
    type_: CalendarCreateType
    campus_id: int | None | Unset = UNSET
    ev_termine_event_type_id: int | None | Unset = UNSET
    event_template_id: int | None | Unset = UNSET
    i_cal_source_url: None | str | Unset = UNSET
    sync_to_ev_termine: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color

        name = self.name

        sort_key = self.sort_key

        type_ = self.type_.value

        campus_id: int | None | Unset
        if isinstance(self.campus_id, Unset):
            campus_id = UNSET
        else:
            campus_id = self.campus_id

        ev_termine_event_type_id: int | None | Unset
        if isinstance(self.ev_termine_event_type_id, Unset):
            ev_termine_event_type_id = UNSET
        else:
            ev_termine_event_type_id = self.ev_termine_event_type_id

        event_template_id: int | None | Unset
        if isinstance(self.event_template_id, Unset):
            event_template_id = UNSET
        else:
            event_template_id = self.event_template_id

        i_cal_source_url: None | str | Unset
        if isinstance(self.i_cal_source_url, Unset):
            i_cal_source_url = UNSET
        else:
            i_cal_source_url = self.i_cal_source_url

        sync_to_ev_termine = self.sync_to_ev_termine

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "color": color,
                "name": name,
                "sortKey": sort_key,
                "type": type_,
            }
        )
        if campus_id is not UNSET:
            field_dict["campusId"] = campus_id
        if ev_termine_event_type_id is not UNSET:
            field_dict["evTermineEventTypeId"] = ev_termine_event_type_id
        if event_template_id is not UNSET:
            field_dict["eventTemplateId"] = event_template_id
        if i_cal_source_url is not UNSET:
            field_dict["iCalSourceUrl"] = i_cal_source_url
        if sync_to_ev_termine is not UNSET:
            field_dict["syncToEvTermine"] = sync_to_ev_termine

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = d.pop("color")

        name = d.pop("name")

        sort_key = d.pop("sortKey")

        type_ = CalendarCreateType(d.pop("type"))

        def _parse_campus_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        campus_id = _parse_campus_id(d.pop("campusId", UNSET))

        def _parse_ev_termine_event_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ev_termine_event_type_id = _parse_ev_termine_event_type_id(
            d.pop("evTermineEventTypeId", UNSET)
        )

        def _parse_event_template_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        event_template_id = _parse_event_template_id(d.pop("eventTemplateId", UNSET))

        def _parse_i_cal_source_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        i_cal_source_url = _parse_i_cal_source_url(d.pop("iCalSourceUrl", UNSET))

        sync_to_ev_termine = d.pop("syncToEvTermine", UNSET)

        calendar_create = cls(
            color=color,
            name=name,
            sort_key=sort_key,
            type_=type_,
            campus_id=campus_id,
            ev_termine_event_type_id=ev_termine_event_type_id,
            event_template_id=event_template_id,
            i_cal_source_url=i_cal_source_url,
            sync_to_ev_termine=sync_to_ev_termine,
        )

        calendar_create.additional_properties = d
        return calendar_create

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
