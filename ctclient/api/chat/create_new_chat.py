from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_new_chat_body import CreateNewChatBody
from ...models.create_new_chat_response_201 import CreateNewChatResponse201
from ...types import Response


def _get_kwargs(
    *,
    body: CreateNewChatBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chat",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateNewChatResponse201 | str | None:
    if response.status_code == 201:
        response_201 = CreateNewChatResponse201.from_dict(response.json())

        return response_201

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
) -> Response[Any | CreateNewChatResponse201 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateNewChatBody,
) -> Response[Any | CreateNewChatResponse201 | str]:
    """Start new chat

    Args:
        body (CreateNewChatBody):  Example: {'domainId': 9, 'guid':
            '681F54E3-2EB7-40A4-84F0-EFF8E8F05727', 'prefix': 'ctg', 'roomname': 'Technik'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateNewChatResponse201 | str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateNewChatBody,
) -> Any | CreateNewChatResponse201 | str | None:
    """Start new chat

    Args:
        body (CreateNewChatBody):  Example: {'domainId': 9, 'guid':
            '681F54E3-2EB7-40A4-84F0-EFF8E8F05727', 'prefix': 'ctg', 'roomname': 'Technik'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateNewChatResponse201 | str
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateNewChatBody,
) -> Response[Any | CreateNewChatResponse201 | str]:
    """Start new chat

    Args:
        body (CreateNewChatBody):  Example: {'domainId': 9, 'guid':
            '681F54E3-2EB7-40A4-84F0-EFF8E8F05727', 'prefix': 'ctg', 'roomname': 'Technik'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateNewChatResponse201 | str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateNewChatBody,
) -> Any | CreateNewChatResponse201 | str | None:
    """Start new chat

    Args:
        body (CreateNewChatBody):  Example: {'domainId': 9, 'guid':
            '681F54E3-2EB7-40A4-84F0-EFF8E8F05727', 'prefix': 'ctg', 'roomname': 'Technik'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateNewChatResponse201 | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
