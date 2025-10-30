from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_widget_blog_response_200_data_items_item import (
        GetWidgetBlogResponse200DataItemsItem,
    )


T = TypeVar("T", bound="GetWidgetBlogResponse200Data")


@_attrs_define
class GetWidgetBlogResponse200Data:
    """
    Attributes:
        description (str | Unset):
        items (list[GetWidgetBlogResponse200DataItemsItem] | Unset):
        link (str | Unset):
        title (str | Unset):
        total_count (int | Unset):
    """

    description: str | Unset = UNSET
    items: list[GetWidgetBlogResponse200DataItemsItem] | Unset = UNSET
    link: str | Unset = UNSET
    title: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        link = self.link

        title = self.title

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if items is not UNSET:
            field_dict["items"] = items
        if link is not UNSET:
            field_dict["link"] = link
        if title is not UNSET:
            field_dict["title"] = title
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_widget_blog_response_200_data_items_item import (
            GetWidgetBlogResponse200DataItemsItem,
        )

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = GetWidgetBlogResponse200DataItemsItem.from_dict(
                items_item_data
            )

            items.append(items_item)

        link = d.pop("link", UNSET)

        title = d.pop("title", UNSET)

        total_count = d.pop("totalCount", UNSET)

        get_widget_blog_response_200_data = cls(
            description=description,
            items=items,
            link=link,
            title=title,
            total_count=total_count,
        )

        get_widget_blog_response_200_data.additional_properties = d
        return get_widget_blog_response_200_data

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
