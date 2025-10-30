from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.person_duplicate_p1 import PersonDuplicateP1
    from ..models.person_duplicate_p2 import PersonDuplicateP2


T = TypeVar("T", bound="PersonDuplicate")


@_attrs_define
class PersonDuplicate:
    """
    Attributes:
        key (str):
        p1 (PersonDuplicateP1):
        p2 (PersonDuplicateP2):
        relationship_id (str | Unset):
    """

    key: str
    p1: PersonDuplicateP1
    p2: PersonDuplicateP2
    relationship_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        p1 = self.p1.to_dict()

        p2 = self.p2.to_dict()

        relationship_id = self.relationship_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "p1": p1,
                "p2": p2,
            }
        )
        if relationship_id is not UNSET:
            field_dict["relationshipId"] = relationship_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.person_duplicate_p1 import PersonDuplicateP1
        from ..models.person_duplicate_p2 import PersonDuplicateP2

        d = dict(src_dict)
        key = d.pop("key")

        p1 = PersonDuplicateP1.from_dict(d.pop("p1"))

        p2 = PersonDuplicateP2.from_dict(d.pop("p2"))

        relationship_id = d.pop("relationshipId", UNSET)

        person_duplicate = cls(
            key=key,
            p1=p1,
            p2=p2,
            relationship_id=relationship_id,
        )

        person_duplicate.additional_properties = d
        return person_duplicate

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
