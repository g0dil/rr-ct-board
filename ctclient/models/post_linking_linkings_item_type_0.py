from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_linking_linkings_item_type_0_fetch_status import (
    PostLinkingLinkingsItemType0FetchStatus,
)
from ..models.post_linking_linkings_item_type_0_linking_type import (
    PostLinkingLinkingsItemType0LinkingType,
)

if TYPE_CHECKING:
    from ..models.post_linking_linkings_item_type_0_data_type_0 import (
        PostLinkingLinkingsItemType0DataType0,
    )


T = TypeVar("T", bound="PostLinkingLinkingsItemType0")


@_attrs_define
class PostLinkingLinkingsItemType0:
    """
    Attributes:
        fetch_status (PostLinkingLinkingsItemType0FetchStatus):
        url (str):
        data (None | PostLinkingLinkingsItemType0DataType0):
        linking_type (PostLinkingLinkingsItemType0LinkingType):
    """

    fetch_status: PostLinkingLinkingsItemType0FetchStatus
    url: str
    data: None | PostLinkingLinkingsItemType0DataType0
    linking_type: PostLinkingLinkingsItemType0LinkingType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_linking_linkings_item_type_0_data_type_0 import (
            PostLinkingLinkingsItemType0DataType0,
        )

        fetch_status = self.fetch_status.value

        url = self.url

        data: dict[str, Any] | None
        if isinstance(self.data, PostLinkingLinkingsItemType0DataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        linking_type = self.linking_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fetchStatus": fetch_status,
                "url": url,
                "data": data,
                "linkingType": linking_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_linking_linkings_item_type_0_data_type_0 import (
            PostLinkingLinkingsItemType0DataType0,
        )

        d = dict(src_dict)
        fetch_status = PostLinkingLinkingsItemType0FetchStatus(d.pop("fetchStatus"))

        url = d.pop("url")

        def _parse_data(data: object) -> None | PostLinkingLinkingsItemType0DataType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = PostLinkingLinkingsItemType0DataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(None | PostLinkingLinkingsItemType0DataType0, data)

        data = _parse_data(d.pop("data"))

        linking_type = PostLinkingLinkingsItemType0LinkingType(d.pop("linkingType"))

        post_linking_linkings_item_type_0 = cls(
            fetch_status=fetch_status,
            url=url,
            data=data,
            linking_type=linking_type,
        )

        post_linking_linkings_item_type_0.additional_properties = d
        return post_linking_linkings_item_type_0

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
