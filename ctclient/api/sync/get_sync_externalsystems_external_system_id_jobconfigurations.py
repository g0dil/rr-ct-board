from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_sync_externalsystems_external_system_id_jobconfigurations_response_200 import (
    GetSyncExternalsystemsExternalSystemIdJobconfigurationsResponse200,
)
from ...types import Response


def _get_kwargs(
    external_system_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sync/externalsystems/{external_system_id}/jobconfigs".format(
            external_system_id=external_system_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSyncExternalsystemsExternalSystemIdJobconfigurationsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSyncExternalsystemsExternalSystemIdJobconfigurationsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetSyncExternalsystemsExternalSystemIdJobconfigurationsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    external_system_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetSyncExternalsystemsExternalSystemIdJobconfigurationsResponse200]:
    """GET Job configurations

     Get all job configurations for an external system

    Args:
        external_system_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSyncExternalsystemsExternalSystemIdJobconfigurationsResponse200]
    """

    kwargs = _get_kwargs(
        external_system_id=external_system_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    external_system_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetSyncExternalsystemsExternalSystemIdJobconfigurationsResponse200 | None:
    """GET Job configurations

     Get all job configurations for an external system

    Args:
        external_system_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSyncExternalsystemsExternalSystemIdJobconfigurationsResponse200
    """

    return sync_detailed(
        external_system_id=external_system_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    external_system_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetSyncExternalsystemsExternalSystemIdJobconfigurationsResponse200]:
    """GET Job configurations

     Get all job configurations for an external system

    Args:
        external_system_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSyncExternalsystemsExternalSystemIdJobconfigurationsResponse200]
    """

    kwargs = _get_kwargs(
        external_system_id=external_system_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    external_system_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetSyncExternalsystemsExternalSystemIdJobconfigurationsResponse200 | None:
    """GET Job configurations

     Get all job configurations for an external system

    Args:
        external_system_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSyncExternalsystemsExternalSystemIdJobconfigurationsResponse200
    """

    return (
        await asyncio_detailed(
            external_system_id=external_system_id,
            client=client,
        )
    ).parsed
