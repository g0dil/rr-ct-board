from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_routines_routine_id_body_steps_item_type_0_reposition_item_type_1 import (
    PatchRoutinesRoutineIdBodyStepsItemType0RepositionItemType1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchRoutinesRoutineIdBodyStepsItemType0")


@_attrs_define
class PatchRoutinesRoutineIdBodyStepsItemType0:
    """
    Attributes:
        id (int | Unset):
        reposition (list[int | PatchRoutinesRoutineIdBodyStepsItemType0RepositionItemType1] | Unset):
    """

    id: int | Unset = UNSET
    reposition: (
        list[int | PatchRoutinesRoutineIdBodyStepsItemType0RepositionItemType1] | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        reposition: list[int | str] | Unset = UNSET
        if not isinstance(self.reposition, Unset):
            reposition = []
            for reposition_item_data in self.reposition:
                reposition_item: int | str
                if isinstance(
                    reposition_item_data,
                    PatchRoutinesRoutineIdBodyStepsItemType0RepositionItemType1,
                ):
                    reposition_item = reposition_item_data.value
                else:
                    reposition_item = reposition_item_data
                reposition.append(reposition_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if reposition is not UNSET:
            field_dict["reposition"] = reposition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        reposition = []
        _reposition = d.pop("reposition", UNSET)
        for reposition_item_data in _reposition or []:

            def _parse_reposition_item(
                data: object,
            ) -> int | PatchRoutinesRoutineIdBodyStepsItemType0RepositionItemType1:
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    reposition_item_type_1 = (
                        PatchRoutinesRoutineIdBodyStepsItemType0RepositionItemType1(
                            data
                        )
                    )

                    return reposition_item_type_1
                except:  # noqa: E722
                    pass
                return cast(
                    int | PatchRoutinesRoutineIdBodyStepsItemType0RepositionItemType1,
                    data,
                )

            reposition_item = _parse_reposition_item(reposition_item_data)

            reposition.append(reposition_item)

        patch_routines_routine_id_body_steps_item_type_0 = cls(
            id=id,
            reposition=reposition,
        )

        patch_routines_routine_id_body_steps_item_type_0.additional_properties = d
        return patch_routines_routine_id_body_steps_item_type_0

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
