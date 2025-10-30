from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.routine_step_create_create_follow_up_action_key import (
    RoutineStepCreateCreateFollowUpActionKey,
)

if TYPE_CHECKING:
    from ..models.routine_step_create_create_follow_up_action_data import (
        RoutineStepCreateCreateFollowUpActionData,
    )


T = TypeVar("T", bound="RoutineStepCreateCreateFollowUp")


@_attrs_define
class RoutineStepCreateCreateFollowUp:
    """
    Attributes:
        action_data (RoutineStepCreateCreateFollowUpActionData):
        action_key (RoutineStepCreateCreateFollowUpActionKey):
        is_enabled (bool):
    """

    action_data: RoutineStepCreateCreateFollowUpActionData
    action_key: RoutineStepCreateCreateFollowUpActionKey
    is_enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_data = self.action_data.to_dict()

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
        from ..models.routine_step_create_create_follow_up_action_data import (
            RoutineStepCreateCreateFollowUpActionData,
        )

        d = dict(src_dict)
        action_data = RoutineStepCreateCreateFollowUpActionData.from_dict(
            d.pop("actionData")
        )

        action_key = RoutineStepCreateCreateFollowUpActionKey(d.pop("actionKey"))

        is_enabled = d.pop("isEnabled")

        routine_step_create_create_follow_up = cls(
            action_data=action_data,
            action_key=action_key,
            is_enabled=is_enabled,
        )

        routine_step_create_create_follow_up.additional_properties = d
        return routine_step_create_create_follow_up

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
