from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_posts_post_id_include_item import GetPostsPostIdIncludeItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    post_id: int,
    *,
    include: list[GetPostsPostIdIncludeItem] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include: list[str] | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = []
        for include_item_data in include:
            include_item = include_item_data.value
            json_include.append(include_item)

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/posts/{post_id}".format(
            post_id=post_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | str | None:
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
    post_id: int,
    *,
    client: AuthenticatedClient | Client,
    include: list[GetPostsPostIdIncludeItem] | Unset = UNSET,
) -> Response[Any | str]:
    """Get a post.

    Args:
        post_id (int):  Example: 42.
        include (list[GetPostsPostIdIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    post_id: int,
    *,
    client: AuthenticatedClient | Client,
    include: list[GetPostsPostIdIncludeItem] | Unset = UNSET,
) -> Any | str | None:
    """Get a post.

    Args:
        post_id (int):  Example: 42.
        include (list[GetPostsPostIdIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        post_id=post_id,
        client=client,
        include=include,
    ).parsed


async def asyncio_detailed(
    post_id: int,
    *,
    client: AuthenticatedClient | Client,
    include: list[GetPostsPostIdIncludeItem] | Unset = UNSET,
) -> Response[Any | str]:
    """Get a post.

    Args:
        post_id (int):  Example: 42.
        include (list[GetPostsPostIdIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    post_id: int,
    *,
    client: AuthenticatedClient | Client,
    include: list[GetPostsPostIdIncludeItem] | Unset = UNSET,
) -> Any | str | None:
    """Get a post.

    Args:
        post_id (int):  Example: 42.
        include (list[GetPostsPostIdIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            post_id=post_id,
            client=client,
            include=include,
        )
    ).parsed
