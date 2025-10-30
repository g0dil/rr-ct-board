from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_events_body import DeleteEventsBody
from ...types import Response


def _get_kwargs(
    event_id: int,
    *,
    body: DeleteEventsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/events/{event_id}".format(
            event_id=event_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    *,
    client: AuthenticatedClient | Client,
    body: DeleteEventsBody,
) -> Response[Any | str]:
    """Delete a single event

     Delete an event

    Args:
        event_id (int):  Example: 42.
        body (DeleteEventsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: DeleteEventsBody,
) -> Any | str | None:
    """Delete a single event

     Delete an event

    Args:
        event_id (int):  Example: 42.
        body (DeleteEventsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        event_id=event_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    event_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: DeleteEventsBody,
) -> Response[Any | str]:
    """Delete a single event

     Delete an event

    Args:
        event_id (int):  Example: 42.
        body (DeleteEventsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: DeleteEventsBody,
) -> Any | str | None:
    """Delete a single event

     Delete an event

    Args:
        event_id (int):  Example: 42.
        body (DeleteEventsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
            body=body,
        )
    ).parsed
