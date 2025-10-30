import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_calendars_appointments_include_item import (
    GetCalendarsAppointmentsIncludeItem,
)
from ...models.get_calendars_appointments_response_200 import (
    GetCalendarsAppointmentsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    calendar_ids: list[int],
    include: list[GetCalendarsAppointmentsIncludeItem] | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    query: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_calendar_ids = calendar_ids

    params["calendar_ids[]"] = json_calendar_ids

    json_include: list[str] | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = []
        for include_item_data in include:
            include_item = include_item_data.value
            json_include.append(include_item)

    params["include[]"] = json_include

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["query"] = query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/calendars/appointments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetCalendarsAppointmentsResponse200 | str | None:
    if response.status_code == 200:
        response_200 = GetCalendarsAppointmentsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = response.text
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetCalendarsAppointmentsResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    calendar_ids: list[int],
    include: list[GetCalendarsAppointmentsIncludeItem] | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    query: str | Unset = UNSET,
) -> Response[Any | GetCalendarsAppointmentsResponse200 | str]:
    """Get all appointments

    Args:
        calendar_ids (list[int]):
        include (list[GetCalendarsAppointmentsIncludeItem] | Unset):
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCalendarsAppointmentsResponse200 | str]
    """

    kwargs = _get_kwargs(
        calendar_ids=calendar_ids,
        include=include,
        from_=from_,
        to=to,
        query=query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    calendar_ids: list[int],
    include: list[GetCalendarsAppointmentsIncludeItem] | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    query: str | Unset = UNSET,
) -> Any | GetCalendarsAppointmentsResponse200 | str | None:
    """Get all appointments

    Args:
        calendar_ids (list[int]):
        include (list[GetCalendarsAppointmentsIncludeItem] | Unset):
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCalendarsAppointmentsResponse200 | str
    """

    return sync_detailed(
        client=client,
        calendar_ids=calendar_ids,
        include=include,
        from_=from_,
        to=to,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    calendar_ids: list[int],
    include: list[GetCalendarsAppointmentsIncludeItem] | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    query: str | Unset = UNSET,
) -> Response[Any | GetCalendarsAppointmentsResponse200 | str]:
    """Get all appointments

    Args:
        calendar_ids (list[int]):
        include (list[GetCalendarsAppointmentsIncludeItem] | Unset):
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCalendarsAppointmentsResponse200 | str]
    """

    kwargs = _get_kwargs(
        calendar_ids=calendar_ids,
        include=include,
        from_=from_,
        to=to,
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    calendar_ids: list[int],
    include: list[GetCalendarsAppointmentsIncludeItem] | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    query: str | Unset = UNSET,
) -> Any | GetCalendarsAppointmentsResponse200 | str | None:
    """Get all appointments

    Args:
        calendar_ids (list[int]):
        include (list[GetCalendarsAppointmentsIncludeItem] | Unset):
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCalendarsAppointmentsResponse200 | str
    """

    return (
        await asyncio_detailed(
            client=client,
            calendar_ids=calendar_ids,
            include=include,
            from_=from_,
            to=to,
            query=query,
        )
    ).parsed
