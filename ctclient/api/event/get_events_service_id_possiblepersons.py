from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_events_service_id_possiblepersons_response_200 import (
    GetEventsServiceIdPossiblepersonsResponse200,
)
from ...types import Response


def _get_kwargs(
    service_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events/{service_id}/possiblepersonsforservice".format(
            service_id=service_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetEventsServiceIdPossiblepersonsResponse200 | str | None:
    if response.status_code == 200:
        response_200 = GetEventsServiceIdPossiblepersonsResponse200.from_dict(
            response.json()
        )

        return response_200

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
) -> Response[Any | GetEventsServiceIdPossiblepersonsResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetEventsServiceIdPossiblepersonsResponse200 | str]:
    """Get all possible persons for a service

     Gets a list of all possible persons for a service with their availability. This endpoint is used to
    get the persons for a service that is not part of an event.

    Args:
        service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetEventsServiceIdPossiblepersonsResponse200 | str]
    """

    kwargs = _get_kwargs(
        service_id=service_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetEventsServiceIdPossiblepersonsResponse200 | str | None:
    """Get all possible persons for a service

     Gets a list of all possible persons for a service with their availability. This endpoint is used to
    get the persons for a service that is not part of an event.

    Args:
        service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetEventsServiceIdPossiblepersonsResponse200 | str
    """

    return sync_detailed(
        service_id=service_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetEventsServiceIdPossiblepersonsResponse200 | str]:
    """Get all possible persons for a service

     Gets a list of all possible persons for a service with their availability. This endpoint is used to
    get the persons for a service that is not part of an event.

    Args:
        service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetEventsServiceIdPossiblepersonsResponse200 | str]
    """

    kwargs = _get_kwargs(
        service_id=service_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetEventsServiceIdPossiblepersonsResponse200 | str | None:
    """Get all possible persons for a service

     Gets a list of all possible persons for a service with their availability. This endpoint is used to
    get the persons for a service that is not part of an event.

    Args:
        service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetEventsServiceIdPossiblepersonsResponse200 | str
    """

    return (
        await asyncio_detailed(
            service_id=service_id,
            client=client,
        )
    ).parsed
