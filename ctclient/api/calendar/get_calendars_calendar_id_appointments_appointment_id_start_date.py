from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    calendar_id: int,
    appointment_id: int,
    start_date: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/calendars/{calendar_id}/appointments/{appointment_id}/{start_date}".format(
            calendar_id=calendar_id,
            appointment_id=appointment_id,
            start_date=start_date,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | str | None:
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
) -> Response[Any | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    calendar_id: int,
    appointment_id: int,
    start_date: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | str]:
    """Get an appointment with all bookings and meeting requests

    Args:
        calendar_id (int):  Example: 42.
        appointment_id (int):  Example: 4.
        start_date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        calendar_id=calendar_id,
        appointment_id=appointment_id,
        start_date=start_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    calendar_id: int,
    appointment_id: int,
    start_date: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | str | None:
    """Get an appointment with all bookings and meeting requests

    Args:
        calendar_id (int):  Example: 42.
        appointment_id (int):  Example: 4.
        start_date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        calendar_id=calendar_id,
        appointment_id=appointment_id,
        start_date=start_date,
        client=client,
    ).parsed


async def asyncio_detailed(
    calendar_id: int,
    appointment_id: int,
    start_date: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | str]:
    """Get an appointment with all bookings and meeting requests

    Args:
        calendar_id (int):  Example: 42.
        appointment_id (int):  Example: 4.
        start_date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        calendar_id=calendar_id,
        appointment_id=appointment_id,
        start_date=start_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    calendar_id: int,
    appointment_id: int,
    start_date: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | str | None:
    """Get an appointment with all bookings and meeting requests

    Args:
        calendar_id (int):  Example: 42.
        appointment_id (int):  Example: 4.
        start_date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            calendar_id=calendar_id,
            appointment_id=appointment_id,
            start_date=start_date,
            client=client,
        )
    ).parsed
