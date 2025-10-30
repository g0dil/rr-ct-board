from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    domain_type: Any,
    domain_identifier: str,
    address_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/addresses/{domain_type}/{domain_identifier}/{address_id}".format(
            domain_type=domain_type,
            domain_identifier=domain_identifier,
            address_id=address_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | str | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | str]:
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
) -> Response[Any | str]:
    """Delete address

    Args:
        domain_type (Any):
        domain_identifier (str):
        address_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
        domain_identifier=domain_identifier,
        address_id=address_id,
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
) -> Any | str | None:
    """Delete address

    Args:
        domain_type (Any):
        domain_identifier (str):
        address_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        domain_type=domain_type,
        domain_identifier=domain_identifier,
        address_id=address_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    domain_type: Any,
    domain_identifier: str,
    address_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | str]:
    """Delete address

    Args:
        domain_type (Any):
        domain_identifier (str):
        address_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        domain_type=domain_type,
        domain_identifier=domain_identifier,
        address_id=address_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain_type: Any,
    domain_identifier: str,
    address_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | str | None:
    """Delete address

    Args:
        domain_type (Any):
        domain_identifier (str):
        address_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            domain_type=domain_type,
            domain_identifier=domain_identifier,
            address_id=address_id,
            client=client,
        )
    ).parsed
