from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonUpdateablePrivacyPolicyAgreement")


@_attrs_define
class PersonUpdateablePrivacyPolicyAgreement:
    """This object can be optional or required. Depending on your ChurchTools data security settings.

    Attributes:
        date (datetime.date | None | Unset):
        type_id (int | None | Unset):
        who_id (int | None | Unset):
    """

    date: datetime.date | None | Unset = UNSET
    type_id: int | None | Unset = UNSET
    who_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.date):
            date = self.date.isoformat()
        else:
            date = self.date

        type_id: int | None | Unset
        if isinstance(self.type_id, Unset):
            type_id = UNSET
        else:
            type_id = self.type_id

        who_id: int | None | Unset
        if isinstance(self.who_id, Unset):
            who_id = UNSET
        else:
            who_id = self.who_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if type_id is not UNSET:
            field_dict["typeId"] = type_id
        if who_id is not UNSET:
            field_dict["whoId"] = who_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data).date()

                return date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.date | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        type_id = _parse_type_id(d.pop("typeId", UNSET))

        def _parse_who_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        who_id = _parse_who_id(d.pop("whoId", UNSET))

        person_updateable_privacy_policy_agreement = cls(
            date=date,
            type_id=type_id,
            who_id=who_id,
        )

        person_updateable_privacy_policy_agreement.additional_properties = d
        return person_updateable_privacy_policy_agreement

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
