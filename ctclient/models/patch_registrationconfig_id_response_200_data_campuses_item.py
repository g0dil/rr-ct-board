from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PatchRegistrationconfigIdResponse200DataCampusesItem")


@_attrs_define
class PatchRegistrationconfigIdResponse200DataCampusesItem:
    """
    Attributes:
        campus_id (int):
        group_ids (list[int]):
    """

    campus_id: int
    group_ids: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campus_id = self.campus_id

        group_ids = self.group_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "campusId": campus_id,
                "groupIds": group_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        campus_id = d.pop("campusId")

        group_ids = cast(list[int], d.pop("groupIds"))

        patch_registrationconfig_id_response_200_data_campuses_item = cls(
            campus_id=campus_id,
            group_ids=group_ids,
        )

        patch_registrationconfig_id_response_200_data_campuses_item.additional_properties = d
        return patch_registrationconfig_id_response_200_data_campuses_item

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
