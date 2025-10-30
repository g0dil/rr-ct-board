from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_addresses_domain_type_domain_identifier_address_id_body import (
    PutAddressesDomainTypeDomainIdentifierAddressIdBody,
)
from ...models.put_addresses_domain_type_domain_identifier_address_id_response_200 import (
    PutAddressesDomainTypeDomainIdentifierAddressIdResponse200,
)
from ...types import Response


def _get_kwargs(
    domain_type: Any,
    domain_identifier: str,
    address_id: int,
    *,
    body: PutAddressesDomainTypeDomainIdentifierAddressIdBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/addresses/{domain_type}/{domain_identifier}/{address_id}".format(
            domain_type=domain_type,
            domain_identifier=domain_identifier,
            address_id=address_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutAddressesDomainTypeDomainIdentifierAddressIdResponse200 | str | None:
    if response.status_code == 200:
        response_200 = (
            PutAddressesDomainTypeDomainIdentifierAddressIdResponse200.from_dict(
                response.json()
            )
        )

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
) -> Response[Any | PutAddressesDomainTypeDomainIdentifierAddressIdResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    domain_type: Any,
    domain_identifier: str,
    address_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PutAddressesDomainTypeDomainIdentifierAddressIdBody,
) -> Response[Any | PutAddressesDomainTypeDomainIdentifierAddressIdResponse200 | str]:
    """Update address

    Args:
        domain_type (Any):
        domain_identifier (str):
        address_id (int):
        body (PutAddressesDomainTypeDomainIdentifierAddressIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutAddressesDomainTypeDomainIdentifierAddressIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
        domain_identifier=domain_identifier,
        address_id=address_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    domain_type: Any,
    domain_identifier: str,
    address_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PutAddressesDomainTypeDomainIdentifierAddressIdBody,
) -> Any | PutAddressesDomainTypeDomainIdentifierAddressIdResponse200 | str | None:
    """Update address

    Args:
        domain_type (Any):
        domain_identifier (str):
        address_id (int):
        body (PutAddressesDomainTypeDomainIdentifierAddressIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutAddressesDomainTypeDomainIdentifierAddressIdResponse200 | str
    """

    return sync_detailed(
        domain_type=domain_type,
        domain_identifier=domain_identifier,
        address_id=address_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    domain_type: Any,
    domain_identifier: str,
    address_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PutAddressesDomainTypeDomainIdentifierAddressIdBody,
) -> Response[Any | PutAddressesDomainTypeDomainIdentifierAddressIdResponse200 | str]:
    """Update address

    Args:
        domain_type (Any):
        domain_identifier (str):
        address_id (int):
        body (PutAddressesDomainTypeDomainIdentifierAddressIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutAddressesDomainTypeDomainIdentifierAddressIdResponse200 | str]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
        domain_identifier=domain_identifier,
        address_id=address_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain_type: Any,
    domain_identifier: str,
    address_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PutAddressesDomainTypeDomainIdentifierAddressIdBody,
) -> Any | PutAddressesDomainTypeDomainIdentifierAddressIdResponse200 | str | None:
    """Update address

    Args:
        domain_type (Any):
        domain_identifier (str):
        address_id (int):
        body (PutAddressesDomainTypeDomainIdentifierAddressIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutAddressesDomainTypeDomainIdentifierAddressIdResponse200 | str
    """

    return (
        await asyncio_detailed(
            domain_type=domain_type,
            domain_identifier=domain_identifier,
            address_id=address_id,
            client=client,
            body=body,
        )
    ).parsed
