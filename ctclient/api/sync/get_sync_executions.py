import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_sync_executions_response_200 import GetSyncExecutionsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    es_ids: list[int] | Unset = UNSET,
    job_ids: list[int] | Unset = UNSET,
    start_date: datetime.datetime | Unset = UNSET,
    end_date: datetime.datetime | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    is_dry_run: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

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

    json_statuses: list[str] | Unset = UNSET
    if not isinstance(statuses, Unset):
        json_statuses = statuses

    params["statuses"] = json_statuses

    params["page"] = page

    params["limit"] = limit

    params["is_dry_run"] = is_dry_run

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sync/executions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSyncExecutionsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSyncExecutionsResponse200.from_dict(response.json())

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
) -> Response[Any | GetSyncExecutionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    es_ids: list[int] | Unset = UNSET,
    job_ids: list[int] | Unset = UNSET,
    start_date: datetime.datetime | Unset = UNSET,
    end_date: datetime.datetime | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    is_dry_run: bool | Unset = UNSET,
) -> Response[Any | GetSyncExecutionsResponse200]:
    """Statistical Information about Sync Executions

     Fetch statistical information about sync executions, like count of created entities, linked ones,
    etc.

    Result is ordered by execution start date.

    Args:
        es_ids (list[int] | Unset):
        job_ids (list[int] | Unset):
        start_date (datetime.datetime | Unset):
        end_date (datetime.datetime | Unset):
        statuses (list[str] | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        is_dry_run (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSyncExecutionsResponse200]
    """

    kwargs = _get_kwargs(
        es_ids=es_ids,
        job_ids=job_ids,
        start_date=start_date,
        end_date=end_date,
        statuses=statuses,
        page=page,
        limit=limit,
        is_dry_run=is_dry_run,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    es_ids: list[int] | Unset = UNSET,
    job_ids: list[int] | Unset = UNSET,
    start_date: datetime.datetime | Unset = UNSET,
    end_date: datetime.datetime | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    is_dry_run: bool | Unset = UNSET,
) -> Any | GetSyncExecutionsResponse200 | None:
    """Statistical Information about Sync Executions

     Fetch statistical information about sync executions, like count of created entities, linked ones,
    etc.

    Result is ordered by execution start date.

    Args:
        es_ids (list[int] | Unset):
        job_ids (list[int] | Unset):
        start_date (datetime.datetime | Unset):
        end_date (datetime.datetime | Unset):
        statuses (list[str] | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        is_dry_run (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSyncExecutionsResponse200
    """

    return sync_detailed(
        client=client,
        es_ids=es_ids,
        job_ids=job_ids,
        start_date=start_date,
        end_date=end_date,
        statuses=statuses,
        page=page,
        limit=limit,
        is_dry_run=is_dry_run,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    es_ids: list[int] | Unset = UNSET,
    job_ids: list[int] | Unset = UNSET,
    start_date: datetime.datetime | Unset = UNSET,
    end_date: datetime.datetime | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    is_dry_run: bool | Unset = UNSET,
) -> Response[Any | GetSyncExecutionsResponse200]:
    """Statistical Information about Sync Executions

     Fetch statistical information about sync executions, like count of created entities, linked ones,
    etc.

    Result is ordered by execution start date.

    Args:
        es_ids (list[int] | Unset):
        job_ids (list[int] | Unset):
        start_date (datetime.datetime | Unset):
        end_date (datetime.datetime | Unset):
        statuses (list[str] | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        is_dry_run (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSyncExecutionsResponse200]
    """

    kwargs = _get_kwargs(
        es_ids=es_ids,
        job_ids=job_ids,
        start_date=start_date,
        end_date=end_date,
        statuses=statuses,
        page=page,
        limit=limit,
        is_dry_run=is_dry_run,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    es_ids: list[int] | Unset = UNSET,
    job_ids: list[int] | Unset = UNSET,
    start_date: datetime.datetime | Unset = UNSET,
    end_date: datetime.datetime | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    is_dry_run: bool | Unset = UNSET,
) -> Any | GetSyncExecutionsResponse200 | None:
    """Statistical Information about Sync Executions

     Fetch statistical information about sync executions, like count of created entities, linked ones,
    etc.

    Result is ordered by execution start date.

    Args:
        es_ids (list[int] | Unset):
        job_ids (list[int] | Unset):
        start_date (datetime.datetime | Unset):
        end_date (datetime.datetime | Unset):
        statuses (list[str] | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        is_dry_run (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSyncExecutionsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            es_ids=es_ids,
            job_ids=job_ids,
            start_date=start_date,
            end_date=end_date,
            statuses=statuses,
            page=page,
            limit=limit,
            is_dry_run=is_dry_run,
        )
    ).parsed
