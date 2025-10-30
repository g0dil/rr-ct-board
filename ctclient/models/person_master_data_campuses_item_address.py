from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PersonMasterDataCampusesItemAddress")


@_attrs_define
class PersonMasterDataCampusesItemAddress:
    """
    Attributes:
        geo_lat (None | str):
        geo_lng (None | str):
        latitude_loose (None | str):
        longitude_loose (None | str):
        marker_color (None | str):
        marker_icon (None | str):
        marker_url (None | str):
        meeting_at (None | str):
        postalcode (None | str):
    """

    geo_lat: None | str
    geo_lng: None | str
    latitude_loose: None | str
    longitude_loose: None | str
    marker_color: None | str
    marker_icon: None | str
    marker_url: None | str
    meeting_at: None | str
    postalcode: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        geo_lat: None | str
        geo_lat = self.geo_lat

        geo_lng: None | str
        geo_lng = self.geo_lng

        latitude_loose: None | str
        latitude_loose = self.latitude_loose

        longitude_loose: None | str
        longitude_loose = self.longitude_loose

        marker_color: None | str
        marker_color = self.marker_color

        marker_icon: None | str
        marker_icon = self.marker_icon

        marker_url: None | str
        marker_url = self.marker_url

        meeting_at: None | str
        meeting_at = self.meeting_at

        postalcode: None | str
        postalcode = self.postalcode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "geoLat": geo_lat,
                "geoLng": geo_lng,
                "latitudeLoose": latitude_loose,
                "longitudeLoose": longitude_loose,
                "markerColor": marker_color,
                "markerIcon": marker_icon,
                "markerUrl": marker_url,
                "meetingAt": meeting_at,
                "postalcode": postalcode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_geo_lat(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        geo_lat = _parse_geo_lat(d.pop("geoLat"))

        def _parse_geo_lng(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        geo_lng = _parse_geo_lng(d.pop("geoLng"))

        def _parse_latitude_loose(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        latitude_loose = _parse_latitude_loose(d.pop("latitudeLoose"))

        def _parse_longitude_loose(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        longitude_loose = _parse_longitude_loose(d.pop("longitudeLoose"))

        def _parse_marker_color(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        marker_color = _parse_marker_color(d.pop("markerColor"))

        def _parse_marker_icon(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        marker_icon = _parse_marker_icon(d.pop("markerIcon"))

        def _parse_marker_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        marker_url = _parse_marker_url(d.pop("markerUrl"))

        def _parse_meeting_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        meeting_at = _parse_meeting_at(d.pop("meetingAt"))

        def _parse_postalcode(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        postalcode = _parse_postalcode(d.pop("postalcode"))

        person_master_data_campuses_item_address = cls(
            geo_lat=geo_lat,
            geo_lng=geo_lng,
            latitude_loose=latitude_loose,
            longitude_loose=longitude_loose,
            marker_color=marker_color,
            marker_icon=marker_icon,
            marker_url=marker_url,
            meeting_at=meeting_at,
            postalcode=postalcode,
        )

        person_master_data_campuses_item_address.additional_properties = d
        return person_master_data_campuses_item_address

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
