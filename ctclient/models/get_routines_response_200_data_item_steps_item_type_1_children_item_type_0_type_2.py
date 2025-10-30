from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_routines_response_200_data_item_steps_item_type_1_children_item_type_0_type_2_action_key import (
    GetRoutinesResponse200DataItemStepsItemType1ChildrenItemType0Type2ActionKey,
)

if TYPE_CHECKING:
    from ..models.get_routines_response_200_data_item_steps_item_type_1_children_item_type_0_type_2_action_data import (
        GetRoutinesResponse200DataItemStepsItemType1ChildrenItemType0Type2ActionData,
    )


T = TypeVar(
    "T", bound="GetRoutinesResponse200DataItemStepsItemType1ChildrenItemType0Type2"
)


@_attrs_define
class GetRoutinesResponse200DataItemStepsItemType1ChildrenItemType0Type2:
    """
    Attributes:
        action_data (GetRoutinesResponse200DataItemStepsItemType1ChildrenItemType0Type2ActionData):
        action_key (GetRoutinesResponse200DataItemStepsItemType1ChildrenItemType0Type2ActionKey):
        is_enabled (bool):
    """

    action_data: (
        GetRoutinesResponse200DataItemStepsItemType1ChildrenItemType0Type2ActionData
    )
    action_key: (
        GetRoutinesResponse200DataItemStepsItemType1ChildrenItemType0Type2ActionKey
    )
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
        from ..models.get_routines_response_200_data_item_steps_item_type_1_children_item_type_0_type_2_action_data import (
            GetRoutinesResponse200DataItemStepsItemType1ChildrenItemType0Type2ActionData,
        )

        d = dict(src_dict)
        action_data = GetRoutinesResponse200DataItemStepsItemType1ChildrenItemType0Type2ActionData.from_dict(
            d.pop("actionData")
        )

        action_key = (
            GetRoutinesResponse200DataItemStepsItemType1ChildrenItemType0Type2ActionKey(
                d.pop("actionKey")
            )
        )

        is_enabled = d.pop("isEnabled")

        get_routines_response_200_data_item_steps_item_type_1_children_item_type_0_type_2 = cls(
            action_data=action_data,
            action_key=action_key,
            is_enabled=is_enabled,
        )

        get_routines_response_200_data_item_steps_item_type_1_children_item_type_0_type_2.additional_properties = d
        return get_routines_response_200_data_item_steps_item_type_1_children_item_type_0_type_2

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
