from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_followups_filter_item import GetFollowupsFilterItem
from ...models.get_followups_response_200 import GetFollowupsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_: list[GetFollowupsFilterItem] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_filter_: list[str] | Unset = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = []
        for filter_item_data in filter_:
            filter_item = filter_item_data.value
            json_filter_.append(filter_item)

    params["filter"] = json_filter_

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/followups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetFollowupsResponse200 | str | None:
    if response.status_code == 200:
        response_200 = GetFollowupsResponse200.from_dict(response.json())

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
) -> Response[Any | GetFollowupsResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_: list[GetFollowupsFilterItem] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> Response[Any | GetFollowupsResponse200 | str]:
    """Get all followups

     Get all follow-ups that the current user is responsible for.

    Args:
        filter_ (list[GetFollowupsFilterItem] | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFollowupsResponse200 | str]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    filter_: list[GetFollowupsFilterItem] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> Any | GetFollowupsResponse200 | str | None:
    """Get all followups

     Get all follow-ups that the current user is responsible for.

    Args:
        filter_ (list[GetFollowupsFilterItem] | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFollowupsResponse200 | str
    """

    return sync_detailed(
        client=client,
        filter_=filter_,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_: list[GetFollowupsFilterItem] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> Response[Any | GetFollowupsResponse200 | str]:
    """Get all followups

     Get all follow-ups that the current user is responsible for.

    Args:
        filter_ (list[GetFollowupsFilterItem] | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFollowupsResponse200 | str]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    filter_: list[GetFollowupsFilterItem] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> Any | GetFollowupsResponse200 | str | None:
    """Get all followups

     Get all follow-ups that the current user is responsible for.

    Args:
        filter_ (list[GetFollowupsFilterItem] | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFollowupsResponse200 | str
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_=filter_,
            page=page,
            limit=limit,
        )
    ).parsed
