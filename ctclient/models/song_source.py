from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.song_source_meta import SongSourceMeta


T = TypeVar("T", bound="SongSource")


@_attrs_define
class SongSource:
    """Source of a song resp. arrangement

    Attributes:
        id (int):
        meta (SongSourceMeta):  Example: {'createdDate': '2020-01-01T00:00:00Z', 'createdPerson': {'id': 1},
            'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
        name (str):
        shorty (str):
        sort_key (int):
    """

    id: int
    meta: SongSourceMeta
    name: str
    shorty: str
    sort_key: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        meta = self.meta.to_dict()

        name = self.name

        shorty = self.shorty

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "meta": meta,
                "name": name,
                "shorty": shorty,
                "sortKey": sort_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.song_source_meta import SongSourceMeta

        d = dict(src_dict)
        id = d.pop("id")

        meta = SongSourceMeta.from_dict(d.pop("meta"))

        name = d.pop("name")

        shorty = d.pop("shorty")

        sort_key = d.pop("sortKey")

        song_source = cls(
            id=id,
            meta=meta,
            name=name,
            shorty=shorty,
            sort_key=sort_key,
        )

        song_source.additional_properties = d
        return song_source

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
