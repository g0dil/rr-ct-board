from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_routines_response_201_data_steps_item_type_1_action_key import (
    PostRoutinesResponse201DataStepsItemType1ActionKey,
)

if TYPE_CHECKING:
    from ..models.post_routines_response_201_data_steps_item_type_1_action_data import (
        PostRoutinesResponse201DataStepsItemType1ActionData,
    )
    from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_0 import (
        PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type0,
    )
    from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_1 import (
        PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type1,
    )
    from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_2 import (
        PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type2,
    )
    from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_3 import (
        PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type3,
    )
    from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_4 import (
        PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type4,
    )
    from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_5 import (
        PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type5,
    )
    from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_6 import (
        PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type6,
    )
    from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_1 import (
        PostRoutinesResponse201DataStepsItemType1ChildrenItemType1,
    )


T = TypeVar("T", bound="PostRoutinesResponse201DataStepsItemType1")


@_attrs_define
class PostRoutinesResponse201DataStepsItemType1:
    """
    Attributes:
        id (int):
        routine_id (int):
        action_data (PostRoutinesResponse201DataStepsItemType1ActionData):
        action_key (PostRoutinesResponse201DataStepsItemType1ActionKey):
        children (list[PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type0 |
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type1 |
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type2 |
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type3 |
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type4 |
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type5 |
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type6 |
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType1]):
        is_enabled (bool):
    """

    id: int
    routine_id: int
    action_data: PostRoutinesResponse201DataStepsItemType1ActionData
    action_key: PostRoutinesResponse201DataStepsItemType1ActionKey
    children: list[
        PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type0
        | PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type1
        | PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type2
        | PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type3
        | PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type4
        | PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type5
        | PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type6
        | PostRoutinesResponse201DataStepsItemType1ChildrenItemType1
    ]
    is_enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_0 import (
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type0,
        )
        from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_1 import (
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type1,
        )
        from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_2 import (
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type2,
        )
        from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_3 import (
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type3,
        )
        from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_4 import (
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type4,
        )
        from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_5 import (
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type5,
        )
        from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_6 import (
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type6,
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
                PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type0,
            ):
                children_item = children_item_data.to_dict()
            elif isinstance(
                children_item_data,
                PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type1,
            ):
                children_item = children_item_data.to_dict()
            elif isinstance(
                children_item_data,
                PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type2,
            ):
                children_item = children_item_data.to_dict()
            elif isinstance(
                children_item_data,
                PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type3,
            ):
                children_item = children_item_data.to_dict()
            elif isinstance(
                children_item_data,
                PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type4,
            ):
                children_item = children_item_data.to_dict()
            elif isinstance(
                children_item_data,
                PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type5,
            ):
                children_item = children_item_data.to_dict()
            elif isinstance(
                children_item_data,
                PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type6,
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
        from ..models.post_routines_response_201_data_steps_item_type_1_action_data import (
            PostRoutinesResponse201DataStepsItemType1ActionData,
        )
        from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_0 import (
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type0,
        )
        from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_1 import (
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type1,
        )
        from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_2 import (
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type2,
        )
        from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_3 import (
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type3,
        )
        from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_4 import (
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type4,
        )
        from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_5 import (
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type5,
        )
        from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_0_type_6 import (
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type6,
        )
        from ..models.post_routines_response_201_data_steps_item_type_1_children_item_type_1 import (
            PostRoutinesResponse201DataStepsItemType1ChildrenItemType1,
        )

        d = dict(src_dict)
        id = d.pop("id")

        routine_id = d.pop("routineId")

        action_data = PostRoutinesResponse201DataStepsItemType1ActionData.from_dict(
            d.pop("actionData")
        )

        action_key = PostRoutinesResponse201DataStepsItemType1ActionKey(
            d.pop("actionKey")
        )

        children = []
        _children = d.pop("children")
        for children_item_data in _children:

            def _parse_children_item(
                data: object,
            ) -> (
                PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type0
                | PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type1
                | PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type2
                | PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type3
                | PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type4
                | PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type5
                | PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type6
                | PostRoutinesResponse201DataStepsItemType1ChildrenItemType1
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    children_item_type_0_type_0 = PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type0.from_dict(
                        data
                    )

                    return children_item_type_0_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    children_item_type_0_type_1 = PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type1.from_dict(
                        data
                    )

                    return children_item_type_0_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    children_item_type_0_type_2 = PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type2.from_dict(
                        data
                    )

                    return children_item_type_0_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    children_item_type_0_type_3 = PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type3.from_dict(
                        data
                    )

                    return children_item_type_0_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    children_item_type_0_type_4 = PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type4.from_dict(
                        data
                    )

                    return children_item_type_0_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    children_item_type_0_type_5 = PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type5.from_dict(
                        data
                    )

                    return children_item_type_0_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    children_item_type_0_type_6 = PostRoutinesResponse201DataStepsItemType1ChildrenItemType0Type6.from_dict(
                        data
                    )

                    return children_item_type_0_type_6
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                children_item_type_1 = PostRoutinesResponse201DataStepsItemType1ChildrenItemType1.from_dict(
                    data
                )

                return children_item_type_1

            children_item = _parse_children_item(children_item_data)

            children.append(children_item)

        is_enabled = d.pop("isEnabled")

        post_routines_response_201_data_steps_item_type_1 = cls(
            id=id,
            routine_id=routine_id,
            action_data=action_data,
            action_key=action_key,
            children=children,
            is_enabled=is_enabled,
        )

        post_routines_response_201_data_steps_item_type_1.additional_properties = d
        return post_routines_response_201_data_steps_item_type_1

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
