from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostWikiCategoryResponse200WikiCategory")


@_attrs_define
class PostWikiCategoryResponse200WikiCategory:
    """
    Attributes:
        campus_id (int | None):
        file_access_without_permission (bool):
        id (int):
        in_menu (bool):
        name (str):
        sort_key (int):
        name_translated (str | Unset):
    """

    campus_id: int | None
    file_access_without_permission: bool
    id: int
    in_menu: bool
    name: str
    sort_key: int
    name_translated: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campus_id: int | None
        campus_id = self.campus_id

        file_access_without_permission = self.file_access_without_permission

        id = self.id

        in_menu = self.in_menu

        name = self.name

        sort_key = self.sort_key

        name_translated = self.name_translated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "campusId": campus_id,
                "fileAccessWithoutPermission": file_access_without_permission,
                "id": id,
                "inMenu": in_menu,
                "name": name,
                "sortKey": sort_key,
            }
        )
        if name_translated is not UNSET:
            field_dict["nameTranslated"] = name_translated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_campus_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        campus_id = _parse_campus_id(d.pop("campusId"))

        file_access_without_permission = d.pop("fileAccessWithoutPermission")

        id = d.pop("id")

        in_menu = d.pop("inMenu")

        name = d.pop("name")

        sort_key = d.pop("sortKey")

        name_translated = d.pop("nameTranslated", UNSET)

        post_wiki_category_response_200_wiki_category = cls(
            campus_id=campus_id,
            file_access_without_permission=file_access_without_permission,
            id=id,
            in_menu=in_menu,
            name=name,
            sort_key=sort_key,
            name_translated=name_translated,
        )

        post_wiki_category_response_200_wiki_category.additional_properties = d
        return post_wiki_category_response_200_wiki_category

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
