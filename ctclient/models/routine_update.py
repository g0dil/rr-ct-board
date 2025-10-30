from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.routine_update_finish_item_type_1 import RoutineUpdateFinishItemType1
from ..models.routine_update_restart_item_type_1 import RoutineUpdateRestartItemType1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.routine_update_steps_item_type_0 import RoutineUpdateStepsItemType0
    from ..models.routine_update_steps_item_type_1 import RoutineUpdateStepsItemType1


T = TypeVar("T", bound="RoutineUpdate")


@_attrs_define
class RoutineUpdate:
    """
    Attributes:
        description (None | str | Unset):
        finish (list[int | RoutineUpdateFinishItemType1] | Unset):
        is_enabled (bool | Unset):  Default: False.
        name (str | Unset):
        priority (int | Unset):  Default: 0.
        restart (list[int | RoutineUpdateRestartItemType1] | Unset):
        steps (list[RoutineUpdateStepsItemType0 | RoutineUpdateStepsItemType1] | Unset):
    """

    description: None | str | Unset = UNSET
    finish: list[int | RoutineUpdateFinishItemType1] | Unset = UNSET
    is_enabled: bool | Unset = False
    name: str | Unset = UNSET
    priority: int | Unset = 0
    restart: list[int | RoutineUpdateRestartItemType1] | Unset = UNSET
    steps: list[RoutineUpdateStepsItemType0 | RoutineUpdateStepsItemType1] | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.routine_update_steps_item_type_0 import (
            RoutineUpdateStepsItemType0,
        )

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        finish: list[int | str] | Unset = UNSET
        if not isinstance(self.finish, Unset):
            finish = []
            for finish_item_data in self.finish:
                finish_item: int | str
                if isinstance(finish_item_data, RoutineUpdateFinishItemType1):
                    finish_item = finish_item_data.value
                else:
                    finish_item = finish_item_data
                finish.append(finish_item)

        is_enabled = self.is_enabled

        name = self.name

        priority = self.priority

        restart: list[int | str] | Unset = UNSET
        if not isinstance(self.restart, Unset):
            restart = []
            for restart_item_data in self.restart:
                restart_item: int | str
                if isinstance(restart_item_data, RoutineUpdateRestartItemType1):
                    restart_item = restart_item_data.value
                else:
                    restart_item = restart_item_data
                restart.append(restart_item)

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item: dict[str, Any]
                if isinstance(steps_item_data, RoutineUpdateStepsItemType0):
                    steps_item = steps_item_data.to_dict()
                else:
                    steps_item = steps_item_data.to_dict()

                steps.append(steps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if finish is not UNSET:
            field_dict["finish"] = finish
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if name is not UNSET:
            field_dict["name"] = name
        if priority is not UNSET:
            field_dict["priority"] = priority
        if restart is not UNSET:
            field_dict["restart"] = restart
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.routine_update_steps_item_type_0 import (
            RoutineUpdateStepsItemType0,
        )
        from ..models.routine_update_steps_item_type_1 import (
            RoutineUpdateStepsItemType1,
        )

        d = dict(src_dict)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        finish = []
        _finish = d.pop("finish", UNSET)
        for finish_item_data in _finish or []:

            def _parse_finish_item(data: object) -> int | RoutineUpdateFinishItemType1:
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    finish_item_type_1 = RoutineUpdateFinishItemType1(data)

                    return finish_item_type_1
                except:  # noqa: E722
                    pass
                return cast(int | RoutineUpdateFinishItemType1, data)

            finish_item = _parse_finish_item(finish_item_data)

            finish.append(finish_item)

        is_enabled = d.pop("isEnabled", UNSET)

        name = d.pop("name", UNSET)

        priority = d.pop("priority", UNSET)

        restart = []
        _restart = d.pop("restart", UNSET)
        for restart_item_data in _restart or []:

            def _parse_restart_item(
                data: object,
            ) -> int | RoutineUpdateRestartItemType1:
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    restart_item_type_1 = RoutineUpdateRestartItemType1(data)

                    return restart_item_type_1
                except:  # noqa: E722
                    pass
                return cast(int | RoutineUpdateRestartItemType1, data)

            restart_item = _parse_restart_item(restart_item_data)

            restart.append(restart_item)

        steps = []
        _steps = d.pop("steps", UNSET)
        for steps_item_data in _steps or []:

            def _parse_steps_item(
                data: object,
            ) -> RoutineUpdateStepsItemType0 | RoutineUpdateStepsItemType1:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_0 = RoutineUpdateStepsItemType0.from_dict(data)

                    return steps_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                steps_item_type_1 = RoutineUpdateStepsItemType1.from_dict(data)

                return steps_item_type_1

            steps_item = _parse_steps_item(steps_item_data)

            steps.append(steps_item)

        routine_update = cls(
            description=description,
            finish=finish,
            is_enabled=is_enabled,
            name=name,
            priority=priority,
            restart=restart,
            steps=steps,
        )

        routine_update.additional_properties = d
        return routine_update

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
