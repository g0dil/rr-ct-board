from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wiki_categories_response_200_meta import (
        GetWikiCategoriesResponse200Meta,
    )
    from ..models.get_wiki_categories_response_200_permissions import (
        GetWikiCategoriesResponse200Permissions,
    )
    from ..models.get_wiki_categories_response_200_wiki_category import (
        GetWikiCategoriesResponse200WikiCategory,
    )


T = TypeVar("T", bound="GetWikiCategoriesResponse200")


@_attrs_define
class GetWikiCategoriesResponse200:
    """
    Attributes:
        data (list[GetWikiCategoriesResponse200WikiCategory] | Unset):
        meta (GetWikiCategoriesResponse200Meta | Unset):
        permissions (GetWikiCategoriesResponse200Permissions | Unset):
    """

    data: list[GetWikiCategoriesResponse200WikiCategory] | Unset = UNSET
    meta: GetWikiCategoriesResponse200Meta | Unset = UNSET
    permissions: GetWikiCategoriesResponse200Permissions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wiki_categories_response_200_meta import (
            GetWikiCategoriesResponse200Meta,
        )
        from ..models.get_wiki_categories_response_200_permissions import (
            GetWikiCategoriesResponse200Permissions,
        )
        from ..models.get_wiki_categories_response_200_wiki_category import (
            GetWikiCategoriesResponse200WikiCategory,
        )

        d = dict(src_dict)
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = GetWikiCategoriesResponse200WikiCategory.from_dict(
                data_item_data
            )

            data.append(data_item)

        _meta = d.pop("meta", UNSET)
        meta: GetWikiCategoriesResponse200Meta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = GetWikiCategoriesResponse200Meta.from_dict(_meta)

        _permissions = d.pop("permissions", UNSET)
        permissions: GetWikiCategoriesResponse200Permissions | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = GetWikiCategoriesResponse200Permissions.from_dict(
                _permissions
            )

        get_wiki_categories_response_200 = cls(
            data=data,
            meta=meta,
            permissions=permissions,
        )

        get_wiki_categories_response_200.additional_properties = d
        return get_wiki_categories_response_200

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
