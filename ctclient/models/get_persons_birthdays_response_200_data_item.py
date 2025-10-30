from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_persons_birthdays_response_200_data_item_person import (
        GetPersonsBirthdaysResponse200DataItemPerson,
    )


T = TypeVar("T", bound="GetPersonsBirthdaysResponse200DataItem")


@_attrs_define
class GetPersonsBirthdaysResponse200DataItem:
    """
    Attributes:
        age (int): Calculated age. (see note to that endpoint)
        date (str): Actually birthday
        type_ (str): Type of Date Example: birthday.
        person (GetPersonsBirthdaysResponse200DataItemPerson | Unset):
    """

    age: int
    date: str
    type_: str
    person: GetPersonsBirthdaysResponse200DataItemPerson | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        age = self.age

        date = self.date

        type_ = self.type_

        person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "age": age,
                "date": date,
                "type": type_,
            }
        )
        if person is not UNSET:
            field_dict["person"] = person

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_persons_birthdays_response_200_data_item_person import (
            GetPersonsBirthdaysResponse200DataItemPerson,
        )

        d = dict(src_dict)
        age = d.pop("age")

        date = d.pop("date")

        type_ = d.pop("type")

        _person = d.pop("person", UNSET)
        person: GetPersonsBirthdaysResponse200DataItemPerson | Unset
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = GetPersonsBirthdaysResponse200DataItemPerson.from_dict(_person)

        get_persons_birthdays_response_200_data_item = cls(
            age=age,
            date=date,
            type_=type_,
            person=person,
        )

        get_persons_birthdays_response_200_data_item.additional_properties = d
        return get_persons_birthdays_response_200_data_item

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
