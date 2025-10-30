from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.booking_conflict_request_body_additionals_type_0_item import (
        BookingConflictRequestBodyAdditionalsType0Item,
    )
    from ..models.booking_conflict_request_body_exceptions_type_0_item import (
        BookingConflictRequestBodyExceptionsType0Item,
    )


T = TypeVar("T", bound="BookingConflictRequestBody")


@_attrs_define
class BookingConflictRequestBody:
    """
    Attributes:
        end_date (datetime.date | datetime.datetime):
        resource_id (int):
        start_date (datetime.date | datetime.datetime):
        additionals (list[BookingConflictRequestBodyAdditionalsType0Item] | None | Unset):
        exceptions (list[BookingConflictRequestBodyExceptionsType0Item] | None | Unset):
        repeat_frequency (int | None | Unset):
        repeat_id (int | Unset):  Default: 0.
        repeat_option (int | None | Unset):
        repeat_until (datetime.date | None | Unset): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
    """

    end_date: datetime.date | datetime.datetime
    resource_id: int
    start_date: datetime.date | datetime.datetime
    additionals: list[BookingConflictRequestBodyAdditionalsType0Item] | None | Unset = (
        UNSET
    )
    exceptions: list[BookingConflictRequestBodyExceptionsType0Item] | None | Unset = (
        UNSET
    )
    repeat_frequency: int | None | Unset = UNSET
    repeat_id: int | Unset = 0
    repeat_option: int | None | Unset = UNSET
    repeat_until: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_date: str
        if isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date.isoformat()

        resource_id = self.resource_id

        start_date: str
        if isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date.isoformat()

        additionals: list[dict[str, Any]] | None | Unset
        if isinstance(self.additionals, Unset):
            additionals = UNSET
        elif isinstance(self.additionals, list):
            additionals = []
            for additionals_type_0_item_data in self.additionals:
                additionals_type_0_item = additionals_type_0_item_data.to_dict()
                additionals.append(additionals_type_0_item)

        else:
            additionals = self.additionals

        exceptions: list[dict[str, Any]] | None | Unset
        if isinstance(self.exceptions, Unset):
            exceptions = UNSET
        elif isinstance(self.exceptions, list):
            exceptions = []
            for exceptions_type_0_item_data in self.exceptions:
                exceptions_type_0_item = exceptions_type_0_item_data.to_dict()
                exceptions.append(exceptions_type_0_item)

        else:
            exceptions = self.exceptions

        repeat_frequency: int | None | Unset
        if isinstance(self.repeat_frequency, Unset):
            repeat_frequency = UNSET
        else:
            repeat_frequency = self.repeat_frequency

        repeat_id = self.repeat_id

        repeat_option: int | None | Unset
        if isinstance(self.repeat_option, Unset):
            repeat_option = UNSET
        else:
            repeat_option = self.repeat_option

        repeat_until: None | str | Unset
        if isinstance(self.repeat_until, Unset):
            repeat_until = UNSET
        elif isinstance(self.repeat_until, datetime.date):
            repeat_until = self.repeat_until.isoformat()
        else:
            repeat_until = self.repeat_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endDate": end_date,
                "resourceId": resource_id,
                "startDate": start_date,
            }
        )
        if additionals is not UNSET:
            field_dict["additionals"] = additionals
        if exceptions is not UNSET:
            field_dict["exceptions"] = exceptions
        if repeat_frequency is not UNSET:
            field_dict["repeatFrequency"] = repeat_frequency
        if repeat_id is not UNSET:
            field_dict["repeatId"] = repeat_id
        if repeat_option is not UNSET:
            field_dict["repeatOption"] = repeat_option
        if repeat_until is not UNSET:
            field_dict["repeatUntil"] = repeat_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_conflict_request_body_additionals_type_0_item import (
            BookingConflictRequestBodyAdditionalsType0Item,
        )
        from ..models.booking_conflict_request_body_exceptions_type_0_item import (
            BookingConflictRequestBodyExceptionsType0Item,
        )

        d = dict(src_dict)

        def _parse_end_date(data: object) -> datetime.date | datetime.datetime:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            end_date_type_1 = isoparse(data).date()

            return end_date_type_1

        end_date = _parse_end_date(d.pop("endDate"))

        resource_id = d.pop("resourceId")

        def _parse_start_date(data: object) -> datetime.date | datetime.datetime:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            start_date_type_1 = isoparse(data).date()

            return start_date_type_1

        start_date = _parse_start_date(d.pop("startDate"))

        def _parse_additionals(
            data: object,
        ) -> list[BookingConflictRequestBodyAdditionalsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                additionals_type_0 = []
                _additionals_type_0 = data
                for additionals_type_0_item_data in _additionals_type_0:
                    additionals_type_0_item = (
                        BookingConflictRequestBodyAdditionalsType0Item.from_dict(
                            additionals_type_0_item_data
                        )
                    )

                    additionals_type_0.append(additionals_type_0_item)

                return additionals_type_0
            except:  # noqa: E722
                pass
            return cast(
                list[BookingConflictRequestBodyAdditionalsType0Item] | None | Unset,
                data,
            )

        additionals = _parse_additionals(d.pop("additionals", UNSET))

        def _parse_exceptions(
            data: object,
        ) -> list[BookingConflictRequestBodyExceptionsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exceptions_type_0 = []
                _exceptions_type_0 = data
                for exceptions_type_0_item_data in _exceptions_type_0:
                    exceptions_type_0_item = (
                        BookingConflictRequestBodyExceptionsType0Item.from_dict(
                            exceptions_type_0_item_data
                        )
                    )

                    exceptions_type_0.append(exceptions_type_0_item)

                return exceptions_type_0
            except:  # noqa: E722
                pass
            return cast(
                list[BookingConflictRequestBodyExceptionsType0Item] | None | Unset, data
            )

        exceptions = _parse_exceptions(d.pop("exceptions", UNSET))

        def _parse_repeat_frequency(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        repeat_frequency = _parse_repeat_frequency(d.pop("repeatFrequency", UNSET))

        repeat_id = d.pop("repeatId", UNSET)

        def _parse_repeat_option(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        repeat_option = _parse_repeat_option(d.pop("repeatOption", UNSET))

        def _parse_repeat_until(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                repeat_until_type_0 = isoparse(data).date()

                return repeat_until_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.date | None | Unset, data)

        repeat_until = _parse_repeat_until(d.pop("repeatUntil", UNSET))

        booking_conflict_request_body = cls(
            end_date=end_date,
            resource_id=resource_id,
            start_date=start_date,
            additionals=additionals,
            exceptions=exceptions,
            repeat_frequency=repeat_frequency,
            repeat_id=repeat_id,
            repeat_option=repeat_option,
            repeat_until=repeat_until,
        )

        booking_conflict_request_body.additional_properties = d
        return booking_conflict_request_body

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
