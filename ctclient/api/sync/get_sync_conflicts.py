from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_sync_conflicts_response_200 import GetSyncConflictsResponse200
from ...models.get_sync_conflicts_types_item import GetSyncConflictsTypesItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    types: list[GetSyncConflictsTypesItem] | Unset = UNSET,
    domain_types: list[str] | Unset = UNSET,
    source_ids: list[int] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_types: list[str] | Unset = UNSET
    if not isinstance(types, Unset):
        json_types = []
        for types_item_data in types:
            types_item = types_item_data.value
            json_types.append(types_item)

    params["types[]"] = json_types

    json_domain_types: list[str] | Unset = UNSET
    if not isinstance(domain_types, Unset):
        json_domain_types = domain_types

    params["domain_types[]"] = json_domain_types

    json_source_ids: list[int] | Unset = UNSET
    if not isinstance(source_ids, Unset):
        json_source_ids = source_ids

    params["source_ids[]"] = json_source_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sync/conflicts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSyncConflictsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSyncConflictsResponse200.from_dict(response.json())

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
) -> Response[Any | GetSyncConflictsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    types: list[GetSyncConflictsTypesItem] | Unset = UNSET,
    domain_types: list[str] | Unset = UNSET,
    source_ids: list[int] | Unset = UNSET,
) -> Response[Any | GetSyncConflictsResponse200]:
    """Fetch all conflicts

     When synchronizing two systems conflicts may appear. You can fetch know conflicts using this
    endpoint.

    Args:
        types (list[GetSyncConflictsTypesItem] | Unset):
        domain_types (list[str] | Unset):
        source_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSyncConflictsResponse200]
    """

    kwargs = _get_kwargs(
        types=types,
        domain_types=domain_types,
        source_ids=source_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    types: list[GetSyncConflictsTypesItem] | Unset = UNSET,
    domain_types: list[str] | Unset = UNSET,
    source_ids: list[int] | Unset = UNSET,
) -> Any | GetSyncConflictsResponse200 | None:
    """Fetch all conflicts

     When synchronizing two systems conflicts may appear. You can fetch know conflicts using this
    endpoint.

    Args:
        types (list[GetSyncConflictsTypesItem] | Unset):
        domain_types (list[str] | Unset):
        source_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSyncConflictsResponse200
    """

    return sync_detailed(
        client=client,
        types=types,
        domain_types=domain_types,
        source_ids=source_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    types: list[GetSyncConflictsTypesItem] | Unset = UNSET,
    domain_types: list[str] | Unset = UNSET,
    source_ids: list[int] | Unset = UNSET,
) -> Response[Any | GetSyncConflictsResponse200]:
    """Fetch all conflicts

     When synchronizing two systems conflicts may appear. You can fetch know conflicts using this
    endpoint.

    Args:
        types (list[GetSyncConflictsTypesItem] | Unset):
        domain_types (list[str] | Unset):
        source_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSyncConflictsResponse200]
    """

    kwargs = _get_kwargs(
        types=types,
        domain_types=domain_types,
        source_ids=source_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    types: list[GetSyncConflictsTypesItem] | Unset = UNSET,
    domain_types: list[str] | Unset = UNSET,
    source_ids: list[int] | Unset = UNSET,
) -> Any | GetSyncConflictsResponse200 | None:
    """Fetch all conflicts

     When synchronizing two systems conflicts may appear. You can fetch know conflicts using this
    endpoint.

    Args:
        types (list[GetSyncConflictsTypesItem] | Unset):
        domain_types (list[str] | Unset):
        source_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSyncConflictsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            types=types,
            domain_types=domain_types,
            source_ids=source_ids,
        )
    ).parsed
