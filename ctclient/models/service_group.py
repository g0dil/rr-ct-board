from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceGroup")


@_attrs_define
class ServiceGroup:
    """
    Attributes:
        campus_id (int | None | Unset):
        id (int | Unset):  Example: 3.
        name (str | Unset):  Example: Technik.
        only_visible_in_campus_filter (bool | Unset):
        sort_key (int | Unset):  Example: 30.
        view_all (bool | Unset):
    """

    campus_id: int | None | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    only_visible_in_campus_filter: bool | Unset = UNSET
    sort_key: int | Unset = UNSET
    view_all: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campus_id: int | None | Unset
        if isinstance(self.campus_id, Unset):
            campus_id = UNSET
        else:
            campus_id = self.campus_id

        id = self.id

        name = self.name

        only_visible_in_campus_filter = self.only_visible_in_campus_filter

        sort_key = self.sort_key

        view_all = self.view_all

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if campus_id is not UNSET:
            field_dict["campusId"] = campus_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if only_visible_in_campus_filter is not UNSET:
            field_dict["onlyVisibleInCampusFilter"] = only_visible_in_campus_filter
        if sort_key is not UNSET:
            field_dict["sortKey"] = sort_key
        if view_all is not UNSET:
            field_dict["viewAll"] = view_all

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_campus_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        campus_id = _parse_campus_id(d.pop("campusId", UNSET))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        only_visible_in_campus_filter = d.pop("onlyVisibleInCampusFilter", UNSET)

        sort_key = d.pop("sortKey", UNSET)

        view_all = d.pop("viewAll", UNSET)

        service_group = cls(
            campus_id=campus_id,
            id=id,
            name=name,
            only_visible_in_campus_filter=only_visible_in_campus_filter,
            sort_key=sort_key,
            view_all=view_all,
        )

        service_group.additional_properties = d
        return service_group

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
