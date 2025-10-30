import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_group_members_group_member_statuses_item import (
    GetAllGroupMembersGroupMemberStatusesItem,
)
from ...models.get_all_group_members_include_item import GetAllGroupMembersIncludeItem
from ...models.get_all_group_members_order_directions_item import (
    GetAllGroupMembersOrderDirectionsItem,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    role_ids: list[int] | Unset = UNSET,
    person_id: list[int] | Unset = UNSET,
    group_member_statuses: list[GetAllGroupMembersGroupMemberStatusesItem]
    | Unset = UNSET,
    allowed_chat_users_only: bool | Unset = UNSET,
    allowed_chat_writers_only: bool | Unset = UNSET,
    query: str | Unset = UNSET,
    comment: str | Unset = UNSET,
    member_start_date_after: datetime.date | Unset = UNSET,
    member_start_date_before: datetime.date | Unset = UNSET,
    order_fields: list[str] | Unset = UNSET,
    order_directions: list[GetAllGroupMembersOrderDirectionsItem] | Unset = UNSET,
    person_fields: list[str] | Unset = UNSET,
    include: list[GetAllGroupMembersIncludeItem] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    json_role_ids: list[int] | Unset = UNSET
    if not isinstance(role_ids, Unset):
        json_role_ids = role_ids

    params["role_ids[]"] = json_role_ids

    json_person_id: list[int] | Unset = UNSET
    if not isinstance(person_id, Unset):
        json_person_id = person_id

    params["person_id[]"] = json_person_id

    json_group_member_statuses: list[str] | Unset = UNSET
    if not isinstance(group_member_statuses, Unset):
        json_group_member_statuses = []
        for group_member_statuses_item_data in group_member_statuses:
            group_member_statuses_item = group_member_statuses_item_data.value
            json_group_member_statuses.append(group_member_statuses_item)

    params["group_member_statuses[]"] = json_group_member_statuses

    params["allowed_chat_users_only"] = allowed_chat_users_only

    params["allowed_chat_writers_only"] = allowed_chat_writers_only

    params["query"] = query

    params["comment"] = comment

    json_member_start_date_after: str | Unset = UNSET
    if not isinstance(member_start_date_after, Unset):
        json_member_start_date_after = member_start_date_after.isoformat()
    params["member_start_date_after"] = json_member_start_date_after

    json_member_start_date_before: str | Unset = UNSET
    if not isinstance(member_start_date_before, Unset):
        json_member_start_date_before = member_start_date_before.isoformat()
    params["member_start_date_before"] = json_member_start_date_before

    json_order_fields: list[str] | Unset = UNSET
    if not isinstance(order_fields, Unset):
        json_order_fields = order_fields

    params["orderFields[]"] = json_order_fields

    json_order_directions: list[str] | Unset = UNSET
    if not isinstance(order_directions, Unset):
        json_order_directions = []
        for order_directions_item_data in order_directions:
            order_directions_item = order_directions_item_data.value
            json_order_directions.append(order_directions_item)

    params["orderDirections[]"] = json_order_directions

    json_person_fields: list[str] | Unset = UNSET
    if not isinstance(person_fields, Unset):
        json_person_fields = person_fields

    params["personFields[]"] = json_person_fields

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
        "url": "/groups/{group_id}/members".format(
            group_id=group_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
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
    page: int | Unset = 1,
    limit: int | Unset = 10,
    role_ids: list[int] | Unset = UNSET,
    person_id: list[int] | Unset = UNSET,
    group_member_statuses: list[GetAllGroupMembersGroupMemberStatusesItem]
    | Unset = UNSET,
    allowed_chat_users_only: bool | Unset = UNSET,
    allowed_chat_writers_only: bool | Unset = UNSET,
    query: str | Unset = UNSET,
    comment: str | Unset = UNSET,
    member_start_date_after: datetime.date | Unset = UNSET,
    member_start_date_before: datetime.date | Unset = UNSET,
    order_fields: list[str] | Unset = UNSET,
    order_directions: list[GetAllGroupMembersOrderDirectionsItem] | Unset = UNSET,
    person_fields: list[str] | Unset = UNSET,
    include: list[GetAllGroupMembersIncludeItem] | Unset = UNSET,
) -> Response[Any]:
    """Get all group members

     This endpoint returns an array with all group members of one group. In addition to the documented
    query parameters, members can be filtered by group member fields (`<fieldName>=fieldValue`) and/or
    person fields (`person_<fieldName>=fieldValue`) as query parameters.

    Args:
        group_id (int):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        role_ids (list[int] | Unset):
        person_id (list[int] | Unset):
        group_member_statuses (list[GetAllGroupMembersGroupMemberStatusesItem] | Unset):
        allowed_chat_users_only (bool | Unset):
        allowed_chat_writers_only (bool | Unset):
        query (str | Unset):  Example: Peter Maier.
        comment (str | Unset):  Example: Member.
        member_start_date_after (datetime.date | Unset): A simple date in ISO format, e.g.
            '2022-10-19' Example: 2022-10-19.
        member_start_date_before (datetime.date | Unset): A simple date in ISO format, e.g.
            '2022-10-19' Example: 2022-10-19.
        order_fields (list[str] | Unset):
        order_directions (list[GetAllGroupMembersOrderDirectionsItem] | Unset):
        person_fields (list[str] | Unset):
        include (list[GetAllGroupMembersIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        page=page,
        limit=limit,
        role_ids=role_ids,
        person_id=person_id,
        group_member_statuses=group_member_statuses,
        allowed_chat_users_only=allowed_chat_users_only,
        allowed_chat_writers_only=allowed_chat_writers_only,
        query=query,
        comment=comment,
        member_start_date_after=member_start_date_after,
        member_start_date_before=member_start_date_before,
        order_fields=order_fields,
        order_directions=order_directions,
        person_fields=person_fields,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    role_ids: list[int] | Unset = UNSET,
    person_id: list[int] | Unset = UNSET,
    group_member_statuses: list[GetAllGroupMembersGroupMemberStatusesItem]
    | Unset = UNSET,
    allowed_chat_users_only: bool | Unset = UNSET,
    allowed_chat_writers_only: bool | Unset = UNSET,
    query: str | Unset = UNSET,
    comment: str | Unset = UNSET,
    member_start_date_after: datetime.date | Unset = UNSET,
    member_start_date_before: datetime.date | Unset = UNSET,
    order_fields: list[str] | Unset = UNSET,
    order_directions: list[GetAllGroupMembersOrderDirectionsItem] | Unset = UNSET,
    person_fields: list[str] | Unset = UNSET,
    include: list[GetAllGroupMembersIncludeItem] | Unset = UNSET,
) -> Response[Any]:
    """Get all group members

     This endpoint returns an array with all group members of one group. In addition to the documented
    query parameters, members can be filtered by group member fields (`<fieldName>=fieldValue`) and/or
    person fields (`person_<fieldName>=fieldValue`) as query parameters.

    Args:
        group_id (int):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        role_ids (list[int] | Unset):
        person_id (list[int] | Unset):
        group_member_statuses (list[GetAllGroupMembersGroupMemberStatusesItem] | Unset):
        allowed_chat_users_only (bool | Unset):
        allowed_chat_writers_only (bool | Unset):
        query (str | Unset):  Example: Peter Maier.
        comment (str | Unset):  Example: Member.
        member_start_date_after (datetime.date | Unset): A simple date in ISO format, e.g.
            '2022-10-19' Example: 2022-10-19.
        member_start_date_before (datetime.date | Unset): A simple date in ISO format, e.g.
            '2022-10-19' Example: 2022-10-19.
        order_fields (list[str] | Unset):
        order_directions (list[GetAllGroupMembersOrderDirectionsItem] | Unset):
        person_fields (list[str] | Unset):
        include (list[GetAllGroupMembersIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        page=page,
        limit=limit,
        role_ids=role_ids,
        person_id=person_id,
        group_member_statuses=group_member_statuses,
        allowed_chat_users_only=allowed_chat_users_only,
        allowed_chat_writers_only=allowed_chat_writers_only,
        query=query,
        comment=comment,
        member_start_date_after=member_start_date_after,
        member_start_date_before=member_start_date_before,
        order_fields=order_fields,
        order_directions=order_directions,
        person_fields=person_fields,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
