from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_markdown_check_body import PostMarkdownCheckBody
from ...models.post_markdown_check_response_200 import PostMarkdownCheckResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostMarkdownCheckBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/markdown/check",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostMarkdownCheckResponse200 | None:
    if response.status_code == 200:
        response_200 = PostMarkdownCheckResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostMarkdownCheckResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostMarkdownCheckBody,
) -> Response[PostMarkdownCheckResponse200]:
    """Validate Markdown string

     Check if the provided Markdown content is valid for the specified scope

    Args:
        body (PostMarkdownCheckBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostMarkdownCheckResponse200]
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
    body: PostMarkdownCheckBody,
) -> PostMarkdownCheckResponse200 | None:
    """Validate Markdown string

     Check if the provided Markdown content is valid for the specified scope

    Args:
        body (PostMarkdownCheckBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostMarkdownCheckResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostMarkdownCheckBody,
) -> Response[PostMarkdownCheckResponse200]:
    """Validate Markdown string

     Check if the provided Markdown content is valid for the specified scope

    Args:
        body (PostMarkdownCheckBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostMarkdownCheckResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostMarkdownCheckBody,
) -> PostMarkdownCheckResponse200 | None:
    """Validate Markdown string

     Check if the provided Markdown content is valid for the specified scope

    Args:
        body (PostMarkdownCheckBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostMarkdownCheckResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
