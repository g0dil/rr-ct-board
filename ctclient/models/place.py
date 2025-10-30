from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.place_marker_color_type_0 import PlaceMarkerColorType0
from ..models.place_marker_color_type_1 import PlaceMarkerColorType1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.place_meta import PlaceMeta


T = TypeVar("T", bound="Place")


@_attrs_define
class Place:
    """Place wehre e.g. a group meeting takes place

    Attributes:
        id (int):
        meta (PlaceMeta):  Example: {'createdDate': '2020-01-01T00:00:00Z', 'createdPerson': {'id': 1}, 'modifiedDate':
            '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
        city (None | str | Unset): City
        district (None | str | Unset): Disctrict
        geo_lat (None | str | Unset): Latitude
        geo_lng (None | str | Unset): Longitude
        marker_color (PlaceMarkerColorType0 | PlaceMarkerColorType1 | Unset):
        marker_icon (str | Unset):
        marker_url (None | str | Unset): url for the marker icon
        name (None | str | Unset): Name of the place or the person living there
        postalcode (None | str | Unset): Zip code of the place
        street (None | str | Unset): Street
    """

    id: int
    meta: PlaceMeta
    city: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    geo_lat: None | str | Unset = UNSET
    geo_lng: None | str | Unset = UNSET
    marker_color: PlaceMarkerColorType0 | PlaceMarkerColorType1 | Unset = UNSET
    marker_icon: str | Unset = UNSET
    marker_url: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    postalcode: None | str | Unset = UNSET
    street: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        meta = self.meta.to_dict()

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        geo_lat: None | str | Unset
        if isinstance(self.geo_lat, Unset):
            geo_lat = UNSET
        else:
            geo_lat = self.geo_lat

        geo_lng: None | str | Unset
        if isinstance(self.geo_lng, Unset):
            geo_lng = UNSET
        else:
            geo_lng = self.geo_lng

        marker_color: str | Unset
        if isinstance(self.marker_color, Unset):
            marker_color = UNSET
        elif isinstance(self.marker_color, PlaceMarkerColorType0):
            marker_color = self.marker_color.value
        else:
            marker_color = self.marker_color.value

        marker_icon = self.marker_icon

        marker_url: None | str | Unset
        if isinstance(self.marker_url, Unset):
            marker_url = UNSET
        else:
            marker_url = self.marker_url

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        postalcode: None | str | Unset
        if isinstance(self.postalcode, Unset):
            postalcode = UNSET
        else:
            postalcode = self.postalcode

        street: None | str | Unset
        if isinstance(self.street, Unset):
            street = UNSET
        else:
            street = self.street

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "meta": meta,
            }
        )
        if city is not UNSET:
            field_dict["city"] = city
        if district is not UNSET:
            field_dict["district"] = district
        if geo_lat is not UNSET:
            field_dict["geoLat"] = geo_lat
        if geo_lng is not UNSET:
            field_dict["geoLng"] = geo_lng
        if marker_color is not UNSET:
            field_dict["markerColor"] = marker_color
        if marker_icon is not UNSET:
            field_dict["markerIcon"] = marker_icon
        if marker_url is not UNSET:
            field_dict["markerUrl"] = marker_url
        if name is not UNSET:
            field_dict["name"] = name
        if postalcode is not UNSET:
            field_dict["postalcode"] = postalcode
        if street is not UNSET:
            field_dict["street"] = street

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.place_meta import PlaceMeta

        d = dict(src_dict)
        id = d.pop("id")

        meta = PlaceMeta.from_dict(d.pop("meta"))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("district", UNSET))

        def _parse_geo_lat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geo_lat = _parse_geo_lat(d.pop("geoLat", UNSET))

        def _parse_geo_lng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geo_lng = _parse_geo_lng(d.pop("geoLng", UNSET))

        def _parse_marker_color(
            data: object,
        ) -> PlaceMarkerColorType0 | PlaceMarkerColorType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                marker_color_type_0 = PlaceMarkerColorType0(data)

                return marker_color_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            marker_color_type_1 = PlaceMarkerColorType1(data)

            return marker_color_type_1

        marker_color = _parse_marker_color(d.pop("markerColor", UNSET))

        marker_icon = d.pop("markerIcon", UNSET)

        def _parse_marker_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        marker_url = _parse_marker_url(d.pop("markerUrl", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_postalcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postalcode = _parse_postalcode(d.pop("postalcode", UNSET))

        def _parse_street(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street = _parse_street(d.pop("street", UNSET))

        place = cls(
            id=id,
            meta=meta,
            city=city,
            district=district,
            geo_lat=geo_lat,
            geo_lng=geo_lng,
            marker_color=marker_color,
            marker_icon=marker_icon,
            marker_url=marker_url,
            name=name,
            postalcode=postalcode,
            street=street,
        )

        place.additional_properties = d
        return place

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
