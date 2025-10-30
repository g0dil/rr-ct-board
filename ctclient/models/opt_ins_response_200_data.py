from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.opt_ins_response_200_data_newsletter import (
        OptInsResponse200DataNewsletter,
    )
    from ..models.opt_ins_response_200_data_persons import OptInsResponse200DataPersons


T = TypeVar("T", bound="OptInsResponse200Data")


@_attrs_define
class OptInsResponse200Data:
    """
    Attributes:
        newsletter (OptInsResponse200DataNewsletter | Unset):
        persons (OptInsResponse200DataPersons | Unset):
    """

    newsletter: OptInsResponse200DataNewsletter | Unset = UNSET
    persons: OptInsResponse200DataPersons | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        newsletter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.newsletter, Unset):
            newsletter = self.newsletter.to_dict()

        persons: dict[str, Any] | Unset = UNSET
        if not isinstance(self.persons, Unset):
            persons = self.persons.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if newsletter is not UNSET:
            field_dict["newsletter"] = newsletter
        if persons is not UNSET:
            field_dict["persons"] = persons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.opt_ins_response_200_data_newsletter import (
            OptInsResponse200DataNewsletter,
        )
        from ..models.opt_ins_response_200_data_persons import (
            OptInsResponse200DataPersons,
        )

        d = dict(src_dict)
        _newsletter = d.pop("newsletter", UNSET)
        newsletter: OptInsResponse200DataNewsletter | Unset
        if isinstance(_newsletter, Unset):
            newsletter = UNSET
        else:
            newsletter = OptInsResponse200DataNewsletter.from_dict(_newsletter)

        _persons = d.pop("persons", UNSET)
        persons: OptInsResponse200DataPersons | Unset
        if isinstance(_persons, Unset):
            persons = UNSET
        else:
            persons = OptInsResponse200DataPersons.from_dict(_persons)

        opt_ins_response_200_data = cls(
            newsletter=newsletter,
            persons=persons,
        )

        opt_ins_response_200_data.additional_properties = d
        return opt_ins_response_200_data

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
