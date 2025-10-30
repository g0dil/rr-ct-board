from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="PatchRoutinesRoutineIdResponse200DataStepsItemType1ChildrenItemType0Type0ActionData",
)


@_attrs_define
class PatchRoutinesRoutineIdResponse200DataStepsItemType1ChildrenItemType0Type0ActionData:
    """
    Attributes:
        body (str):
        group_id (int):
        subject (str):
        sender_id (int | Unset):
        template_id (int | Unset):
    """

    body: str
    group_id: int
    subject: str
    sender_id: int | Unset = UNSET
    template_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        group_id = self.group_id

        subject = self.subject

        sender_id = self.sender_id

        template_id = self.template_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
                "groupId": group_id,
                "subject": subject,
            }
        )
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id
        if template_id is not UNSET:
            field_dict["templateId"] = template_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body")

        group_id = d.pop("groupId")

        subject = d.pop("subject")

        sender_id = d.pop("senderId", UNSET)

        template_id = d.pop("templateId", UNSET)

        patch_routines_routine_id_response_200_data_steps_item_type_1_children_item_type_0_type_0_action_data = cls(
            body=body,
            group_id=group_id,
            subject=subject,
            sender_id=sender_id,
            template_id=template_id,
        )

        patch_routines_routine_id_response_200_data_steps_item_type_1_children_item_type_0_type_0_action_data.additional_properties = d
        return patch_routines_routine_id_response_200_data_steps_item_type_1_children_item_type_0_type_0_action_data

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
