import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.change_impact_additionals_item import ChangeImpactAdditionalsItem
from ...models.change_impact_exceptions_item import ChangeImpactExceptionsItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    calendar_id: int,
    appointment_id_path: int,
    *,
    additionals: list[ChangeImpactAdditionalsItem] | Unset = UNSET,
    appointment_id_query: int | Unset = UNSET,
    end_date: datetime.datetime | Unset = UNSET,
    exceptions: list[ChangeImpactExceptionsItem] | Unset = UNSET,
    repeat_frequency: int | Unset = UNSET,
    repeat_id: int | Unset = UNSET,
    repeat_option: int | Unset = UNSET,
    repeat_until: datetime.date | Unset = UNSET,
    start_date: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_additionals: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(additionals, Unset):
        json_additionals = []
        for additionals_item_data in additionals:
            additionals_item = additionals_item_data.to_dict()
            json_additionals.append(additionals_item)

    params["additionals"] = json_additionals

    params["appointmentId"] = appointment_id_query

    json_end_date: str | Unset = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    json_exceptions: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(exceptions, Unset):
        json_exceptions = []
        for exceptions_item_data in exceptions:
            exceptions_item = exceptions_item_data.to_dict()
            json_exceptions.append(exceptions_item)

    params["exceptions"] = json_exceptions

    params["repeatFrequency"] = repeat_frequency

    params["repeatId"] = repeat_id

    params["repeatOption"] = repeat_option

    json_repeat_until: str | Unset = UNSET
    if not isinstance(repeat_until, Unset):
        json_repeat_until = repeat_until.isoformat()
    params["repeatUntil"] = json_repeat_until

    json_start_date: str | Unset = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/calendars/{calendar_id}/appointments/{appointment_id_path}/changeimpact".format(
            calendar_id=calendar_id,
            appointment_id_path=appointment_id_path,
        ),
        "params": params,
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
    appointment_id_path: int,
    *,
    client: AuthenticatedClient | Client,
    additionals: list[ChangeImpactAdditionalsItem] | Unset = UNSET,
    appointment_id_query: int | Unset = UNSET,
    end_date: datetime.datetime | Unset = UNSET,
    exceptions: list[ChangeImpactExceptionsItem] | Unset = UNSET,
    repeat_frequency: int | Unset = UNSET,
    repeat_id: int | Unset = UNSET,
    repeat_option: int | Unset = UNSET,
    repeat_until: datetime.date | Unset = UNSET,
    start_date: datetime.datetime | Unset = UNSET,
) -> Response[Any | str]:
    """Get the change of impact of an appointment

    Args:
        calendar_id (int):  Example: 42.
        appointment_id_path (int):  Example: 4.
        additionals (list[ChangeImpactAdditionalsItem] | Unset):
        appointment_id_query (int | Unset):
        end_date (datetime.datetime | Unset):  Example: 2022-01-01T12:00:00Z.
        exceptions (list[ChangeImpactExceptionsItem] | Unset):
        repeat_frequency (int | Unset):
        repeat_id (int | Unset):
        repeat_option (int | Unset):
        repeat_until (datetime.date | Unset):  Example: 2022-01-01.
        start_date (datetime.datetime | Unset):  Example: 2022-01-01T12:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        calendar_id=calendar_id,
        appointment_id_path=appointment_id_path,
        additionals=additionals,
        appointment_id_query=appointment_id_query,
        end_date=end_date,
        exceptions=exceptions,
        repeat_frequency=repeat_frequency,
        repeat_id=repeat_id,
        repeat_option=repeat_option,
        repeat_until=repeat_until,
        start_date=start_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    calendar_id: int,
    appointment_id_path: int,
    *,
    client: AuthenticatedClient | Client,
    additionals: list[ChangeImpactAdditionalsItem] | Unset = UNSET,
    appointment_id_query: int | Unset = UNSET,
    end_date: datetime.datetime | Unset = UNSET,
    exceptions: list[ChangeImpactExceptionsItem] | Unset = UNSET,
    repeat_frequency: int | Unset = UNSET,
    repeat_id: int | Unset = UNSET,
    repeat_option: int | Unset = UNSET,
    repeat_until: datetime.date | Unset = UNSET,
    start_date: datetime.datetime | Unset = UNSET,
) -> Any | str | None:
    """Get the change of impact of an appointment

    Args:
        calendar_id (int):  Example: 42.
        appointment_id_path (int):  Example: 4.
        additionals (list[ChangeImpactAdditionalsItem] | Unset):
        appointment_id_query (int | Unset):
        end_date (datetime.datetime | Unset):  Example: 2022-01-01T12:00:00Z.
        exceptions (list[ChangeImpactExceptionsItem] | Unset):
        repeat_frequency (int | Unset):
        repeat_id (int | Unset):
        repeat_option (int | Unset):
        repeat_until (datetime.date | Unset):  Example: 2022-01-01.
        start_date (datetime.datetime | Unset):  Example: 2022-01-01T12:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        calendar_id=calendar_id,
        appointment_id_path=appointment_id_path,
        client=client,
        additionals=additionals,
        appointment_id_query=appointment_id_query,
        end_date=end_date,
        exceptions=exceptions,
        repeat_frequency=repeat_frequency,
        repeat_id=repeat_id,
        repeat_option=repeat_option,
        repeat_until=repeat_until,
        start_date=start_date,
    ).parsed


