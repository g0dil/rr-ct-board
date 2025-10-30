import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_posts_group_visibility import GetPostsGroupVisibility
from ...models.get_posts_include_item import GetPostsIncludeItem
from ...models.get_posts_post_visibility import GetPostsPostVisibility
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    before: datetime.datetime | Unset = UNSET,
    last_post_indentifier: str | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    campus_id: int | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    actor_ids: list[int] | Unset = UNSET,
    group_visibility: GetPostsGroupVisibility | Unset = UNSET,
    post_visibility: GetPostsPostVisibility | Unset = UNSET,
    group_ids: list[int] | Unset = UNSET,
    include: list[GetPostsIncludeItem] | Unset = UNSET,
    limit: int | Unset = 10,
    only_my_groups: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_before: str | Unset = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat()
    params["before"] = json_before

    params["last_post_indentifier"] = last_post_indentifier

    json_after: str | Unset = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat()
    params["after"] = json_after

    params["campus_id"] = campus_id

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

    params["include[]"] = json_include

    params["limit"] = limit

    params["only_my_groups"] = only_my_groups

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/posts",
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
    before: datetime.datetime | Unset = UNSET,
    last_post_indentifier: str | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    campus_id: int | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    actor_ids: list[int] | Unset = UNSET,
    group_visibility: GetPostsGroupVisibility | Unset = UNSET,
    post_visibility: GetPostsPostVisibility | Unset = UNSET,
    group_ids: list[int] | Unset = UNSET,
    include: list[GetPostsIncludeItem] | Unset = UNSET,
    limit: int | Unset = 10,
    only_my_groups: bool | Unset = UNSET,
) -> Response[Any | str]:
    """Get a list of posts. The posts are sorted by the `createdDate` field descending.

    Args:
        before (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        last_post_indentifier (str | Unset):
        after (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        campus_id (int | Unset):
        campus_ids (list[int] | Unset):
        actor_ids (list[int] | Unset):
        group_visibility (GetPostsGroupVisibility | Unset):
        post_visibility (GetPostsPostVisibility | Unset):
        group_ids (list[int] | Unset):
        include (list[GetPostsIncludeItem] | Unset):
        limit (int | Unset):  Default: 10. Example: 10.
        only_my_groups (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        before=before,
        last_post_indentifier=last_post_indentifier,
        after=after,
        campus_id=campus_id,
        campus_ids=campus_ids,
        actor_ids=actor_ids,
        group_visibility=group_visibility,
        post_visibility=post_visibility,
        group_ids=group_ids,
        include=include,
        limit=limit,
        only_my_groups=only_my_groups,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    before: datetime.datetime | Unset = UNSET,
    last_post_indentifier: str | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    campus_id: int | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    actor_ids: list[int] | Unset = UNSET,
    group_visibility: GetPostsGroupVisibility | Unset = UNSET,
    post_visibility: GetPostsPostVisibility | Unset = UNSET,
    group_ids: list[int] | Unset = UNSET,
    include: list[GetPostsIncludeItem] | Unset = UNSET,
    limit: int | Unset = 10,
    only_my_groups: bool | Unset = UNSET,
) -> Any | str | None:
    """Get a list of posts. The posts are sorted by the `createdDate` field descending.

    Args:
        before (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        last_post_indentifier (str | Unset):
        after (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        campus_id (int | Unset):
        campus_ids (list[int] | Unset):
        actor_ids (list[int] | Unset):
        group_visibility (GetPostsGroupVisibility | Unset):
        post_visibility (GetPostsPostVisibility | Unset):
        group_ids (list[int] | Unset):
        include (list[GetPostsIncludeItem] | Unset):
        limit (int | Unset):  Default: 10. Example: 10.
        only_my_groups (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        client=client,
        before=before,
        last_post_indentifier=last_post_indentifier,
        after=after,
        campus_id=campus_id,
        campus_ids=campus_ids,
        actor_ids=actor_ids,
        group_visibility=group_visibility,
        post_visibility=post_visibility,
        group_ids=group_ids,
        include=include,
        limit=limit,
        only_my_groups=only_my_groups,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    before: datetime.datetime | Unset = UNSET,
    last_post_indentifier: str | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    campus_id: int | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    actor_ids: list[int] | Unset = UNSET,
    group_visibility: GetPostsGroupVisibility | Unset = UNSET,
    post_visibility: GetPostsPostVisibility | Unset = UNSET,
    group_ids: list[int] | Unset = UNSET,
    include: list[GetPostsIncludeItem] | Unset = UNSET,
    limit: int | Unset = 10,
    only_my_groups: bool | Unset = UNSET,
) -> Response[Any | str]:
    """Get a list of posts. The posts are sorted by the `createdDate` field descending.

    Args:
        before (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        last_post_indentifier (str | Unset):
        after (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        campus_id (int | Unset):
        campus_ids (list[int] | Unset):
        actor_ids (list[int] | Unset):
        group_visibility (GetPostsGroupVisibility | Unset):
        post_visibility (GetPostsPostVisibility | Unset):
        group_ids (list[int] | Unset):
        include (list[GetPostsIncludeItem] | Unset):
        limit (int | Unset):  Default: 10. Example: 10.
        only_my_groups (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        before=before,
        last_post_indentifier=last_post_indentifier,
        after=after,
        campus_id=campus_id,
        campus_ids=campus_ids,
        actor_ids=actor_ids,
        group_visibility=group_visibility,
        post_visibility=post_visibility,
        group_ids=group_ids,
        include=include,
        limit=limit,
        only_my_groups=only_my_groups,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    before: datetime.datetime | Unset = UNSET,
    last_post_indentifier: str | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    campus_id: int | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    actor_ids: list[int] | Unset = UNSET,
    group_visibility: GetPostsGroupVisibility | Unset = UNSET,
    post_visibility: GetPostsPostVisibility | Unset = UNSET,
    group_ids: list[int] | Unset = UNSET,
    include: list[GetPostsIncludeItem] | Unset = UNSET,
    limit: int | Unset = 10,
    only_my_groups: bool | Unset = UNSET,
) -> Any | str | None:
    """Get a list of posts. The posts are sorted by the `createdDate` field descending.

    Args:
        before (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        last_post_indentifier (str | Unset):
        after (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        campus_id (int | Unset):
        campus_ids (list[int] | Unset):
        actor_ids (list[int] | Unset):
        group_visibility (GetPostsGroupVisibility | Unset):
        post_visibility (GetPostsPostVisibility | Unset):
        group_ids (list[int] | Unset):
        include (list[GetPostsIncludeItem] | Unset):
        limit (int | Unset):  Default: 10. Example: 10.
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
            before=before,
            last_post_indentifier=last_post_indentifier,
            after=after,
            campus_id=campus_id,
            campus_ids=campus_ids,
            actor_ids=actor_ids,
            group_visibility=group_visibility,
            post_visibility=post_visibility,
            group_ids=group_ids,
            include=include,
            limit=limit,
            only_my_groups=only_my_groups,
        )
    ).parsed
