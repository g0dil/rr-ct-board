from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base_repeat_id import (
    GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseRepeatId,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base_additionals_item import (
        GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseAdditionalsItem,
    )
    from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base_additions_item import (
        GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseAdditionsItem,
    )
    from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base_address import (
        GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseAddress,
    )
    from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base_calendar import (
        GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseCalendar,
    )
    from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base_exceptions_item import (
        GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseExceptionsItem,
    )
    from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base_image_type_0 import (
        GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseImageType0,
    )
    from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base_meta import (
        GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseMeta,
    )
    from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base_signup_type_0 import (
        GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseSignupType0,
    )


T = TypeVar(
    "T", bound="GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBase"
)


@_attrs_define
class GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBase:
    """
    Attributes:
        additionals (list[GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseAdditionalsItem]):
        address (GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseAddress):
        all_day (bool):
        calendar (GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseCalendar):
        description (None | str):
        end_date (datetime.date | datetime.datetime):
        exceptions (list[GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseExceptionsItem]):
        id (int):
        image (GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseImageType0 | None):
        is_internal (bool):
        link (None | str):
        meta (GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseMeta):  Example: {'createdDate':
            '2020-01-01T00:00:00Z', 'createdPerson': {'id': 1}, 'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson':
            {'id': 1}}.
        on_behalf_of_pid (int | None):
        repeat_frequency (int | None):
        repeat_id (GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseRepeatId): ID of the repeat
            pattern, NONE = 0, DAILY = 1, WEEKLY = 7, MONTHLY_BY_DATE = 31, MONTHLY_BY_WEEKDAY = 32, YEARLY = 365, MANUALLY
            = 999
        repeat_option (int | None):
        repeat_until (datetime.date | None): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
        signup (GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseSignupType0 | None):
        start_date (datetime.date | datetime.datetime):
        subtitle (None | str):
        title (str):
        version (int):
        additions (list[GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseAdditionsItem] | Unset):
            Use 'additionals' instead
        caption (str | Unset): Use 'title' instead
        information (None | str | Unset): Use 'description' instead
        note (None | str | Unset): Use 'subtitle' instead
    """

    additionals: list[
        GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseAdditionalsItem
    ]
    address: (
        GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseAddress
    )
    all_day: bool
    calendar: (
        GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseCalendar
    )
    description: None | str
    end_date: datetime.date | datetime.datetime
    exceptions: list[
        GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseExceptionsItem
    ]
    id: int
    image: (
        GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseImageType0
        | None
    )
    is_internal: bool
    link: None | str
    meta: GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseMeta
    on_behalf_of_pid: int | None
    repeat_frequency: int | None
    repeat_id: (
        GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseRepeatId
    )
    repeat_option: int | None
    repeat_until: datetime.date | None
    signup: (
        GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseSignupType0
        | None
    )
    start_date: datetime.date | datetime.datetime
    subtitle: None | str
    title: str
    version: int
    additions: (
        list[
            GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseAdditionsItem
        ]
        | Unset
    ) = UNSET
    caption: str | Unset = UNSET
    information: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base_image_type_0 import (
            GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseImageType0,
        )
        from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base_signup_type_0 import (
            GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseSignupType0,
        )

        additionals = []
        for additionals_item_data in self.additionals:
            additionals_item = additionals_item_data.to_dict()
            additionals.append(additionals_item)

        address = self.address.to_dict()

        all_day = self.all_day

        calendar = self.calendar.to_dict()

        description: None | str
        description = self.description

        end_date: str
        if isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date.isoformat()

        exceptions = []
        for exceptions_item_data in self.exceptions:
            exceptions_item = exceptions_item_data.to_dict()
            exceptions.append(exceptions_item)

        id = self.id

        image: dict[str, Any] | None
        if isinstance(
            self.image,
            GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseImageType0,
        ):
            image = self.image.to_dict()
        else:
            image = self.image

        is_internal = self.is_internal

        link: None | str
        link = self.link

        meta = self.meta.to_dict()

        on_behalf_of_pid: int | None
        on_behalf_of_pid = self.on_behalf_of_pid

        repeat_frequency: int | None
        repeat_frequency = self.repeat_frequency

        repeat_id = self.repeat_id.value

        repeat_option: int | None
        repeat_option = self.repeat_option

        repeat_until: None | str
        if isinstance(self.repeat_until, datetime.date):
            repeat_until = self.repeat_until.isoformat()
        else:
            repeat_until = self.repeat_until

        signup: dict[str, Any] | None
        if isinstance(
            self.signup,
            GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseSignupType0,
        ):
            signup = self.signup.to_dict()
        else:
            signup = self.signup

        start_date: str
        if isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date.isoformat()

        subtitle: None | str
        subtitle = self.subtitle

        title = self.title

        version = self.version

        additions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.additions, Unset):
            additions = []
            for additions_item_data in self.additions:
                additions_item = additions_item_data.to_dict()
                additions.append(additions_item)

        caption = self.caption

        information: None | str | Unset
        if isinstance(self.information, Unset):
            information = UNSET
        else:
            information = self.information

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "additionals": additionals,
                "address": address,
                "allDay": all_day,
                "calendar": calendar,
                "description": description,
                "endDate": end_date,
                "exceptions": exceptions,
                "id": id,
                "image": image,
                "isInternal": is_internal,
                "link": link,
                "meta": meta,
                "onBehalfOfPid": on_behalf_of_pid,
                "repeatFrequency": repeat_frequency,
                "repeatId": repeat_id,
                "repeatOption": repeat_option,
                "repeatUntil": repeat_until,
                "signup": signup,
                "startDate": start_date,
                "subtitle": subtitle,
                "title": title,
                "version": version,
            }
        )
        if additions is not UNSET:
            field_dict["additions"] = additions
        if caption is not UNSET:
            field_dict["caption"] = caption
        if information is not UNSET:
            field_dict["information"] = information
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base_additionals_item import (
            GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseAdditionalsItem,
        )
        from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base_additions_item import (
            GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseAdditionsItem,
        )
        from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base_address import (
            GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseAddress,
        )
        from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base_calendar import (
            GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseCalendar,
        )
        from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base_exceptions_item import (
            GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseExceptionsItem,
        )
        from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base_image_type_0 import (
            GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseImageType0,
        )
        from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base_meta import (
            GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseMeta,
        )
        from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base_signup_type_0 import (
            GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseSignupType0,
        )

        d = dict(src_dict)
        additionals = []
        _additionals = d.pop("additionals")
        for additionals_item_data in _additionals:
            additionals_item = GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseAdditionalsItem.from_dict(
                additionals_item_data
            )

            additionals.append(additionals_item)

        address = GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseAddress.from_dict(
            d.pop("address")
        )

        all_day = d.pop("allDay")

        calendar = GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseCalendar.from_dict(
            d.pop("calendar")
        )

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

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

        exceptions = []
        _exceptions = d.pop("exceptions")
        for exceptions_item_data in _exceptions:
            exceptions_item = GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseExceptionsItem.from_dict(
                exceptions_item_data
            )

            exceptions.append(exceptions_item)

        id = d.pop("id")

        def _parse_image(
            data: object,
        ) -> (
            GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseImageType0
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_type_0 = GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseImageType0.from_dict(
                    data
                )

                return image_type_0
            except:  # noqa: E722
                pass
            return cast(
                GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseImageType0
                | None,
                data,
            )

        image = _parse_image(d.pop("image"))

        is_internal = d.pop("isInternal")

        def _parse_link(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        link = _parse_link(d.pop("link"))

        meta = GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseMeta.from_dict(
            d.pop("meta")
        )

        def _parse_on_behalf_of_pid(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        on_behalf_of_pid = _parse_on_behalf_of_pid(d.pop("onBehalfOfPid"))

        def _parse_repeat_frequency(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        repeat_frequency = _parse_repeat_frequency(d.pop("repeatFrequency"))

        repeat_id = GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseRepeatId(
            d.pop("repeatId")
        )

        def _parse_repeat_option(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        repeat_option = _parse_repeat_option(d.pop("repeatOption"))

        def _parse_repeat_until(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                repeat_until_type_0 = isoparse(data).date()

                return repeat_until_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.date | None, data)

        repeat_until = _parse_repeat_until(d.pop("repeatUntil"))

        def _parse_signup(
            data: object,
        ) -> (
            GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseSignupType0
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                signup_type_0 = GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseSignupType0.from_dict(
                    data
                )

                return signup_type_0
            except:  # noqa: E722
                pass
            return cast(
                GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseSignupType0
                | None,
                data,
            )

        signup = _parse_signup(d.pop("signup"))

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

        def _parse_subtitle(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subtitle = _parse_subtitle(d.pop("subtitle"))

        title = d.pop("title")

        version = d.pop("version")

        additions = []
        _additions = d.pop("additions", UNSET)
        for additions_item_data in _additions or []:
            additions_item = GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBaseAdditionsItem.from_dict(
                additions_item_data
            )

            additions.append(additions_item)

        caption = d.pop("caption", UNSET)

        def _parse_information(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        information = _parse_information(d.pop("information", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base = cls(
            additionals=additionals,
            address=address,
            all_day=all_day,
            calendar=calendar,
            description=description,
            end_date=end_date,
            exceptions=exceptions,
            id=id,
            image=image,
            is_internal=is_internal,
            link=link,
            meta=meta,
            on_behalf_of_pid=on_behalf_of_pid,
            repeat_frequency=repeat_frequency,
            repeat_id=repeat_id,
            repeat_option=repeat_option,
            repeat_until=repeat_until,
            signup=signup,
            start_date=start_date,
            subtitle=subtitle,
            title=title,
            version=version,
            additions=additions,
            caption=caption,
            information=information,
            note=note,
        )

        get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base.additional_properties = d
        return get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base

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
