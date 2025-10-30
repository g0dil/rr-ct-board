from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_checkin_persons_body_group import PostCheckinPersonsBodyGroup
    from ..models.post_checkin_persons_body_person import PostCheckinPersonsBodyPerson


T = TypeVar("T", bound="PostCheckinPersonsBody")


@_attrs_define
class PostCheckinPersonsBody:
    """
    Attributes:
        group (PostCheckinPersonsBodyGroup):
        person (PostCheckinPersonsBodyPerson): See `POST /persons`
        tag_id (int):
    """

    group: PostCheckinPersonsBodyGroup
    person: PostCheckinPersonsBodyPerson
    tag_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group = self.group.to_dict()

        person = self.person.to_dict()

        tag_id = self.tag_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group": group,
                "person": person,
                "tagId": tag_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_checkin_persons_body_group import PostCheckinPersonsBodyGroup
        from ..models.post_checkin_persons_body_person import (
            PostCheckinPersonsBodyPerson,
        )

        d = dict(src_dict)
        group = PostCheckinPersonsBodyGroup.from_dict(d.pop("group"))

        person = PostCheckinPersonsBodyPerson.from_dict(d.pop("person"))

        tag_id = d.pop("tagId")

        post_checkin_persons_body = cls(
            group=group,
            person=person,
            tag_id=tag_id,
        )

        post_checkin_persons_body.additional_properties = d
        return post_checkin_persons_body

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
