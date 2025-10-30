import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_sync_logs_response_200 import GetSyncLogsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    es_ids: list[int] | Unset = UNSET,
    job_ids: list[int] | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    types: list[int] | Unset = UNSET,
    query: str | Unset = UNSET,
    levels: list[str] | Unset = UNSET,
    is_dry_run: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    json_es_ids: list[int] | Unset = UNSET
    if not isinstance(es_ids, Unset):
        json_es_ids = es_ids

    params["es_ids[]"] = json_es_ids

    json_job_ids: list[int] | Unset = UNSET
    if not isinstance(job_ids, Unset):
        json_job_ids = job_ids

    params["job_ids[]"] = json_job_ids

    json_start_date: str | Unset = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    json_end_date: str | Unset = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date

    json_types: list[int] | Unset = UNSET
    if not isinstance(types, Unset):
        json_types = types

    params["types"] = json_types

    params["query"] = query

    json_levels: list[str] | Unset = UNSET
    if not isinstance(levels, Unset):
        json_levels = levels

    params["levels"] = json_levels

    params["is_dry_run"] = is_dry_run

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sync/logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSyncLogsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSyncLogsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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
) -> Response[Any | GetSyncLogsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    es_ids: list[int] | Unset = UNSET,
    job_ids: list[int] | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    types: list[int] | Unset = UNSET,
    query: str | Unset = UNSET,
    levels: list[str] | Unset = UNSET,
    is_dry_run: bool | Unset = UNSET,
) -> Response[Any | GetSyncLogsResponse200]:
    """Get Sync Logs

     Fetch all

    Args:
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        es_ids (list[int] | Unset):
        job_ids (list[int] | Unset):
        start_date (datetime.date | Unset):  Example: 2021-02-01.
        end_date (datetime.date | Unset):  Example: 2021-02-01.
        types (list[int] | Unset):
        query (str | Unset):
        levels (list[str] | Unset):
        is_dry_run (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSyncLogsResponse200]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        es_ids=es_ids,
        job_ids=job_ids,
        start_date=start_date,
        end_date=end_date,
        types=types,
        query=query,
        levels=levels,
        is_dry_run=is_dry_run,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    es_ids: list[int] | Unset = UNSET,
    job_ids: list[int] | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    types: list[int] | Unset = UNSET,
    query: str | Unset = UNSET,
    levels: list[str] | Unset = UNSET,
    is_dry_run: bool | Unset = UNSET,
) -> Any | GetSyncLogsResponse200 | None:
    """Get Sync Logs

     Fetch all

    Args:
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        es_ids (list[int] | Unset):
        job_ids (list[int] | Unset):
        start_date (datetime.date | Unset):  Example: 2021-02-01.
        end_date (datetime.date | Unset):  Example: 2021-02-01.
        types (list[int] | Unset):
        query (str | Unset):
        levels (list[str] | Unset):
        is_dry_run (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSyncLogsResponse200
    """

    return sync_detailed(
        client=client,
        page=page,
        limit=limit,
        es_ids=es_ids,
        job_ids=job_ids,
        start_date=start_date,
        end_date=end_date,
        types=types,
        query=query,
        levels=levels,
        is_dry_run=is_dry_run,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    es_ids: list[int] | Unset = UNSET,
    job_ids: list[int] | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    types: list[int] | Unset = UNSET,
    query: str | Unset = UNSET,
    levels: list[str] | Unset = UNSET,
    is_dry_run: bool | Unset = UNSET,
) -> Response[Any | GetSyncLogsResponse200]:
    """Get Sync Logs

     Fetch all

    Args:
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        es_ids (list[int] | Unset):
        job_ids (list[int] | Unset):
        start_date (datetime.date | Unset):  Example: 2021-02-01.
        end_date (datetime.date | Unset):  Example: 2021-02-01.
        types (list[int] | Unset):
        query (str | Unset):
        levels (list[str] | Unset):
        is_dry_run (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSyncLogsResponse200]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        es_ids=es_ids,
        job_ids=job_ids,
        start_date=start_date,
        end_date=end_date,
        types=types,
        query=query,
        levels=levels,
        is_dry_run=is_dry_run,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    es_ids: list[int] | Unset = UNSET,
    job_ids: list[int] | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    types: list[int] | Unset = UNSET,
    query: str | Unset = UNSET,
    levels: list[str] | Unset = UNSET,
    is_dry_run: bool | Unset = UNSET,
) -> Any | GetSyncLogsResponse200 | None:
    """Get Sync Logs

     Fetch all

    Args:
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        es_ids (list[int] | Unset):
        job_ids (list[int] | Unset):
        start_date (datetime.date | Unset):  Example: 2021-02-01.
        end_date (datetime.date | Unset):  Example: 2021-02-01.
        types (list[int] | Unset):
        query (str | Unset):
        levels (list[str] | Unset):
        is_dry_run (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSyncLogsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            limit=limit,
            es_ids=es_ids,
            job_ids=job_ids,
            start_date=start_date,
            end_date=end_date,
            types=types,
            query=query,
            levels=levels,
            is_dry_run=is_dry_run,
        )
    ).parsed
