from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_groups_group_id_followups_filter_item import (
    GetGroupsGroupIdFollowupsFilterItem,
)
from ...models.get_groups_group_id_followups_response_200 import (
    GetGroupsGroupIdFollowupsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    filter_: list[GetGroupsGroupIdFollowupsFilterItem] | Unset = UNSET,
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
        "url": "/groups/{group_id}/followups".format(
            group_id=group_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetGroupsGroupIdFollowupsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetGroupsGroupIdFollowupsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetGroupsGroupIdFollowupsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    filter_: list[GetGroupsGroupIdFollowupsFilterItem] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> Response[Any | GetGroupsGroupIdFollowupsResponse200]:
    """Get follow-ups for group

     Get all follow-ups for the specified group

    Args:
        group_id (int):  Example: 42.
        filter_ (list[GetGroupsGroupIdFollowupsFilterItem] | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetGroupsGroupIdFollowupsResponse200]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        filter_=filter_,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    filter_: list[GetGroupsGroupIdFollowupsFilterItem] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> Any | GetGroupsGroupIdFollowupsResponse200 | None:
    """Get follow-ups for group

     Get all follow-ups for the specified group

    Args:
        group_id (int):  Example: 42.
        filter_ (list[GetGroupsGroupIdFollowupsFilterItem] | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetGroupsGroupIdFollowupsResponse200
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        filter_=filter_,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    filter_: list[GetGroupsGroupIdFollowupsFilterItem] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> Response[Any | GetGroupsGroupIdFollowupsResponse200]:
    """Get follow-ups for group

     Get all follow-ups for the specified group

    Args:
        group_id (int):  Example: 42.
        filter_ (list[GetGroupsGroupIdFollowupsFilterItem] | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetGroupsGroupIdFollowupsResponse200]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        filter_=filter_,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    filter_: list[GetGroupsGroupIdFollowupsFilterItem] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> Any | GetGroupsGroupIdFollowupsResponse200 | None:
    """Get follow-ups for group

     Get all follow-ups for the specified group

    Args:
        group_id (int):  Example: 42.
        filter_ (list[GetGroupsGroupIdFollowupsFilterItem] | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetGroupsGroupIdFollowupsResponse200
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            filter_=filter_,
            page=page,
            limit=limit,
        )
    ).parsed
