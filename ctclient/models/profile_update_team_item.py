from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_update_team_item_person import ProfileUpdateTeamItemPerson


T = TypeVar("T", bound="ProfileUpdateTeamItem")


@_attrs_define
class ProfileUpdateTeamItem:
    """
    Attributes:
        note (str):
        sort_key (int):
        person (ProfileUpdateTeamItemPerson | Unset): DomainObject
        person_id (int | Unset):
    """

    note: str
    sort_key: int
    person: ProfileUpdateTeamItemPerson | Unset = UNSET
    person_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        note = self.note

        sort_key = self.sort_key

        person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        person_id = self.person_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "note": note,
                "sortKey": sort_key,
            }
        )
        if person is not UNSET:
            field_dict["person"] = person
        if person_id is not UNSET:
            field_dict["personId"] = person_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_update_team_item_person import ProfileUpdateTeamItemPerson

        d = dict(src_dict)
        note = d.pop("note")

        sort_key = d.pop("sortKey")

        _person = d.pop("person", UNSET)
        person: ProfileUpdateTeamItemPerson | Unset
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = ProfileUpdateTeamItemPerson.from_dict(_person)

        person_id = d.pop("personId", UNSET)

        profile_update_team_item = cls(
            note=note,
            sort_key=sort_key,
            person=person,
            person_id=person_id,
        )

        profile_update_team_item.additional_properties = d
        return profile_update_team_item

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
