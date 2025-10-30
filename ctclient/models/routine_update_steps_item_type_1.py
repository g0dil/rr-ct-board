from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.routine_update_steps_item_type_1_action_key import (
    RoutineUpdateStepsItemType1ActionKey,
)
from ..models.routine_update_steps_item_type_1_finish_item_type_1 import (
    RoutineUpdateStepsItemType1FinishItemType1,
)
from ..models.routine_update_steps_item_type_1_reposition_item_type_1 import (
    RoutineUpdateStepsItemType1RepositionItemType1,
)
from ..models.routine_update_steps_item_type_1_restart_item_type_1 import (
    RoutineUpdateStepsItemType1RestartItemType1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.routine_update_steps_item_type_1_action_data import (
        RoutineUpdateStepsItemType1ActionData,
    )
    from ..models.routine_update_steps_item_type_1_children_item import (
        RoutineUpdateStepsItemType1ChildrenItem,
    )


T = TypeVar("T", bound="RoutineUpdateStepsItemType1")


@_attrs_define
class RoutineUpdateStepsItemType1:
    """
    Attributes:
        action_data (RoutineUpdateStepsItemType1ActionData):
        action_key (RoutineUpdateStepsItemType1ActionKey):
        children (list[RoutineUpdateStepsItemType1ChildrenItem]):
        is_enabled (bool):
        finish (list[int | RoutineUpdateStepsItemType1FinishItemType1] | Unset):
        id (int | Unset):
        reposition (list[int | RoutineUpdateStepsItemType1RepositionItemType1] | Unset):
        restart (list[int | RoutineUpdateStepsItemType1RestartItemType1] | Unset):
    """

    action_data: RoutineUpdateStepsItemType1ActionData
    action_key: RoutineUpdateStepsItemType1ActionKey
    children: list[RoutineUpdateStepsItemType1ChildrenItem]
    is_enabled: bool
    finish: list[int | RoutineUpdateStepsItemType1FinishItemType1] | Unset = UNSET
    id: int | Unset = UNSET
    reposition: list[int | RoutineUpdateStepsItemType1RepositionItemType1] | Unset = (
        UNSET
    )
    restart: list[int | RoutineUpdateStepsItemType1RestartItemType1] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_data = self.action_data.to_dict()

        action_key = self.action_key.value

        children = []
        for children_item_data in self.children:
            children_item = children_item_data.to_dict()
            children.append(children_item)

        is_enabled = self.is_enabled

        finish: list[int | str] | Unset = UNSET
        if not isinstance(self.finish, Unset):
            finish = []
            for finish_item_data in self.finish:
                finish_item: int | str
                if isinstance(
                    finish_item_data, RoutineUpdateStepsItemType1FinishItemType1
                ):
                    finish_item = finish_item_data.value
                else:
                    finish_item = finish_item_data
                finish.append(finish_item)

        id = self.id

        reposition: list[int | str] | Unset = UNSET
        if not isinstance(self.reposition, Unset):
            reposition = []
            for reposition_item_data in self.reposition:
                reposition_item: int | str
                if isinstance(
                    reposition_item_data, RoutineUpdateStepsItemType1RepositionItemType1
                ):
                    reposition_item = reposition_item_data.value
                else:
                    reposition_item = reposition_item_data
                reposition.append(reposition_item)

        restart: list[int | str] | Unset = UNSET
        if not isinstance(self.restart, Unset):
            restart = []
            for restart_item_data in self.restart:
                restart_item: int | str
                if isinstance(
                    restart_item_data, RoutineUpdateStepsItemType1RestartItemType1
                ):
                    restart_item = restart_item_data.value
                else:
                    restart_item = restart_item_data
                restart.append(restart_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actionData": action_data,
                "actionKey": action_key,
                "children": children,
                "isEnabled": is_enabled,
            }
        )
        if finish is not UNSET:
            field_dict["finish"] = finish
        if id is not UNSET:
            field_dict["id"] = id
        if reposition is not UNSET:
            field_dict["reposition"] = reposition
        if restart is not UNSET:
            field_dict["restart"] = restart

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.routine_update_steps_item_type_1_action_data import (
            RoutineUpdateStepsItemType1ActionData,
        )
        from ..models.routine_update_steps_item_type_1_children_item import (
            RoutineUpdateStepsItemType1ChildrenItem,
        )

        d = dict(src_dict)
        action_data = RoutineUpdateStepsItemType1ActionData.from_dict(
            d.pop("actionData")
        )

        action_key = RoutineUpdateStepsItemType1ActionKey(d.pop("actionKey"))

        children = []
        _children = d.pop("children")
        for children_item_data in _children:
            children_item = RoutineUpdateStepsItemType1ChildrenItem.from_dict(
                children_item_data
            )

            children.append(children_item)

        is_enabled = d.pop("isEnabled")

        finish = []
        _finish = d.pop("finish", UNSET)
        for finish_item_data in _finish or []:

            def _parse_finish_item(
                data: object,
            ) -> int | RoutineUpdateStepsItemType1FinishItemType1:
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    finish_item_type_1 = RoutineUpdateStepsItemType1FinishItemType1(
                        data
                    )

                    return finish_item_type_1
                except:  # noqa: E722
                    pass
                return cast(int | RoutineUpdateStepsItemType1FinishItemType1, data)

            finish_item = _parse_finish_item(finish_item_data)

            finish.append(finish_item)

        id = d.pop("id", UNSET)

        reposition = []
        _reposition = d.pop("reposition", UNSET)
        for reposition_item_data in _reposition or []:

            def _parse_reposition_item(
                data: object,
            ) -> int | RoutineUpdateStepsItemType1RepositionItemType1:
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    reposition_item_type_1 = (
                        RoutineUpdateStepsItemType1RepositionItemType1(data)
                    )

                    return reposition_item_type_1
                except:  # noqa: E722
                    pass
                return cast(int | RoutineUpdateStepsItemType1RepositionItemType1, data)

            reposition_item = _parse_reposition_item(reposition_item_data)

            reposition.append(reposition_item)

        restart = []
        _restart = d.pop("restart", UNSET)
        for restart_item_data in _restart or []:

            def _parse_restart_item(
                data: object,
            ) -> int | RoutineUpdateStepsItemType1RestartItemType1:
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    restart_item_type_1 = RoutineUpdateStepsItemType1RestartItemType1(
                        data
                    )

                    return restart_item_type_1
                except:  # noqa: E722
                    pass
                return cast(int | RoutineUpdateStepsItemType1RestartItemType1, data)

            restart_item = _parse_restart_item(restart_item_data)

            restart.append(restart_item)

        routine_update_steps_item_type_1 = cls(
            action_data=action_data,
            action_key=action_key,
            children=children,
            is_enabled=is_enabled,
            finish=finish,
            id=id,
            reposition=reposition,
            restart=restart,
        )

        routine_update_steps_item_type_1.additional_properties = d
        return routine_update_steps_item_type_1

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