async def asyncio_detailed(
    calendar_id: int,
    appointment_id_path: int,
    *,
    client: AuthenticatedClient | Client,
    additionals: list[ChangeImpactAdditionalsItem] | Unset = UNSET,
    appointment_id_query: int | Unset = UNSET,
    end_date: datetime.datetime | Unset = UNSET,
    exceptions: list[ChangeImpactExceptionsItem] | Unset = UNSET,
    repeat_frequency: int | Unset = UNSET,
    repeat_id: int | Unset = UNSET,
    repeat_option: int | Unset = UNSET,
    repeat_until: datetime.date | Unset = UNSET,
    start_date: datetime.datetime | Unset = UNSET,
) -> Response[Any | str]:
    """Get the change of impact of an appointment

    Args:
        calendar_id (int):  Example: 42.
        appointment_id_path (int):  Example: 4.
        additionals (list[ChangeImpactAdditionalsItem] | Unset):
        appointment_id_query (int | Unset):
        end_date (datetime.datetime | Unset):  Example: 2022-01-01T12:00:00Z.
        exceptions (list[ChangeImpactExceptionsItem] | Unset):
        repeat_frequency (int | Unset):
        repeat_id (int | Unset):
        repeat_option (int | Unset):
        repeat_until (datetime.date | Unset):  Example: 2022-01-01.
        start_date (datetime.datetime | Unset):  Example: 2022-01-01T12:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        calendar_id=calendar_id,
        appointment_id_path=appointment_id_path,
        additionals=additionals,
        appointment_id_query=appointment_id_query,
        end_date=end_date,
        exceptions=exceptions,
        repeat_frequency=repeat_frequency,
        repeat_id=repeat_id,
        repeat_option=repeat_option,
        repeat_until=repeat_until,
        start_date=start_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    calendar_id: int,
    appointment_id_path: int,
    *,
    client: AuthenticatedClient | Client,
    additionals: list[ChangeImpactAdditionalsItem] | Unset = UNSET,
    appointment_id_query: int | Unset = UNSET,
    end_date: datetime.datetime | Unset = UNSET,
    exceptions: list[ChangeImpactExceptionsItem] | Unset = UNSET,
    repeat_frequency: int | Unset = UNSET,
    repeat_id: int | Unset = UNSET,
    repeat_option: int | Unset = UNSET,
    repeat_until: datetime.date | Unset = UNSET,
    start_date: datetime.datetime | Unset = UNSET,
) -> Any | str | None:
    """Get the change of impact of an appointment

    Args:
        calendar_id (int):  Example: 42.
        appointment_id_path (int):  Example: 4.
        additionals (list[ChangeImpactAdditionalsItem] | Unset):
        appointment_id_query (int | Unset):
        end_date (datetime.datetime | Unset):  Example: 2022-01-01T12:00:00Z.
        exceptions (list[ChangeImpactExceptionsItem] | Unset):
        repeat_frequency (int | Unset):
        repeat_id (int | Unset):
        repeat_option (int | Unset):
        repeat_until (datetime.date | Unset):  Example: 2022-01-01.
        start_date (datetime.datetime | Unset):  Example: 2022-01-01T12:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            calendar_id=calendar_id,
            appointment_id_path=appointment_id_path,
            client=client,
            additionals=additionals,
            appointment_id_query=appointment_id_query,
            end_date=end_date,
            exceptions=exceptions,
            repeat_frequency=repeat_frequency,
            repeat_id=repeat_id,
            repeat_option=repeat_option,
            repeat_until=repeat_until,
            start_date=start_date,
        )
    ).parsed
