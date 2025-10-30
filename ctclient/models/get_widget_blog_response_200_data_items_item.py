from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWidgetBlogResponse200DataItemsItem")


@_attrs_define
class GetWidgetBlogResponse200DataItemsItem:
    """
    Attributes:
        author (str | Unset):
        content (str | Unset):
        date (str | Unset):
        description (str | Unset):
        image (str | Unset):
        link (str | Unset):
        title (str | Unset):
    """

    author: str | Unset = UNSET
    content: str | Unset = UNSET
    date: str | Unset = UNSET
    description: str | Unset = UNSET
    image: str | Unset = UNSET
    link: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author = self.author

        content = self.content

        date = self.date

        description = self.description

        image = self.image

        link = self.link

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if content is not UNSET:
            field_dict["content"] = content
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if image is not UNSET:
            field_dict["image"] = image
        if link is not UNSET:
            field_dict["link"] = link
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author = d.pop("author", UNSET)

        content = d.pop("content", UNSET)

        date = d.pop("date", UNSET)

        description = d.pop("description", UNSET)

        image = d.pop("image", UNSET)

        link = d.pop("link", UNSET)

        title = d.pop("title", UNSET)

        get_widget_blog_response_200_data_items_item = cls(
            author=author,
            content=content,
            date=date,
            description=description,
            image=image,
            link=link,
            title=title,
        )

        get_widget_blog_response_200_data_items_item.additional_properties = d
        return get_widget_blog_response_200_data_items_item

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
