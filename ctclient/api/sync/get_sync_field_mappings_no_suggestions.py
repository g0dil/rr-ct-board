from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_sync_field_mappings_no_suggestions_response_200 import (
    GetSyncFieldMappingsNoSuggestionsResponse200,
)
from ...types import Response


def _get_kwargs(
    external_system_id: str,
    domain_type: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sync/externalsystems/{external_system_id}/fieldmappings/{domain_type}/nosuggestions".format(
            external_system_id=external_system_id,
            domain_type=domain_type,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSyncFieldMappingsNoSuggestionsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSyncFieldMappingsNoSuggestionsResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
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
) -> Response[Any | GetSyncFieldMappingsNoSuggestionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    external_system_id: str,
    domain_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetSyncFieldMappingsNoSuggestionsResponse200]:
    """Get fields for which no suggestions should be shown

     Get fields for which no suggestions should be shown, for an external system of a specific domain
    type.

    Args:
        external_system_id (str):
        domain_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSyncFieldMappingsNoSuggestionsResponse200]
    """

    kwargs = _get_kwargs(
        external_system_id=external_system_id,
        domain_type=domain_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    external_system_id: str,
    domain_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetSyncFieldMappingsNoSuggestionsResponse200 | None:
    """Get fields for which no suggestions should be shown

     Get fields for which no suggestions should be shown, for an external system of a specific domain
    type.

    Args:
        external_system_id (str):
        domain_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSyncFieldMappingsNoSuggestionsResponse200
    """

    return sync_detailed(
        external_system_id=external_system_id,
        domain_type=domain_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    external_system_id: str,
    domain_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetSyncFieldMappingsNoSuggestionsResponse200]:
    """Get fields for which no suggestions should be shown

     Get fields for which no suggestions should be shown, for an external system of a specific domain
    type.

    Args:
        external_system_id (str):
        domain_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSyncFieldMappingsNoSuggestionsResponse200]
    """

    kwargs = _get_kwargs(
        external_system_id=external_system_id,
        domain_type=domain_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    external_system_id: str,
    domain_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetSyncFieldMappingsNoSuggestionsResponse200 | None:
    """Get fields for which no suggestions should be shown

     Get fields for which no suggestions should be shown, for an external system of a specific domain
    type.

    Args:
        external_system_id (str):
        domain_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSyncFieldMappingsNoSuggestionsResponse200
    """

    return (
        await asyncio_detailed(
            external_system_id=external_system_id,
            domain_type=domain_type,
            client=client,
        )
    ).parsed
