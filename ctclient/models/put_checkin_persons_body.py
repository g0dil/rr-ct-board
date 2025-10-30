from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.put_checkin_persons_body_group import PutCheckinPersonsBodyGroup


T = TypeVar("T", bound="PutCheckinPersonsBody")


@_attrs_define
class PutCheckinPersonsBody:
    """
    Attributes:
        group (PutCheckinPersonsBodyGroup):
        person_id (int):
        tag_id (int):
    """

    group: PutCheckinPersonsBodyGroup
    person_id: int
    tag_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group = self.group.to_dict()

        person_id = self.person_id

        tag_id = self.tag_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group": group,
                "personId": person_id,
                "tagId": tag_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_checkin_persons_body_group import PutCheckinPersonsBodyGroup

        d = dict(src_dict)
        group = PutCheckinPersonsBodyGroup.from_dict(d.pop("group"))

        person_id = d.pop("personId")

        tag_id = d.pop("tagId")

        put_checkin_persons_body = cls(
            group=group,
            person_id=person_id,
            tag_id=tag_id,
        )

        put_checkin_persons_body.additional_properties = d
        return put_checkin_persons_body

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
