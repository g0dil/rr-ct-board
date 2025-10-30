from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_whoami_response_200 import GetWhoamiResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    only_allow_authenticated: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["only_allow_authenticated"] = only_allow_authenticated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/whoami",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetWhoamiResponse200 | None:
    if response.status_code == 200:
        response_200 = GetWhoamiResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetWhoamiResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    only_allow_authenticated: bool | Unset = UNSET,
) -> Response[Any | GetWhoamiResponse200]:
    """Currently logged in user.

     This endpoint returns the current user. If the request is unauthorized, the anonymous user (aka
    public user) is returned.

    Args:
        only_allow_authenticated (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetWhoamiResponse200]
    """

    kwargs = _get_kwargs(
        only_allow_authenticated=only_allow_authenticated,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    only_allow_authenticated: bool | Unset = UNSET,
) -> Any | GetWhoamiResponse200 | None:
    """Currently logged in user.

     This endpoint returns the current user. If the request is unauthorized, the anonymous user (aka
    public user) is returned.

    Args:
        only_allow_authenticated (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetWhoamiResponse200
    """

    return sync_detailed(
        client=client,
        only_allow_authenticated=only_allow_authenticated,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    only_allow_authenticated: bool | Unset = UNSET,
) -> Response[Any | GetWhoamiResponse200]:
    """Currently logged in user.

     This endpoint returns the current user. If the request is unauthorized, the anonymous user (aka
    public user) is returned.

    Args:
        only_allow_authenticated (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetWhoamiResponse200]
    """

    kwargs = _get_kwargs(
        only_allow_authenticated=only_allow_authenticated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    only_allow_authenticated: bool | Unset = UNSET,
) -> Any | GetWhoamiResponse200 | None:
    """Currently logged in user.

     This endpoint returns the current user. If the request is unauthorized, the anonymous user (aka
    public user) is returned.

    Args:
        only_allow_authenticated (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetWhoamiResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            only_allow_authenticated=only_allow_authenticated,
        )
    ).parsed
