from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_chat_body import UpdateChatBody
from ...models.update_chat_response_200 import UpdateChatResponse200
from ...types import Response


def _get_kwargs(
    guid: str,
    *,
    body: UpdateChatBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/chat/{guid}".format(
            guid=guid,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | UpdateChatResponse200 | str | None:
    if response.status_code == 200:
        response_200 = UpdateChatResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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
) -> Response[Any | UpdateChatResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    guid: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateChatBody,
) -> Response[Any | UpdateChatResponse200 | str]:
    """Update a chat

    Args:
        guid (str):  Example: 681F54E3-2EB7-40A4-84F0-EFF8E8F05727.
        body (UpdateChatBody):  Example: {'creator': 1, 'domainId': 9, 'prefix': 'ctg',
            'roomname': 'Technik', 'status': 'STARTED'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UpdateChatResponse200 | str]
    """

    kwargs = _get_kwargs(
        guid=guid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    guid: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateChatBody,
) -> Any | UpdateChatResponse200 | str | None:
    """Update a chat

    Args:
        guid (str):  Example: 681F54E3-2EB7-40A4-84F0-EFF8E8F05727.
        body (UpdateChatBody):  Example: {'creator': 1, 'domainId': 9, 'prefix': 'ctg',
            'roomname': 'Technik', 'status': 'STARTED'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UpdateChatResponse200 | str
    """

    return sync_detailed(
        guid=guid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    guid: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateChatBody,
) -> Response[Any | UpdateChatResponse200 | str]:
    """Update a chat

    Args:
        guid (str):  Example: 681F54E3-2EB7-40A4-84F0-EFF8E8F05727.
        body (UpdateChatBody):  Example: {'creator': 1, 'domainId': 9, 'prefix': 'ctg',
            'roomname': 'Technik', 'status': 'STARTED'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UpdateChatResponse200 | str]
    """

    kwargs = _get_kwargs(
        guid=guid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    guid: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateChatBody,
) -> Any | UpdateChatResponse200 | str | None:
    """Update a chat

    Args:
        guid (str):  Example: 681F54E3-2EB7-40A4-84F0-EFF8E8F05727.
        body (UpdateChatBody):  Example: {'creator': 1, 'domainId': 9, 'prefix': 'ctg',
            'roomname': 'Technik', 'status': 'STARTED'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UpdateChatResponse200 | str
    """

    return (
        await asyncio_detailed(
            guid=guid,
            client=client,
            body=body,
        )
    ).parsed
