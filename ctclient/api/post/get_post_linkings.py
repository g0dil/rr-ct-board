from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_post_linkings_response_200 import GetPostLinkingsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    post_ids: list[int] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_post_ids: list[int] | Unset = UNSET
    if not isinstance(post_ids, Unset):
        json_post_ids = post_ids

    params["post_ids[]"] = json_post_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/post/linkings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetPostLinkingsResponse200 | str | None:
    if response.status_code == 200:
        response_200 = GetPostLinkingsResponse200.from_dict(response.json())

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
) -> Response[Any | GetPostLinkingsResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    post_ids: list[int] | Unset = UNSET,
) -> Response[Any | GetPostLinkingsResponse200 | str]:
    """
    Args:
        post_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPostLinkingsResponse200 | str]
    """

    kwargs = _get_kwargs(
        post_ids=post_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    post_ids: list[int] | Unset = UNSET,
) -> Any | GetPostLinkingsResponse200 | str | None:
    """
    Args:
        post_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPostLinkingsResponse200 | str
    """

    return sync_detailed(
        client=client,
        post_ids=post_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    post_ids: list[int] | Unset = UNSET,
) -> Response[Any | GetPostLinkingsResponse200 | str]:
    """
    Args:
        post_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPostLinkingsResponse200 | str]
    """

    kwargs = _get_kwargs(
        post_ids=post_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    post_ids: list[int] | Unset = UNSET,
) -> Any | GetPostLinkingsResponse200 | str | None:
    """
    Args:
        post_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPostLinkingsResponse200 | str
    """

    return (
        await asyncio_detailed(
            client=client,
            post_ids=post_ids,
        )
    ).parsed
