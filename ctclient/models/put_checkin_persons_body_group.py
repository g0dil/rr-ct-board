from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.put_checkin_persons_body_group_fields import (
        PutCheckinPersonsBodyGroupFields,
    )
    from ..models.put_checkin_persons_body_group_person_fields import (
        PutCheckinPersonsBodyGroupPersonFields,
    )


T = TypeVar("T", bound="PutCheckinPersonsBodyGroup")


@_attrs_define
class PutCheckinPersonsBodyGroup:
    """
    Attributes:
        fields (PutCheckinPersonsBodyGroupFields): Key-Value mapping of group member fields. Key: field Id; Value: Input
        id (int):
        ignore_group_size (bool): If `true` the group size is ignored, and a person can be added to a full group.
            Default: False.
        person_fields (PutCheckinPersonsBodyGroupPersonFields): Key-Value Mapping of person fields in group. Key: Person
            field name; Value: Input
    """

    fields: PutCheckinPersonsBodyGroupFields
    id: int
    person_fields: PutCheckinPersonsBodyGroupPersonFields
    ignore_group_size: bool = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fields = self.fields.to_dict()

        id = self.id

        ignore_group_size = self.ignore_group_size

        person_fields = self.person_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fields": fields,
                "id": id,
                "ignoreGroupSize": ignore_group_size,
                "personFields": person_fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_checkin_persons_body_group_fields import (
            PutCheckinPersonsBodyGroupFields,
        )
        from ..models.put_checkin_persons_body_group_person_fields import (
            PutCheckinPersonsBodyGroupPersonFields,
        )

        d = dict(src_dict)
        fields = PutCheckinPersonsBodyGroupFields.from_dict(d.pop("fields"))

        id = d.pop("id")

        ignore_group_size = d.pop("ignoreGroupSize")

        person_fields = PutCheckinPersonsBodyGroupPersonFields.from_dict(
            d.pop("personFields")
        )

        put_checkin_persons_body_group = cls(
            fields=fields,
            id=id,
            ignore_group_size=ignore_group_size,
            person_fields=person_fields,
        )

        put_checkin_persons_body_group.additional_properties = d
        return put_checkin_persons_body_group

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
