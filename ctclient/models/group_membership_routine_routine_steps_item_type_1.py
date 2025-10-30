from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.group_membership_routine_routine_steps_item_type_1_action_key import (
    GroupMembershipRoutineRoutineStepsItemType1ActionKey,
)

if TYPE_CHECKING:
    from ..models.group_membership_routine_routine_steps_item_type_1_action_data import (
        GroupMembershipRoutineRoutineStepsItemType1ActionData,
    )
    from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_0 import (
        GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type0,
    )
    from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_1 import (
        GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type1,
    )
    from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_2 import (
        GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type2,
    )
    from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_3 import (
        GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type3,
    )
    from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_4 import (
        GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type4,
    )
    from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_5 import (
        GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type5,
    )
    from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_6 import (
        GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type6,
    )
    from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_1 import (
        GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType1,
    )


T = TypeVar("T", bound="GroupMembershipRoutineRoutineStepsItemType1")


@_attrs_define
class GroupMembershipRoutineRoutineStepsItemType1:
    """
    Attributes:
        id (int):
        routine_id (int):
        action_data (GroupMembershipRoutineRoutineStepsItemType1ActionData):
        action_key (GroupMembershipRoutineRoutineStepsItemType1ActionKey):
        children (list[GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type0 |
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type1 |
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type2 |
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type3 |
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type4 |
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type5 |
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type6 |
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType1]):
        is_enabled (bool):
    """

    id: int
    routine_id: int
    action_data: GroupMembershipRoutineRoutineStepsItemType1ActionData
    action_key: GroupMembershipRoutineRoutineStepsItemType1ActionKey
    children: list[
        GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type0
        | GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type1
        | GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type2
        | GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type3
        | GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type4
        | GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type5
        | GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type6
        | GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType1
    ]
    is_enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_0 import (
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type0,
        )
        from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_1 import (
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type1,
        )
        from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_2 import (
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type2,
        )
        from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_3 import (
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type3,
        )
        from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_4 import (
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type4,
        )
        from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_5 import (
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type5,
        )
        from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_6 import (
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type6,
        )

        id = self.id

        routine_id = self.routine_id

        action_data = self.action_data.to_dict()

        action_key = self.action_key.value

        children = []
        for children_item_data in self.children:
            children_item: dict[str, Any]
            if isinstance(
                children_item_data,
                GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type0,
            ):
                children_item = children_item_data.to_dict()
            elif isinstance(
                children_item_data,
                GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type1,
            ):
                children_item = children_item_data.to_dict()
            elif isinstance(
                children_item_data,
                GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type2,
            ):
                children_item = children_item_data.to_dict()
            elif isinstance(
                children_item_data,
                GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type3,
            ):
                children_item = children_item_data.to_dict()
            elif isinstance(
                children_item_data,
                GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type4,
            ):
                children_item = children_item_data.to_dict()
            elif isinstance(
                children_item_data,
                GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type5,
            ):
                children_item = children_item_data.to_dict()
            elif isinstance(
                children_item_data,
                GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type6,
            ):
                children_item = children_item_data.to_dict()
            else:
                children_item = children_item_data.to_dict()

            children.append(children_item)

        is_enabled = self.is_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "routineId": routine_id,
                "actionData": action_data,
                "actionKey": action_key,
                "children": children,
                "isEnabled": is_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_membership_routine_routine_steps_item_type_1_action_data import (
            GroupMembershipRoutineRoutineStepsItemType1ActionData,
        )
        from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_0 import (
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type0,
        )
        from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_1 import (
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type1,
        )
        from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_2 import (
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type2,
        )
        from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_3 import (
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type3,
        )
        from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_4 import (
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type4,
        )
        from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_5 import (
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type5,
        )
        from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_0_type_6 import (
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type6,
        )
        from ..models.group_membership_routine_routine_steps_item_type_1_children_item_type_1 import (
            GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType1,
        )

        d = dict(src_dict)
        id = d.pop("id")

        routine_id = d.pop("routineId")

        action_data = GroupMembershipRoutineRoutineStepsItemType1ActionData.from_dict(
            d.pop("actionData")
        )

        action_key = GroupMembershipRoutineRoutineStepsItemType1ActionKey(
            d.pop("actionKey")
        )

        children = []
        _children = d.pop("children")
        for children_item_data in _children:

            def _parse_children_item(
                data: object,
            ) -> (
                GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type0
                | GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type1
                | GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type2
                | GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type3
                | GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type4
                | GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type5
                | GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type6
                | GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType1
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    children_item_type_0_type_0 = GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type0.from_dict(
                        data
                    )

                    return children_item_type_0_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    children_item_type_0_type_1 = GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type1.from_dict(
                        data
                    )

                    return children_item_type_0_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    children_item_type_0_type_2 = GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type2.from_dict(
                        data
                    )

                    return children_item_type_0_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    children_item_type_0_type_3 = GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type3.from_dict(
                        data
                    )

                    return children_item_type_0_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    children_item_type_0_type_4 = GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type4.from_dict(
                        data
                    )

                    return children_item_type_0_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    children_item_type_0_type_5 = GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type5.from_dict(
                        data
                    )

                    return children_item_type_0_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    children_item_type_0_type_6 = GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType0Type6.from_dict(
                        data
                    )

                    return children_item_type_0_type_6
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                children_item_type_1 = GroupMembershipRoutineRoutineStepsItemType1ChildrenItemType1.from_dict(
                    data
                )

                return children_item_type_1

            children_item = _parse_children_item(children_item_data)

            children.append(children_item)

        is_enabled = d.pop("isEnabled")

        group_membership_routine_routine_steps_item_type_1 = cls(
            id=id,
            routine_id=routine_id,
            action_data=action_data,
            action_key=action_key,
            children=children,
            is_enabled=is_enabled,
        )

        group_membership_routine_routine_steps_item_type_1.additional_properties = d
        return group_membership_routine_routine_steps_item_type_1

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
