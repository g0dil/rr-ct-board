from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_candidates_response_200_person import (
        GetCandidatesResponse200Person,
    )


T = TypeVar("T", bound="GetCandidatesResponse200")


@_attrs_define
class GetCandidatesResponse200:
    """
    Attributes:
        event_date (str | Unset):
        event_service_id (int | Unset):
        event_title (str | Unset):
        person (GetCandidatesResponse200Person | Unset): Person Domain Object
    """

    event_date: str | Unset = UNSET
    event_service_id: int | Unset = UNSET
    event_title: str | Unset = UNSET
    person: GetCandidatesResponse200Person | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_date = self.event_date

        event_service_id = self.event_service_id

        event_title = self.event_title

        person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_date is not UNSET:
            field_dict["eventDate"] = event_date
        if event_service_id is not UNSET:
            field_dict["eventServiceId"] = event_service_id
        if event_title is not UNSET:
            field_dict["eventTitle"] = event_title
        if person is not UNSET:
            field_dict["person"] = person

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_candidates_response_200_person import (
            GetCandidatesResponse200Person,
        )

        d = dict(src_dict)
        event_date = d.pop("eventDate", UNSET)

        event_service_id = d.pop("eventServiceId", UNSET)

        event_title = d.pop("eventTitle", UNSET)

        _person = d.pop("person", UNSET)
        person: GetCandidatesResponse200Person | Unset
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = GetCandidatesResponse200Person.from_dict(_person)

        get_candidates_response_200 = cls(
            event_date=event_date,
            event_service_id=event_service_id,
            event_title=event_title,
            person=person,
        )

        get_candidates_response_200.additional_properties = d
        return get_candidates_response_200

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
