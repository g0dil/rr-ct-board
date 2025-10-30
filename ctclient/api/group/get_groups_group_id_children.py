from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_groups_group_id_children_visibility import (
    GetGroupsGroupIdChildrenVisibility,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    limit: int | Unset = 10,
    page: int | Unset = 1,
    ids: list[int] | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    agegroup_ids: list[int] | Unset = UNSET,
    group_status_ids: list[int] | Unset = UNSET,
    group_category_ids: list[int] | Unset = UNSET,
    target_group_ids: list[int] | Unset = UNSET,
    weekdays: list[int] | Unset = UNSET,
    group_type_ids: list[int] | Unset = UNSET,
    tag_ids: list[int] | Unset = UNSET,
    is_open_for_members: bool | Unset = UNSET,
    without_my_groups: bool | Unset = UNSET,
    only_my_groups: bool | Unset = UNSET,
    has_meeting_place: bool | Unset = UNSET,
    allow_posts: bool | Unset = UNSET,
    has_posts: bool | Unset = UNSET,
    query: str | Unset = UNSET,
    visibility: GetGroupsGroupIdChildrenVisibility
    | Unset = GetGroupsGroupIdChildrenVisibility.RESTRICTED,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["page"] = page

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_campus_ids: list[int] | Unset = UNSET
    if not isinstance(campus_ids, Unset):
        json_campus_ids = campus_ids

    params["campus_ids[]"] = json_campus_ids

    json_agegroup_ids: list[int] | Unset = UNSET
    if not isinstance(agegroup_ids, Unset):
        json_agegroup_ids = agegroup_ids

    params["agegroup_ids[]"] = json_agegroup_ids

    json_group_status_ids: list[int] | Unset = UNSET
    if not isinstance(group_status_ids, Unset):
        json_group_status_ids = group_status_ids

    params["group_status_ids[]"] = json_group_status_ids

    json_group_category_ids: list[int] | Unset = UNSET
    if not isinstance(group_category_ids, Unset):
        json_group_category_ids = group_category_ids

    params["group_category_ids[]"] = json_group_category_ids

    json_target_group_ids: list[int] | Unset = UNSET
    if not isinstance(target_group_ids, Unset):
        json_target_group_ids = target_group_ids

    params["target_group_ids[]"] = json_target_group_ids

    json_weekdays: list[int] | Unset = UNSET
    if not isinstance(weekdays, Unset):
        json_weekdays = weekdays

    params["weekdays[]"] = json_weekdays

    json_group_type_ids: list[int] | Unset = UNSET
    if not isinstance(group_type_ids, Unset):
        json_group_type_ids = group_type_ids

    params["group_type_ids[]"] = json_group_type_ids

    json_tag_ids: list[int] | Unset = UNSET
    if not isinstance(tag_ids, Unset):
        json_tag_ids = tag_ids

    params["tag_ids[]"] = json_tag_ids

    params["is_open_for_members"] = is_open_for_members

    params["without_my_groups"] = without_my_groups

    params["only_my_groups"] = only_my_groups

    params["has_meeting_place"] = has_meeting_place

    params["allow_posts"] = allow_posts

    params["has_posts"] = has_posts

    params["query"] = query

    json_visibility: str | Unset = UNSET
    if not isinstance(visibility, Unset):
        json_visibility = visibility.value

    params["visibility"] = json_visibility

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/groups/{group_id}/children".format(
            group_id=group_id,
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
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    page: int | Unset = 1,
    ids: list[int] | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    agegroup_ids: list[int] | Unset = UNSET,
    group_status_ids: list[int] | Unset = UNSET,
    group_category_ids: list[int] | Unset = UNSET,
    target_group_ids: list[int] | Unset = UNSET,
    weekdays: list[int] | Unset = UNSET,
    group_type_ids: list[int] | Unset = UNSET,
    tag_ids: list[int] | Unset = UNSET,
    is_open_for_members: bool | Unset = UNSET,
    without_my_groups: bool | Unset = UNSET,
    only_my_groups: bool | Unset = UNSET,
    has_meeting_place: bool | Unset = UNSET,
    allow_posts: bool | Unset = UNSET,
    has_posts: bool | Unset = UNSET,
    query: str | Unset = UNSET,
    visibility: GetGroupsGroupIdChildrenVisibility
    | Unset = GetGroupsGroupIdChildrenVisibility.RESTRICTED,
) -> Response[Any | str]:
    """Get child groups

    Args:
        group_id (int):  Example: 42.
        limit (int | Unset):  Default: 10. Example: 10.
        page (int | Unset):  Default: 1. Example: 1.
        ids (list[int] | Unset):
        campus_ids (list[int] | Unset):
        agegroup_ids (list[int] | Unset):
        group_status_ids (list[int] | Unset):
        group_category_ids (list[int] | Unset):
        target_group_ids (list[int] | Unset):
        weekdays (list[int] | Unset):
        group_type_ids (list[int] | Unset):
        tag_ids (list[int] | Unset):
        is_open_for_members (bool | Unset):  Example: True.
        without_my_groups (bool | Unset):
        only_my_groups (bool | Unset):
        has_meeting_place (bool | Unset):  Example: True.
        allow_posts (bool | Unset):  Example: True.
        has_posts (bool | Unset):  Example: True.
        query (str | Unset):
        visibility (GetGroupsGroupIdChildrenVisibility | Unset):  Default:
            GetGroupsGroupIdChildrenVisibility.RESTRICTED. Example: restricted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        limit=limit,
        page=page,
        ids=ids,
        campus_ids=campus_ids,
        agegroup_ids=agegroup_ids,
        group_status_ids=group_status_ids,
        group_category_ids=group_category_ids,
        target_group_ids=target_group_ids,
        weekdays=weekdays,
        group_type_ids=group_type_ids,
        tag_ids=tag_ids,
        is_open_for_members=is_open_for_members,
        without_my_groups=without_my_groups,
        only_my_groups=only_my_groups,
        has_meeting_place=has_meeting_place,
        allow_posts=allow_posts,
        has_posts=has_posts,
        query=query,
        visibility=visibility,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    page: int | Unset = 1,
    ids: list[int] | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    agegroup_ids: list[int] | Unset = UNSET,
    group_status_ids: list[int] | Unset = UNSET,
    group_category_ids: list[int] | Unset = UNSET,
    target_group_ids: list[int] | Unset = UNSET,
    weekdays: list[int] | Unset = UNSET,
    group_type_ids: list[int] | Unset = UNSET,
    tag_ids: list[int] | Unset = UNSET,
    is_open_for_members: bool | Unset = UNSET,
    without_my_groups: bool | Unset = UNSET,
    only_my_groups: bool | Unset = UNSET,
    has_meeting_place: bool | Unset = UNSET,
    allow_posts: bool | Unset = UNSET,
    has_posts: bool | Unset = UNSET,
    query: str | Unset = UNSET,
    visibility: GetGroupsGroupIdChildrenVisibility
    | Unset = GetGroupsGroupIdChildrenVisibility.RESTRICTED,
) -> Any | str | None:
    """Get child groups

    Args:
        group_id (int):  Example: 42.
        limit (int | Unset):  Default: 10. Example: 10.
        page (int | Unset):  Default: 1. Example: 1.
        ids (list[int] | Unset):
        campus_ids (list[int] | Unset):
        agegroup_ids (list[int] | Unset):
        group_status_ids (list[int] | Unset):
        group_category_ids (list[int] | Unset):
        target_group_ids (list[int] | Unset):
        weekdays (list[int] | Unset):
        group_type_ids (list[int] | Unset):
        tag_ids (list[int] | Unset):
        is_open_for_members (bool | Unset):  Example: True.
        without_my_groups (bool | Unset):
        only_my_groups (bool | Unset):
        has_meeting_place (bool | Unset):  Example: True.
        allow_posts (bool | Unset):  Example: True.
        has_posts (bool | Unset):  Example: True.
        query (str | Unset):
        visibility (GetGroupsGroupIdChildrenVisibility | Unset):  Default:
            GetGroupsGroupIdChildrenVisibility.RESTRICTED. Example: restricted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        limit=limit,
        page=page,
        ids=ids,
        campus_ids=campus_ids,
        agegroup_ids=agegroup_ids,
        group_status_ids=group_status_ids,
        group_category_ids=group_category_ids,
        target_group_ids=target_group_ids,
        weekdays=weekdays,
        group_type_ids=group_type_ids,
        tag_ids=tag_ids,
        is_open_for_members=is_open_for_members,
        without_my_groups=without_my_groups,
        only_my_groups=only_my_groups,
        has_meeting_place=has_meeting_place,
        allow_posts=allow_posts,
        has_posts=has_posts,
        query=query,
        visibility=visibility,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    page: int | Unset = 1,
    ids: list[int] | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    agegroup_ids: list[int] | Unset = UNSET,
    group_status_ids: list[int] | Unset = UNSET,
    group_category_ids: list[int] | Unset = UNSET,
    target_group_ids: list[int] | Unset = UNSET,
    weekdays: list[int] | Unset = UNSET,
    group_type_ids: list[int] | Unset = UNSET,
    tag_ids: list[int] | Unset = UNSET,
    is_open_for_members: bool | Unset = UNSET,
    without_my_groups: bool | Unset = UNSET,
    only_my_groups: bool | Unset = UNSET,
    has_meeting_place: bool | Unset = UNSET,
    allow_posts: bool | Unset = UNSET,
    has_posts: bool | Unset = UNSET,
    query: str | Unset = UNSET,
    visibility: GetGroupsGroupIdChildrenVisibility
    | Unset = GetGroupsGroupIdChildrenVisibility.RESTRICTED,
) -> Response[Any | str]:
    """Get child groups

    Args:
        group_id (int):  Example: 42.
        limit (int | Unset):  Default: 10. Example: 10.
        page (int | Unset):  Default: 1. Example: 1.
        ids (list[int] | Unset):
        campus_ids (list[int] | Unset):
        agegroup_ids (list[int] | Unset):
        group_status_ids (list[int] | Unset):
        group_category_ids (list[int] | Unset):
        target_group_ids (list[int] | Unset):
        weekdays (list[int] | Unset):
        group_type_ids (list[int] | Unset):
        tag_ids (list[int] | Unset):
        is_open_for_members (bool | Unset):  Example: True.
        without_my_groups (bool | Unset):
        only_my_groups (bool | Unset):
        has_meeting_place (bool | Unset):  Example: True.
        allow_posts (bool | Unset):  Example: True.
        has_posts (bool | Unset):  Example: True.
        query (str | Unset):
        visibility (GetGroupsGroupIdChildrenVisibility | Unset):  Default:
            GetGroupsGroupIdChildrenVisibility.RESTRICTED. Example: restricted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        limit=limit,
        page=page,
        ids=ids,
        campus_ids=campus_ids,
        agegroup_ids=agegroup_ids,
        group_status_ids=group_status_ids,
        group_category_ids=group_category_ids,
        target_group_ids=target_group_ids,
        weekdays=weekdays,
        group_type_ids=group_type_ids,
        tag_ids=tag_ids,
        is_open_for_members=is_open_for_members,
        without_my_groups=without_my_groups,
        only_my_groups=only_my_groups,
        has_meeting_place=has_meeting_place,
        allow_posts=allow_posts,
        has_posts=has_posts,
        query=query,
        visibility=visibility,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    page: int | Unset = 1,
    ids: list[int] | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    agegroup_ids: list[int] | Unset = UNSET,
    group_status_ids: list[int] | Unset = UNSET,
    group_category_ids: list[int] | Unset = UNSET,
    target_group_ids: list[int] | Unset = UNSET,
    weekdays: list[int] | Unset = UNSET,
    group_type_ids: list[int] | Unset = UNSET,
    tag_ids: list[int] | Unset = UNSET,
    is_open_for_members: bool | Unset = UNSET,
    without_my_groups: bool | Unset = UNSET,
    only_my_groups: bool | Unset = UNSET,
    has_meeting_place: bool | Unset = UNSET,
    allow_posts: bool | Unset = UNSET,
    has_posts: bool | Unset = UNSET,
    query: str | Unset = UNSET,
    visibility: GetGroupsGroupIdChildrenVisibility
    | Unset = GetGroupsGroupIdChildrenVisibility.RESTRICTED,
) -> Any | str | None:
    """Get child groups

    Args:
        group_id (int):  Example: 42.
        limit (int | Unset):  Default: 10. Example: 10.
        page (int | Unset):  Default: 1. Example: 1.
        ids (list[int] | Unset):
        campus_ids (list[int] | Unset):
        agegroup_ids (list[int] | Unset):
        group_status_ids (list[int] | Unset):
        group_category_ids (list[int] | Unset):
        target_group_ids (list[int] | Unset):
        weekdays (list[int] | Unset):
        group_type_ids (list[int] | Unset):
        tag_ids (list[int] | Unset):
        is_open_for_members (bool | Unset):  Example: True.
        without_my_groups (bool | Unset):
        only_my_groups (bool | Unset):
        has_meeting_place (bool | Unset):  Example: True.
        allow_posts (bool | Unset):  Example: True.
        has_posts (bool | Unset):  Example: True.
        query (str | Unset):
        visibility (GetGroupsGroupIdChildrenVisibility | Unset):  Default:
            GetGroupsGroupIdChildrenVisibility.RESTRICTED. Example: restricted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            limit=limit,
            page=page,
            ids=ids,
            campus_ids=campus_ids,
            agegroup_ids=agegroup_ids,
            group_status_ids=group_status_ids,
            group_category_ids=group_category_ids,
            target_group_ids=target_group_ids,
            weekdays=weekdays,
            group_type_ids=group_type_ids,
            tag_ids=tag_ids,
            is_open_for_members=is_open_for_members,
            without_my_groups=without_my_groups,
            only_my_groups=only_my_groups,
            has_meeting_place=has_meeting_place,
            allow_posts=allow_posts,
            has_posts=has_posts,
            query=query,
            visibility=visibility,
        )
    ).parsed
