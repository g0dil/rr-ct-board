import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_logs_response_200 import GetAllLogsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    message: str | Unset = UNSET,
    levels: list[str] | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    person_id: int | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["message"] = message

    json_levels: list[str] | Unset = UNSET
    if not isinstance(levels, Unset):
        json_levels = levels

    params["levels[]"] = json_levels

    json_before: str | Unset = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat()
    params["before"] = json_before

    json_after: str | Unset = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat()
    params["after"] = json_after

    params["person_id"] = person_id

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetAllLogsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetAllLogsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
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
) -> Response[Any | GetAllLogsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    message: str | Unset = UNSET,
    levels: list[str] | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    person_id: int | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> Response[Any | GetAllLogsResponse200]:
    """Get all log messages

     The response is a collection of all log messages you may see and is limited to a specific number of
    messages. You can use the `page` parameter to browse the list of log messages. The logs are ordered
    by date.

    Args:
        message (str | Unset):  Example: Person updated.
        levels (list[str] | Unset):
        before (datetime.datetime | Unset):  Example: 2019-04-16T10:57:09Z.
        after (datetime.datetime | Unset):  Example: 2019-04-16T10:57:09Z.
        person_id (int | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAllLogsResponse200]
    """

    kwargs = _get_kwargs(
        message=message,
        levels=levels,
        before=before,
        after=after,
        person_id=person_id,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    message: str | Unset = UNSET,
    levels: list[str] | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    person_id: int | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> Any | GetAllLogsResponse200 | None:
    """Get all log messages

     The response is a collection of all log messages you may see and is limited to a specific number of
    messages. You can use the `page` parameter to browse the list of log messages. The logs are ordered
    by date.

    Args:
        message (str | Unset):  Example: Person updated.
        levels (list[str] | Unset):
        before (datetime.datetime | Unset):  Example: 2019-04-16T10:57:09Z.
        after (datetime.datetime | Unset):  Example: 2019-04-16T10:57:09Z.
        person_id (int | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAllLogsResponse200
    """

    return sync_detailed(
        client=client,
        message=message,
        levels=levels,
        before=before,
        after=after,
        person_id=person_id,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    message: str | Unset = UNSET,
    levels: list[str] | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    person_id: int | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> Response[Any | GetAllLogsResponse200]:
    """Get all log messages

     The response is a collection of all log messages you may see and is limited to a specific number of
    messages. You can use the `page` parameter to browse the list of log messages. The logs are ordered
    by date.

    Args:
        message (str | Unset):  Example: Person updated.
        levels (list[str] | Unset):
        before (datetime.datetime | Unset):  Example: 2019-04-16T10:57:09Z.
        after (datetime.datetime | Unset):  Example: 2019-04-16T10:57:09Z.
        person_id (int | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAllLogsResponse200]
    """

    kwargs = _get_kwargs(
        message=message,
        levels=levels,
        before=before,
        after=after,
        person_id=person_id,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    message: str | Unset = UNSET,
    levels: list[str] | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    person_id: int | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> Any | GetAllLogsResponse200 | None:
    """Get all log messages

     The response is a collection of all log messages you may see and is limited to a specific number of
    messages. You can use the `page` parameter to browse the list of log messages. The logs are ordered
    by date.

    Args:
        message (str | Unset):  Example: Person updated.
        levels (list[str] | Unset):
        before (datetime.datetime | Unset):  Example: 2019-04-16T10:57:09Z.
        after (datetime.datetime | Unset):  Example: 2019-04-16T10:57:09Z.
        person_id (int | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAllLogsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            message=message,
            levels=levels,
            before=before,
            after=after,
            person_id=person_id,
            page=page,
            limit=limit,
        )
    ).parsed
