from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_widget_rss_response_200_data_items_item import (
        GetWidgetRssResponse200DataItemsItem,
    )


T = TypeVar("T", bound="GetWidgetRssResponse200Data")


@_attrs_define
class GetWidgetRssResponse200Data:
    """
    Attributes:
        items (list[GetWidgetRssResponse200DataItemsItem]):
        title (str):
        description (str | Unset):
        link (str | Unset):
        total_count (int | Unset):
    """

    items: list[GetWidgetRssResponse200DataItemsItem]
    title: str
    description: str | Unset = UNSET
    link: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        title = self.title

        description = self.description

        link = self.link

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if link is not UNSET:
            field_dict["link"] = link
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_widget_rss_response_200_data_items_item import (
            GetWidgetRssResponse200DataItemsItem,
        )

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = GetWidgetRssResponse200DataItemsItem.from_dict(items_item_data)

            items.append(items_item)

        title = d.pop("title")

        description = d.pop("description", UNSET)

        link = d.pop("link", UNSET)

        total_count = d.pop("totalCount", UNSET)

        get_widget_rss_response_200_data = cls(
            items=items,
            title=title,
            description=description,
            link=link,
            total_count=total_count,
        )

        get_widget_rss_response_200_data.additional_properties = d
        return get_widget_rss_response_200_data

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
