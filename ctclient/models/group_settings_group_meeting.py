from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GroupSettingsGroupMeeting")


@_attrs_define
class GroupSettingsGroupMeeting:
    """
    Attributes:
        auto_create (bool): Automatically create group meetings.
        template_id (int | None): Template for group meetings.
    """

    auto_create: bool
    template_id: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_create = self.auto_create

        template_id: int | None
        template_id = self.template_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoCreate": auto_create,
                "templateId": template_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_create = d.pop("autoCreate")

        def _parse_template_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        template_id = _parse_template_id(d.pop("templateId"))

        group_settings_group_meeting = cls(
            auto_create=auto_create,
            template_id=template_id,
        )

        group_settings_group_meeting.additional_properties = d
        return group_settings_group_meeting

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
