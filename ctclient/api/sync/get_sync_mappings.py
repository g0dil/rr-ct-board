from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_sync_mappings_response_200 import GetSyncMappingsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    domain_type: list[str] | Unset = UNSET,
    domain_id: str | Unset = UNSET,
    source_id: str | Unset = UNSET,
    scope: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_domain_type: list[str] | Unset = UNSET
    if not isinstance(domain_type, Unset):
        json_domain_type = domain_type

    params["domain_type"] = json_domain_type

    params["domain_id"] = domain_id

    params["source_id"] = source_id

    params["scope"] = scope

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sync/entitymappings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSyncMappingsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSyncMappingsResponse200.from_dict(response.json())

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
) -> Response[Any | GetSyncMappingsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    domain_type: list[str] | Unset = UNSET,
    domain_id: str | Unset = UNSET,
    source_id: str | Unset = UNSET,
    scope: str | Unset = UNSET,
) -> Response[Any | GetSyncMappingsResponse200]:
    """Fetch all registered mappings

     The Sync module saved a mapping relationship for every entity. This mapping consists of a
    `domainType` like `person` oder `transaction` (ChurchTools domain type) and its `domainId` to
    identify the entity. And secondly, the corresponding entity on the third party system with its ID.

    Args:
        domain_type (list[str] | Unset):
        domain_id (str | Unset):
        source_id (str | Unset):
        scope (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSyncMappingsResponse200]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
        domain_id=domain_id,
        source_id=source_id,
        scope=scope,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    domain_type: list[str] | Unset = UNSET,
    domain_id: str | Unset = UNSET,
    source_id: str | Unset = UNSET,
    scope: str | Unset = UNSET,
) -> Any | GetSyncMappingsResponse200 | None:
    """Fetch all registered mappings

     The Sync module saved a mapping relationship for every entity. This mapping consists of a
    `domainType` like `person` oder `transaction` (ChurchTools domain type) and its `domainId` to
    identify the entity. And secondly, the corresponding entity on the third party system with its ID.

    Args:
        domain_type (list[str] | Unset):
        domain_id (str | Unset):
        source_id (str | Unset):
        scope (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSyncMappingsResponse200
    """

    return sync_detailed(
        client=client,
        domain_type=domain_type,
        domain_id=domain_id,
        source_id=source_id,
        scope=scope,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    domain_type: list[str] | Unset = UNSET,
    domain_id: str | Unset = UNSET,
    source_id: str | Unset = UNSET,
    scope: str | Unset = UNSET,
) -> Response[Any | GetSyncMappingsResponse200]:
    """Fetch all registered mappings

     The Sync module saved a mapping relationship for every entity. This mapping consists of a
    `domainType` like `person` oder `transaction` (ChurchTools domain type) and its `domainId` to
    identify the entity. And secondly, the corresponding entity on the third party system with its ID.

    Args:
        domain_type (list[str] | Unset):
        domain_id (str | Unset):
        source_id (str | Unset):
        scope (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSyncMappingsResponse200]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
        domain_id=domain_id,
        source_id=source_id,
        scope=scope,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    domain_type: list[str] | Unset = UNSET,
    domain_id: str | Unset = UNSET,
    source_id: str | Unset = UNSET,
    scope: str | Unset = UNSET,
) -> Any | GetSyncMappingsResponse200 | None:
    """Fetch all registered mappings

     The Sync module saved a mapping relationship for every entity. This mapping consists of a
    `domainType` like `person` oder `transaction` (ChurchTools domain type) and its `domainId` to
    identify the entity. And secondly, the corresponding entity on the third party system with its ID.

    Args:
        domain_type (list[str] | Unset):
        domain_id (str | Unset):
        source_id (str | Unset):
        scope (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSyncMappingsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            domain_type=domain_type,
            domain_id=domain_id,
            source_id=source_id,
            scope=scope,
        )
    ).parsed
