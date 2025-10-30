from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.arrangement_create_key_type_0 import ArrangementCreateKeyType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="ArrangementCreate")


@_attrs_define
class ArrangementCreate:
    """Details about a song's arrangement.

    Attributes:
        name (str):  Example: Men Voicing.
        beat (None | str | Unset):  Example: 4/4.
        description (None | str | Unset):  Example: Great arrangement for male voices.
        duration (int | None | Unset): Duration in seconds Example: 170.
        key (ArrangementCreateKeyType0 | None | Unset):
        source_id (int | None | Unset):  Example: 77.
        source_reference (None | str | Unset):  Example: 55a.
        tempo (int | None | Unset):  Example: 120.
    """

    name: str
    beat: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    duration: int | None | Unset = UNSET
    key: ArrangementCreateKeyType0 | None | Unset = UNSET
    source_id: int | None | Unset = UNSET
    source_reference: None | str | Unset = UNSET
    tempo: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        beat: None | str | Unset
        if isinstance(self.beat, Unset):
            beat = UNSET
        else:
            beat = self.beat

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        duration: int | None | Unset
        if isinstance(self.duration, Unset):
            duration = UNSET
        else:
            duration = self.duration

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        elif isinstance(self.key, ArrangementCreateKeyType0):
            key = self.key.value
        else:
            key = self.key

        source_id: int | None | Unset
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        else:
            source_id = self.source_id

        source_reference: None | str | Unset
        if isinstance(self.source_reference, Unset):
            source_reference = UNSET
        else:
            source_reference = self.source_reference

        tempo: int | None | Unset
        if isinstance(self.tempo, Unset):
            tempo = UNSET
        else:
            tempo = self.tempo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if beat is not UNSET:
            field_dict["beat"] = beat
        if description is not UNSET:
            field_dict["description"] = description
        if duration is not UNSET:
            field_dict["duration"] = duration
        if key is not UNSET:
            field_dict["key"] = key
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if source_reference is not UNSET:
            field_dict["sourceReference"] = source_reference
        if tempo is not UNSET:
            field_dict["tempo"] = tempo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_beat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beat = _parse_beat(d.pop("beat", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_duration(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration = _parse_duration(d.pop("duration", UNSET))

        def _parse_key(data: object) -> ArrangementCreateKeyType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                key_type_0 = ArrangementCreateKeyType0(data)

                return key_type_0
            except:  # noqa: E722
                pass
            return cast(ArrangementCreateKeyType0 | None | Unset, data)

        key = _parse_key(d.pop("key", UNSET))

        def _parse_source_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        source_id = _parse_source_id(d.pop("sourceId", UNSET))

        def _parse_source_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_reference = _parse_source_reference(d.pop("sourceReference", UNSET))

        def _parse_tempo(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tempo = _parse_tempo(d.pop("tempo", UNSET))

        arrangement_create = cls(
            name=name,
            beat=beat,
            description=description,
            duration=duration,
            key=key,
            source_id=source_id,
            source_reference=source_reference,
            tempo=tempo,
        )

        arrangement_create.additional_properties = d
        return arrangement_create

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
