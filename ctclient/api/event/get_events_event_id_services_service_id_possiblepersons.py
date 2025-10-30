from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    event_id: int,
    service_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events/{event_id}/services/{service_id}/possiblepersons".format(
            event_id=event_id,
            service_id=service_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | str | None:
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = response.text
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
) -> Response[Any | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_id: int,
    service_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | str]:
    """Get all possible persons for a service

     Gets a list of all possible persons for a service with their availability

    Args:
        event_id (int):  Example: 42.
        service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        service_id=service_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_id: int,
    service_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | str | None:
    """Get all possible persons for a service

     Gets a list of all possible persons for a service with their availability

    Args:
        event_id (int):  Example: 42.
        service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        event_id=event_id,
        service_id=service_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    event_id: int,
    service_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | str]:
    """Get all possible persons for a service

     Gets a list of all possible persons for a service with their availability

    Args:
        event_id (int):  Example: 42.
        service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        service_id=service_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_id: int,
    service_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | str | None:
    """Get all possible persons for a service

     Gets a list of all possible persons for a service with their availability

    Args:
        event_id (int):  Example: 42.
        service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            service_id=service_id,
            client=client,
        )
    ).parsed
