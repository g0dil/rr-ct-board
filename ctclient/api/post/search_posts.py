import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_posts_group_visibility import SearchPostsGroupVisibility
from ...models.search_posts_include_item import SearchPostsIncludeItem
from ...models.search_posts_order_by import SearchPostsOrderBy
from ...models.search_posts_order_direction import SearchPostsOrderDirection
from ...models.search_posts_post_visibility import SearchPostsPostVisibility
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str | Unset = UNSET,
    order_by: SearchPostsOrderBy | Unset = UNSET,
    order_direction: SearchPostsOrderDirection | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    actor_ids: list[int] | Unset = UNSET,
    group_visibility: SearchPostsGroupVisibility | Unset = UNSET,
    post_visibility: SearchPostsPostVisibility | Unset = UNSET,
    group_ids: list[int] | Unset = UNSET,
    include: list[SearchPostsIncludeItem] | Unset = UNSET,
    only_my_groups: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["query"] = query

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    json_order_direction: str | Unset = UNSET
    if not isinstance(order_direction, Unset):
        json_order_direction = order_direction.value

    params["order_direction"] = json_order_direction

    json_before: str | Unset = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat()
    params["before"] = json_before

    json_after: str | Unset = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat()
    params["after"] = json_after

    json_campus_ids: list[int] | Unset = UNSET
    if not isinstance(campus_ids, Unset):
        json_campus_ids = campus_ids

    params["campus_ids[]"] = json_campus_ids

    json_actor_ids: list[int] | Unset = UNSET
    if not isinstance(actor_ids, Unset):
        json_actor_ids = actor_ids

    params["actor_ids[]"] = json_actor_ids

    json_group_visibility: str | Unset = UNSET
    if not isinstance(group_visibility, Unset):
        json_group_visibility = group_visibility.value

    params["group_visibility"] = json_group_visibility

    json_post_visibility: str | Unset = UNSET
    if not isinstance(post_visibility, Unset):
        json_post_visibility = post_visibility.value

    params["post_visibility"] = json_post_visibility

    json_group_ids: list[int] | Unset = UNSET
    if not isinstance(group_ids, Unset):
        json_group_ids = group_ids

    params["group_ids[]"] = json_group_ids

    json_include: list[str] | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = []
        for include_item_data in include:
            include_item = include_item_data.value
            json_include.append(include_item)

    params["include"] = json_include

    params["only_my_groups"] = only_my_groups

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/post/search",
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
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    order_by: SearchPostsOrderBy | Unset = UNSET,
    order_direction: SearchPostsOrderDirection | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    actor_ids: list[int] | Unset = UNSET,
    group_visibility: SearchPostsGroupVisibility | Unset = UNSET,
    post_visibility: SearchPostsPostVisibility | Unset = UNSET,
    group_ids: list[int] | Unset = UNSET,
    include: list[SearchPostsIncludeItem] | Unset = UNSET,
    only_my_groups: bool | Unset = UNSET,
) -> Response[Any | str]:
    """Search posts

    Args:
        query (str | Unset):
        order_by (SearchPostsOrderBy | Unset):
        order_direction (SearchPostsOrderDirection | Unset):
        before (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        after (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        campus_ids (list[int] | Unset):
        actor_ids (list[int] | Unset):
        group_visibility (SearchPostsGroupVisibility | Unset):
        post_visibility (SearchPostsPostVisibility | Unset):
        group_ids (list[int] | Unset):
        include (list[SearchPostsIncludeItem] | Unset):
        only_my_groups (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        query=query,
        order_by=order_by,
        order_direction=order_direction,
        before=before,
        after=after,
        campus_ids=campus_ids,
        actor_ids=actor_ids,
        group_visibility=group_visibility,
        post_visibility=post_visibility,
        group_ids=group_ids,
        include=include,
        only_my_groups=only_my_groups,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    order_by: SearchPostsOrderBy | Unset = UNSET,
    order_direction: SearchPostsOrderDirection | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    actor_ids: list[int] | Unset = UNSET,
    group_visibility: SearchPostsGroupVisibility | Unset = UNSET,
    post_visibility: SearchPostsPostVisibility | Unset = UNSET,
    group_ids: list[int] | Unset = UNSET,
    include: list[SearchPostsIncludeItem] | Unset = UNSET,
    only_my_groups: bool | Unset = UNSET,
) -> Any | str | None:
    """Search posts

    Args:
        query (str | Unset):
        order_by (SearchPostsOrderBy | Unset):
        order_direction (SearchPostsOrderDirection | Unset):
        before (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        after (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        campus_ids (list[int] | Unset):
        actor_ids (list[int] | Unset):
        group_visibility (SearchPostsGroupVisibility | Unset):
        post_visibility (SearchPostsPostVisibility | Unset):
        group_ids (list[int] | Unset):
        include (list[SearchPostsIncludeItem] | Unset):
        only_my_groups (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        client=client,
        query=query,
        order_by=order_by,
        order_direction=order_direction,
        before=before,
        after=after,
        campus_ids=campus_ids,
        actor_ids=actor_ids,
        group_visibility=group_visibility,
        post_visibility=post_visibility,
        group_ids=group_ids,
        include=include,
        only_my_groups=only_my_groups,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    order_by: SearchPostsOrderBy | Unset = UNSET,
    order_direction: SearchPostsOrderDirection | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    actor_ids: list[int] | Unset = UNSET,
    group_visibility: SearchPostsGroupVisibility | Unset = UNSET,
    post_visibility: SearchPostsPostVisibility | Unset = UNSET,
    group_ids: list[int] | Unset = UNSET,
    include: list[SearchPostsIncludeItem] | Unset = UNSET,
    only_my_groups: bool | Unset = UNSET,
) -> Response[Any | str]:
    """Search posts

    Args:
        query (str | Unset):
        order_by (SearchPostsOrderBy | Unset):
        order_direction (SearchPostsOrderDirection | Unset):
        before (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        after (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        campus_ids (list[int] | Unset):
        actor_ids (list[int] | Unset):
        group_visibility (SearchPostsGroupVisibility | Unset):
        post_visibility (SearchPostsPostVisibility | Unset):
        group_ids (list[int] | Unset):
        include (list[SearchPostsIncludeItem] | Unset):
        only_my_groups (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        query=query,
        order_by=order_by,
        order_direction=order_direction,
        before=before,
        after=after,
        campus_ids=campus_ids,
        actor_ids=actor_ids,
        group_visibility=group_visibility,
        post_visibility=post_visibility,
        group_ids=group_ids,
        include=include,
        only_my_groups=only_my_groups,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    order_by: SearchPostsOrderBy | Unset = UNSET,
    order_direction: SearchPostsOrderDirection | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    actor_ids: list[int] | Unset = UNSET,
    group_visibility: SearchPostsGroupVisibility | Unset = UNSET,
    post_visibility: SearchPostsPostVisibility | Unset = UNSET,
    group_ids: list[int] | Unset = UNSET,
    include: list[SearchPostsIncludeItem] | Unset = UNSET,
    only_my_groups: bool | Unset = UNSET,
) -> Any | str | None:
    """Search posts

    Args:
        query (str | Unset):
        order_by (SearchPostsOrderBy | Unset):
        order_direction (SearchPostsOrderDirection | Unset):
        before (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        after (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        campus_ids (list[int] | Unset):
        actor_ids (list[int] | Unset):
        group_visibility (SearchPostsGroupVisibility | Unset):
        post_visibility (SearchPostsPostVisibility | Unset):
        group_ids (list[int] | Unset):
        include (list[SearchPostsIncludeItem] | Unset):
        only_my_groups (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            order_by=order_by,
            order_direction=order_direction,
            before=before,
            after=after,
            campus_ids=campus_ids,
            actor_ids=actor_ids,
            group_visibility=group_visibility,
            post_visibility=post_visibility,
            group_ids=group_ids,
            include=include,
            only_my_groups=only_my_groups,
        )
    ).parsed
