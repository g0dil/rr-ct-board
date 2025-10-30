from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_sync_jobconfigs_response_200 import GetSyncJobconfigsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    external_system_ids: list[int] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_external_system_ids: list[int] | Unset = UNSET
    if not isinstance(external_system_ids, Unset):
        json_external_system_ids = external_system_ids

    params["external_system_ids[]"] = json_external_system_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sync/jobconfigs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSyncJobconfigsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSyncJobconfigsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetSyncJobconfigsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    external_system_ids: list[int] | Unset = UNSET,
) -> Response[GetSyncJobconfigsResponse200]:
    """Your GET endpoint

     Get all job configs for the sync

    Args:
        external_system_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSyncJobconfigsResponse200]
    """

    kwargs = _get_kwargs(
        external_system_ids=external_system_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    external_system_ids: list[int] | Unset = UNSET,
) -> GetSyncJobconfigsResponse200 | None:
    """Your GET endpoint

     Get all job configs for the sync

    Args:
        external_system_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSyncJobconfigsResponse200
    """

    return sync_detailed(
        client=client,
        external_system_ids=external_system_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    external_system_ids: list[int] | Unset = UNSET,
) -> Response[GetSyncJobconfigsResponse200]:
    """Your GET endpoint

     Get all job configs for the sync

    Args:
        external_system_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSyncJobconfigsResponse200]
    """

    kwargs = _get_kwargs(
        external_system_ids=external_system_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    external_system_ids: list[int] | Unset = UNSET,
) -> GetSyncJobconfigsResponse200 | None:
    """Your GET endpoint

     Get all job configs for the sync

    Args:
        external_system_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSyncJobconfigsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            external_system_ids=external_system_ids,
        )
    ).parsed
