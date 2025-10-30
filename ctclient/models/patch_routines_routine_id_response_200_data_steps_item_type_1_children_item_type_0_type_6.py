from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_routines_routine_id_response_200_data_steps_item_type_1_children_item_type_0_type_6_action_key import (
    PatchRoutinesRoutineIdResponse200DataStepsItemType1ChildrenItemType0Type6ActionKey,
)

T = TypeVar(
    "T",
    bound="PatchRoutinesRoutineIdResponse200DataStepsItemType1ChildrenItemType0Type6",
)


@_attrs_define
class PatchRoutinesRoutineIdResponse200DataStepsItemType1ChildrenItemType0Type6:
    """
    Attributes:
        action_data (None):
        action_key (PatchRoutinesRoutineIdResponse200DataStepsItemType1ChildrenItemType0Type6ActionKey):
        is_enabled (bool):
    """

    action_data: None
    action_key: PatchRoutinesRoutineIdResponse200DataStepsItemType1ChildrenItemType0Type6ActionKey
    is_enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_data = self.action_data

        action_key = self.action_key.value

        is_enabled = self.is_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actionData": action_data,
                "actionKey": action_key,
                "isEnabled": is_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action_data = d.pop("actionData")

        action_key = PatchRoutinesRoutineIdResponse200DataStepsItemType1ChildrenItemType0Type6ActionKey(
            d.pop("actionKey")
        )

        is_enabled = d.pop("isEnabled")

        patch_routines_routine_id_response_200_data_steps_item_type_1_children_item_type_0_type_6 = cls(
            action_data=action_data,
            action_key=action_key,
            is_enabled=is_enabled,
        )

        patch_routines_routine_id_response_200_data_steps_item_type_1_children_item_type_0_type_6.additional_properties = d
        return patch_routines_routine_id_response_200_data_steps_item_type_1_children_item_type_0_type_6

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
