from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutFurtherlinksFurtherLinkIdResponse200Data")


@_attrs_define
class PutFurtherlinksFurtherLinkIdResponse200Data:
    """
    Attributes:
        description (None | str):  Example: Our church's NextCloud.
        image_url (None | str):
        name (str):  Example: NextCloud.
        sort_key (float):
        url (str):
        id (int):  Example: 3.
    """

    description: None | str
    image_url: None | str
    name: str
    sort_key: float
    url: str
    id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description: None | str
        description = self.description

        image_url: None | str
        image_url = self.image_url

        name = self.name

        sort_key = self.sort_key

        url = self.url

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "imageUrl": image_url,
                "name": name,
                "sortKey": sort_key,
                "url": url,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url = _parse_image_url(d.pop("imageUrl"))

        name = d.pop("name")

        sort_key = d.pop("sortKey")

        url = d.pop("url")

        id = d.pop("id")

        put_furtherlinks_further_link_id_response_200_data = cls(
            description=description,
            image_url=image_url,
            name=name,
            sort_key=sort_key,
            url=url,
            id=id,
        )

        put_furtherlinks_further_link_id_response_200_data.additional_properties = d
        return put_furtherlinks_further_link_id_response_200_data

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
