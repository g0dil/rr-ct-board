from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostEventIcalResponse200Meta")


@_attrs_define
class PostEventIcalResponse200Meta:
    """
    Attributes:
        i_cal_url (str | Unset):  Example: http://churchtools.test/events/ical/QOkVUp7JVLf5Mg3s9ynS.
    """

    i_cal_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        i_cal_url = self.i_cal_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if i_cal_url is not UNSET:
            field_dict["iCalUrl"] = i_cal_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        i_cal_url = d.pop("iCalUrl", UNSET)

        post_event_ical_response_200_meta = cls(
            i_cal_url=i_cal_url,
        )

        post_event_ical_response_200_meta.additional_properties = d
        return post_event_ical_response_200_meta

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
