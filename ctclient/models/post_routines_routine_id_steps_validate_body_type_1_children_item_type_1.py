from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostRoutinesRoutineIdStepsValidateBodyType1ChildrenItemType1")


@_attrs_define
class PostRoutinesRoutineIdStepsValidateBodyType1ChildrenItemType1:
    """
    Attributes:
        id (int):
        routine_id (int):
    """

    id: int
    routine_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        routine_id = self.routine_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "routineId": routine_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        routine_id = d.pop("routineId")

        post_routines_routine_id_steps_validate_body_type_1_children_item_type_1 = cls(
            id=id,
            routine_id=routine_id,
        )

        post_routines_routine_id_steps_validate_body_type_1_children_item_type_1.additional_properties = d
        return post_routines_routine_id_steps_validate_body_type_1_children_item_type_1

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
