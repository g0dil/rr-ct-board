from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_linking_linkings_item_type_0 import PostLinkingLinkingsItemType0


T = TypeVar("T", bound="PostLinking")


@_attrs_define
class PostLinking:
    """
    Attributes:
        linkings (list[PostLinkingLinkingsItemType0]):
        post_id (int):
    """

    linkings: list[PostLinkingLinkingsItemType0]
    post_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_linking_linkings_item_type_0 import (
            PostLinkingLinkingsItemType0,
        )

        linkings = []
        for linkings_item_data in self.linkings:
            linkings_item: dict[str, Any]
            if isinstance(linkings_item_data, PostLinkingLinkingsItemType0):
                linkings_item = linkings_item_data.to_dict()

            linkings.append(linkings_item)

        post_id = self.post_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "linkings": linkings,
                "postId": post_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_linking_linkings_item_type_0 import (
            PostLinkingLinkingsItemType0,
        )

        d = dict(src_dict)
        linkings = []
        _linkings = d.pop("linkings")
        for linkings_item_data in _linkings:

            def _parse_linkings_item(data: object) -> PostLinkingLinkingsItemType0:
                if not isinstance(data, dict):
                    raise TypeError()
                linkings_item_type_0 = PostLinkingLinkingsItemType0.from_dict(data)

                return linkings_item_type_0

            linkings_item = _parse_linkings_item(linkings_item_data)

            linkings.append(linkings_item)

        post_id = d.pop("postId")

        post_linking = cls(
            linkings=linkings,
            post_id=post_id,
        )

        post_linking.additional_properties = d
        return post_linking

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
