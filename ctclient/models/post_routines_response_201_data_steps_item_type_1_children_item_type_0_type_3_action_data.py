from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_3_action_data_status import (
    PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type3ActionDataStatus,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type3ActionData",
)


@_attrs_define
class PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type3ActionData:
    """Custom group member fields have their numeric field id as key

    Attributes:
        comment (str | Unset):
        group_id (int | Unset):
        role_id (int | Unset):
        status (PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type3ActionDataStatus | Unset):
    """

    comment: str | Unset = UNSET
    group_id: int | Unset = UNSET
    role_id: int | Unset = UNSET
    status: (
        PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type3ActionDataStatus
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        group_id = self.group_id

        role_id = self.role_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if role_id is not UNSET:
            field_dict["roleId"] = role_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment = d.pop("comment", UNSET)

        group_id = d.pop("groupId", UNSET)

        role_id = d.pop("roleId", UNSET)

        _status = d.pop("status", UNSET)
        status: (
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type3ActionDataStatus
            | Unset
        )
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type3ActionDataStatus(
                _status
            )

        post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_3_action_data = cls(
            comment=comment,
            group_id=group_id,
            role_id=role_id,
            status=status,
        )

        post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_3_action_data.additional_properties = d
        return post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_3_action_data

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
