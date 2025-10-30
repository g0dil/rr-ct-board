from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutEventsEventIdServicerequestsRequestIdBody")


@_attrs_define
class PutEventsEventIdServicerequestsRequestIdBody:
    """
    Attributes:
        is_accepted (bool):
        name (None | str): Either `name` or `personId` need to be supplied.
        comment (None | str | Unset):
        person_id (int | None | Unset): Either `personId` or `name` need to be supplied.
    """

    is_accepted: bool
    name: None | str
    comment: None | str | Unset = UNSET
    person_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_accepted = self.is_accepted

        name: None | str
        name = self.name

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        person_id: int | None | Unset
        if isinstance(self.person_id, Unset):
            person_id = UNSET
        else:
            person_id = self.person_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isAccepted": is_accepted,
                "name": name,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if person_id is not UNSET:
            field_dict["personId"] = person_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_accepted = d.pop("isAccepted")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        def _parse_person_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        person_id = _parse_person_id(d.pop("personId", UNSET))

        put_events_event_id_servicerequests_request_id_body = cls(
            is_accepted=is_accepted,
            name=name,
            comment=comment,
            person_id=person_id,
        )

        put_events_event_id_servicerequests_request_id_body.additional_properties = d
        return put_events_event_id_servicerequests_request_id_body

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
