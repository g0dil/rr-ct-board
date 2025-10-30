import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_calendars_calendar_id_appointments_include_item import (
    GetCalendarsCalendarIdAppointmentsIncludeItem,
)
from ...models.get_calendars_calendar_id_appointments_response_200 import (
    GetCalendarsCalendarIdAppointmentsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    calendar_id: int,
    *,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    query: str | Unset = UNSET,
    include: list[GetCalendarsCalendarIdAppointmentsIncludeItem] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["query"] = query

    json_include: list[str] | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = []
        for include_item_data in include:
            include_item = include_item_data.value
            json_include.append(include_item)

    params["include[]"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/calendars/{calendar_id}/appointments".format(
            calendar_id=calendar_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetCalendarsCalendarIdAppointmentsResponse200 | str | None:
    if response.status_code == 200:
        response_200 = GetCalendarsCalendarIdAppointmentsResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 401:
        response_401 = response.text
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetCalendarsCalendarIdAppointmentsResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    calendar_id: int,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    query: str | Unset = UNSET,
    include: list[GetCalendarsCalendarIdAppointmentsIncludeItem] | Unset = UNSET,
) -> Response[Any | GetCalendarsCalendarIdAppointmentsResponse200 | str]:
    """Get all appointments of a calendar

    Args:
        calendar_id (int):  Example: 42.
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        query (str | Unset):
        include (list[GetCalendarsCalendarIdAppointmentsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCalendarsCalendarIdAppointmentsResponse200 | str]
    """

    kwargs = _get_kwargs(
        calendar_id=calendar_id,
        from_=from_,
        to=to,
        query=query,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    calendar_id: int,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    query: str | Unset = UNSET,
    include: list[GetCalendarsCalendarIdAppointmentsIncludeItem] | Unset = UNSET,
) -> Any | GetCalendarsCalendarIdAppointmentsResponse200 | str | None:
    """Get all appointments of a calendar

    Args:
        calendar_id (int):  Example: 42.
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        query (str | Unset):
        include (list[GetCalendarsCalendarIdAppointmentsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCalendarsCalendarIdAppointmentsResponse200 | str
    """

    return sync_detailed(
        calendar_id=calendar_id,
        client=client,
        from_=from_,
        to=to,
        query=query,
        include=include,
    ).parsed


async def asyncio_detailed(
    calendar_id: int,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    query: str | Unset = UNSET,
    include: list[GetCalendarsCalendarIdAppointmentsIncludeItem] | Unset = UNSET,
) -> Response[Any | GetCalendarsCalendarIdAppointmentsResponse200 | str]:
    """Get all appointments of a calendar

    Args:
        calendar_id (int):  Example: 42.
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        query (str | Unset):
        include (list[GetCalendarsCalendarIdAppointmentsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCalendarsCalendarIdAppointmentsResponse200 | str]
    """

    kwargs = _get_kwargs(
        calendar_id=calendar_id,
        from_=from_,
        to=to,
        query=query,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    calendar_id: int,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    query: str | Unset = UNSET,
    include: list[GetCalendarsCalendarIdAppointmentsIncludeItem] | Unset = UNSET,
) -> Any | GetCalendarsCalendarIdAppointmentsResponse200 | str | None:
    """Get all appointments of a calendar

    Args:
        calendar_id (int):  Example: 42.
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        query (str | Unset):
        include (list[GetCalendarsCalendarIdAppointmentsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCalendarsCalendarIdAppointmentsResponse200 | str
    """

    return (
        await asyncio_detailed(
            calendar_id=calendar_id,
            client=client,
            from_=from_,
            to=to,
            query=query,
            include=include,
        )
    ).parsed
