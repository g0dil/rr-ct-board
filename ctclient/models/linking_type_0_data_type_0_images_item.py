from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkingType0DataType0ImagesItem")


@_attrs_define
class LinkingType0DataType0ImagesItem:
    """
    Example:
        {'height': 1080, 'secureUrl': 'https://secure.example.com/image.jpg', 'type': 'image/jpeg', 'url':
            'https://example.com/image.jpg', 'width': 1920}

    Attributes:
        height (int | Unset): The height of the image in pixels.
        secure_url (str | Unset): The secure URL of the image.
        type_ (str | Unset): The MIME type of the image.
        url (str | Unset): The URL of the image.
        width (int | Unset): The width of the image in pixels.
    """

    height: int | Unset = UNSET
    secure_url: str | Unset = UNSET
    type_: str | Unset = UNSET
    url: str | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        height = self.height

        secure_url = self.secure_url

        type_ = self.type_

        url = self.url

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if height is not UNSET:
            field_dict["height"] = height
        if secure_url is not UNSET:
            field_dict["secureUrl"] = secure_url
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        height = d.pop("height", UNSET)

        secure_url = d.pop("secureUrl", UNSET)

        type_ = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        width = d.pop("width", UNSET)

        linking_type_0_data_type_0_images_item = cls(
            height=height,
            secure_url=secure_url,
            type_=type_,
            url=url,
            width=width,
        )

        linking_type_0_data_type_0_images_item.additional_properties = d
        return linking_type_0_data_type_0_images_item

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
