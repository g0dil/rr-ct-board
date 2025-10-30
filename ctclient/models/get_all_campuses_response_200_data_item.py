from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_all_campuses_response_200_data_item_address import (
        GetAllCampusesResponse200DataItemAddress,
    )
    from ..models.get_all_campuses_response_200_data_item_meta import (
        GetAllCampusesResponse200DataItemMeta,
    )


T = TypeVar("T", bound="GetAllCampusesResponse200DataItem")


@_attrs_define
class GetAllCampusesResponse200DataItem:
    """Campus with possible address.

    Attributes:
        guid (str):
        id (int):
        meta (GetAllCampusesResponse200DataItemMeta):  Example: {'createdDate': '2020-01-01T00:00:00Z', 'createdPerson':
            {'id': 1}, 'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
        name (str):
        name_translated (str):
        short_name (str):
        shorty (str):
        sort_key (int):
        address (GetAllCampusesResponse200DataItemAddress | Unset):
    """

    guid: str
    id: int
    meta: GetAllCampusesResponse200DataItemMeta
    name: str
    name_translated: str
    short_name: str
    shorty: str
    sort_key: int
    address: GetAllCampusesResponse200DataItemAddress | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        guid = self.guid

        id = self.id

        meta = self.meta.to_dict()

        name = self.name

        name_translated = self.name_translated

        short_name = self.short_name

        shorty = self.shorty

        sort_key = self.sort_key

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "guid": guid,
                "id": id,
                "meta": meta,
                "name": name,
                "nameTranslated": name_translated,
                "shortName": short_name,
                "shorty": shorty,
                "sortKey": sort_key,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_all_campuses_response_200_data_item_address import (
            GetAllCampusesResponse200DataItemAddress,
        )
        from ..models.get_all_campuses_response_200_data_item_meta import (
            GetAllCampusesResponse200DataItemMeta,
        )

        d = dict(src_dict)
        guid = d.pop("guid")

        id = d.pop("id")

        meta = GetAllCampusesResponse200DataItemMeta.from_dict(d.pop("meta"))

        name = d.pop("name")

        name_translated = d.pop("nameTranslated")

        short_name = d.pop("shortName")

        shorty = d.pop("shorty")

        sort_key = d.pop("sortKey")

        _address = d.pop("address", UNSET)
        address: GetAllCampusesResponse200DataItemAddress | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = GetAllCampusesResponse200DataItemAddress.from_dict(_address)

        get_all_campuses_response_200_data_item = cls(
            guid=guid,
            id=id,
            meta=meta,
            name=name,
            name_translated=name_translated,
            short_name=short_name,
            shorty=shorty,
            sort_key=sort_key,
            address=address,
        )

        get_all_campuses_response_200_data_item.additional_properties = d
        return get_all_campuses_response_200_data_item

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
