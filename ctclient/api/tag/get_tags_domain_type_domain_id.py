from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tags_domain_type_domain_id_domain_type import (
    GetTagsDomainTypeDomainIdDomainType,
)
from ...models.get_tags_domain_type_domain_id_response_200 import (
    GetTagsDomainTypeDomainIdResponse200,
)
from ...types import Response


def _get_kwargs(
    domain_type: GetTagsDomainTypeDomainIdDomainType,
    domain_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tags/{domain_type}/{domain_id}".format(
            domain_type=domain_type,
            domain_id=domain_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetTagsDomainTypeDomainIdResponse200 | str | None:
    if response.status_code == 200:
        response_200 = GetTagsDomainTypeDomainIdResponse200.from_dict(response.json())

        return response_200

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
) -> Response[Any | GetTagsDomainTypeDomainIdResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    domain_type: GetTagsDomainTypeDomainIdDomainType,
    domain_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetTagsDomainTypeDomainIdResponse200 | str]:
    """Get tags for domain object

     Get available tags for the specified domain object.

    Args:
        domain_type (GetTagsDomainTypeDomainIdDomainType):  Example: person.
        domain_id (int):  Example: 35.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTagsDomainTypeDomainIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
        domain_id=domain_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    domain_type: GetTagsDomainTypeDomainIdDomainType,
    domain_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetTagsDomainTypeDomainIdResponse200 | str | None:
    """Get tags for domain object

     Get available tags for the specified domain object.

    Args:
        domain_type (GetTagsDomainTypeDomainIdDomainType):  Example: person.
        domain_id (int):  Example: 35.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTagsDomainTypeDomainIdResponse200 | str
    """

    return sync_detailed(
        domain_type=domain_type,
        domain_id=domain_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    domain_type: GetTagsDomainTypeDomainIdDomainType,
    domain_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetTagsDomainTypeDomainIdResponse200 | str]:
    """Get tags for domain object

     Get available tags for the specified domain object.

    Args:
        domain_type (GetTagsDomainTypeDomainIdDomainType):  Example: person.
        domain_id (int):  Example: 35.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTagsDomainTypeDomainIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
        domain_id=domain_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain_type: GetTagsDomainTypeDomainIdDomainType,
    domain_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetTagsDomainTypeDomainIdResponse200 | str | None:
    """Get tags for domain object

     Get available tags for the specified domain object.

    Args:
        domain_type (GetTagsDomainTypeDomainIdDomainType):  Example: person.
        domain_id (int):  Example: 35.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTagsDomainTypeDomainIdResponse200 | str
    """

    return (
        await asyncio_detailed(
            domain_type=domain_type,
            domain_id=domain_id,
            client=client,
        )
    ).parsed
