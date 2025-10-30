from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="PostFollowupsFollowUpIdPostponeBody")


@_attrs_define
class PostFollowupsFollowUpIdPostponeBody:
    """
    Attributes:
        due_date (datetime.date): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
    """

    due_date: datetime.date
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        due_date = self.due_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dueDate": due_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        due_date = isoparse(d.pop("dueDate")).date()

        post_followups_follow_up_id_postpone_body = cls(
            due_date=due_date,
        )

        post_followups_follow_up_id_postpone_body.additional_properties = d
        return post_followups_follow_up_id_postpone_body

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
