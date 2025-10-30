from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.role_update_type import RoleUpdateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RoleUpdate")


@_attrs_define
class RoleUpdate:
    """
    Attributes:
        group_type_id (int):  Example: 2.
        grow_path_id (int | None):  Example: 4.
        is_default (bool):
        is_hidden (bool):
        name (str):  Example: Leiter.
        shorty (str):  Example: L.
        sort_key (int):  Example: 1.
        type_ (RoleUpdateType):
        id (int):  Example: 16.
        is_leader (bool | Unset):
    """

    group_type_id: int
    grow_path_id: int | None
    is_default: bool
    is_hidden: bool
    name: str
    shorty: str
    sort_key: int
    type_: RoleUpdateType
    id: int
    is_leader: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_type_id = self.group_type_id

        grow_path_id: int | None
        grow_path_id = self.grow_path_id

        is_default = self.is_default

        is_hidden = self.is_hidden

        name = self.name

        shorty = self.shorty

        sort_key = self.sort_key

        type_ = self.type_.value

        id = self.id

        is_leader = self.is_leader

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groupTypeId": group_type_id,
                "growPathId": grow_path_id,
                "isDefault": is_default,
                "isHidden": is_hidden,
                "name": name,
                "shorty": shorty,
                "sortKey": sort_key,
                "type": type_,
                "id": id,
            }
        )
        if is_leader is not UNSET:
            field_dict["isLeader"] = is_leader

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_type_id = d.pop("groupTypeId")

        def _parse_grow_path_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        grow_path_id = _parse_grow_path_id(d.pop("growPathId"))

        is_default = d.pop("isDefault")

        is_hidden = d.pop("isHidden")

        name = d.pop("name")

        shorty = d.pop("shorty")

        sort_key = d.pop("sortKey")

        type_ = RoleUpdateType(d.pop("type"))

        id = d.pop("id")

        is_leader = d.pop("isLeader", UNSET)

        role_update = cls(
            group_type_id=group_type_id,
            grow_path_id=grow_path_id,
            is_default=is_default,
            is_hidden=is_hidden,
            name=name,
            shorty=shorty,
            sort_key=sort_key,
            type_=type_,
            id=id,
            is_leader=is_leader,
        )

        role_update.additional_properties = d
        return role_update

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
