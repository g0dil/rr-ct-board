from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tags_domain_type_domain_type import GetTagsDomainTypeDomainType
from ...models.get_tags_domain_type_response_200 import GetTagsDomainTypeResponse200
from ...types import Response


def _get_kwargs(
    domain_type: GetTagsDomainTypeDomainType,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tags/{domain_type}".format(
            domain_type=domain_type,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetTagsDomainTypeResponse200 | None:
    if response.status_code == 200:
        response_200 = GetTagsDomainTypeResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetTagsDomainTypeResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    domain_type: GetTagsDomainTypeDomainType,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetTagsDomainTypeResponse200]:
    """Get tags for domain type

     Get available tags for the specified domain type.

    Args:
        domain_type (GetTagsDomainTypeDomainType):  Example: person.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTagsDomainTypeResponse200]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    domain_type: GetTagsDomainTypeDomainType,
    *,
    client: AuthenticatedClient | Client,
) -> GetTagsDomainTypeResponse200 | None:
    """Get tags for domain type

     Get available tags for the specified domain type.

    Args:
        domain_type (GetTagsDomainTypeDomainType):  Example: person.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTagsDomainTypeResponse200
    """

    return sync_detailed(
        domain_type=domain_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    domain_type: GetTagsDomainTypeDomainType,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetTagsDomainTypeResponse200]:
    """Get tags for domain type

     Get available tags for the specified domain type.

    Args:
        domain_type (GetTagsDomainTypeDomainType):  Example: person.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTagsDomainTypeResponse200]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain_type: GetTagsDomainTypeDomainType,
    *,
    client: AuthenticatedClient | Client,
) -> GetTagsDomainTypeResponse200 | None:
    """Get tags for domain type

     Get available tags for the specified domain type.

    Args:
        domain_type (GetTagsDomainTypeDomainType):  Example: person.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTagsDomainTypeResponse200
    """

    return (
        await asyncio_detailed(
            domain_type=domain_type,
            client=client,
        )
    ).parsed
