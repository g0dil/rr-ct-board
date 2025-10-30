import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_groups_group_id_meetings_export_direction import (
    GetGroupsGroupIdMeetingsExportDirection,
)
from ...models.get_groups_group_id_meetings_export_format import (
    GetGroupsGroupIdMeetingsExportFormat,
)
from ...models.get_groups_group_id_meetings_export_type import (
    GetGroupsGroupIdMeetingsExportType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    format_: GetGroupsGroupIdMeetingsExportFormat | Unset = UNSET,
    type_: GetGroupsGroupIdMeetingsExportType | Unset = UNSET,
    is_canceled: bool | Unset = UNSET,
    is_completed: bool | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    direction: GetGroupsGroupIdMeetingsExportDirection
    | Unset = GetGroupsGroupIdMeetingsExportDirection.FORWARD,
    limit: int | Unset = 10,
    page: int | Unset = 1,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["is_canceled"] = is_canceled

    params["is_completed"] = is_completed

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    json_direction: str | Unset = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value

    params["direction"] = json_direction

    params["limit"] = limit

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/groups/{group_id}/meetings/export".format(
            group_id=group_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | str | None:
    if response.status_code == 200:
        response_200 = response.text
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
    format_: GetGroupsGroupIdMeetingsExportFormat | Unset = UNSET,
    type_: GetGroupsGroupIdMeetingsExportType | Unset = UNSET,
    is_canceled: bool | Unset = UNSET,
    is_completed: bool | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    direction: GetGroupsGroupIdMeetingsExportDirection
    | Unset = GetGroupsGroupIdMeetingsExportDirection.FORWARD,
    limit: int | Unset = 10,
    page: int | Unset = 1,
) -> Response[Any | str]:
    """
    Args:
        group_id (int):  Example: 42.
        format_ (GetGroupsGroupIdMeetingsExportFormat | Unset):
        type_ (GetGroupsGroupIdMeetingsExportType | Unset):
        is_canceled (bool | Unset):
        is_completed (bool | Unset):
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        direction (GetGroupsGroupIdMeetingsExportDirection | Unset):  Default:
            GetGroupsGroupIdMeetingsExportDirection.FORWARD. Example: forward.
        limit (int | Unset):  Default: 10. Example: 10.
        page (int | Unset):  Default: 1. Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        format_=format_,
        type_=type_,
        is_canceled=is_canceled,
        is_completed=is_completed,
        from_=from_,
        to=to,
        direction=direction,
        limit=limit,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    format_: GetGroupsGroupIdMeetingsExportFormat | Unset = UNSET,
    type_: GetGroupsGroupIdMeetingsExportType | Unset = UNSET,
    is_canceled: bool | Unset = UNSET,
    is_completed: bool | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    direction: GetGroupsGroupIdMeetingsExportDirection
    | Unset = GetGroupsGroupIdMeetingsExportDirection.FORWARD,
    limit: int | Unset = 10,
    page: int | Unset = 1,
) -> Any | str | None:
    """
    Args:
        group_id (int):  Example: 42.
        format_ (GetGroupsGroupIdMeetingsExportFormat | Unset):
        type_ (GetGroupsGroupIdMeetingsExportType | Unset):
        is_canceled (bool | Unset):
        is_completed (bool | Unset):
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        direction (GetGroupsGroupIdMeetingsExportDirection | Unset):  Default:
            GetGroupsGroupIdMeetingsExportDirection.FORWARD. Example: forward.
        limit (int | Unset):  Default: 10. Example: 10.
        page (int | Unset):  Default: 1. Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        format_=format_,
        type_=type_,
        is_canceled=is_canceled,
        is_completed=is_completed,
        from_=from_,
        to=to,
        direction=direction,
        limit=limit,
        page=page,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    format_: GetGroupsGroupIdMeetingsExportFormat | Unset = UNSET,
    type_: GetGroupsGroupIdMeetingsExportType | Unset = UNSET,
    is_canceled: bool | Unset = UNSET,
    is_completed: bool | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    direction: GetGroupsGroupIdMeetingsExportDirection
    | Unset = GetGroupsGroupIdMeetingsExportDirection.FORWARD,
    limit: int | Unset = 10,
    page: int | Unset = 1,
) -> Response[Any | str]:
    """
    Args:
        group_id (int):  Example: 42.
        format_ (GetGroupsGroupIdMeetingsExportFormat | Unset):
        type_ (GetGroupsGroupIdMeetingsExportType | Unset):
        is_canceled (bool | Unset):
        is_completed (bool | Unset):
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        direction (GetGroupsGroupIdMeetingsExportDirection | Unset):  Default:
            GetGroupsGroupIdMeetingsExportDirection.FORWARD. Example: forward.
        limit (int | Unset):  Default: 10. Example: 10.
        page (int | Unset):  Default: 1. Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        format_=format_,
        type_=type_,
        is_canceled=is_canceled,
        is_completed=is_completed,
        from_=from_,
        to=to,
        direction=direction,
        limit=limit,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    format_: GetGroupsGroupIdMeetingsExportFormat | Unset = UNSET,
    type_: GetGroupsGroupIdMeetingsExportType | Unset = UNSET,
    is_canceled: bool | Unset = UNSET,
    is_completed: bool | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    direction: GetGroupsGroupIdMeetingsExportDirection
    | Unset = GetGroupsGroupIdMeetingsExportDirection.FORWARD,
    limit: int | Unset = 10,
    page: int | Unset = 1,
) -> Any | str | None:
    """
    Args:
        group_id (int):  Example: 42.
        format_ (GetGroupsGroupIdMeetingsExportFormat | Unset):
        type_ (GetGroupsGroupIdMeetingsExportType | Unset):
        is_canceled (bool | Unset):
        is_completed (bool | Unset):
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        direction (GetGroupsGroupIdMeetingsExportDirection | Unset):  Default:
            GetGroupsGroupIdMeetingsExportDirection.FORWARD. Example: forward.
        limit (int | Unset):  Default: 10. Example: 10.
        page (int | Unset):  Default: 1. Example: 1.

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
            format_=format_,
            type_=type_,
            is_canceled=is_canceled,
            is_completed=is_completed,
            from_=from_,
            to=to,
            direction=direction,
            limit=limit,
            page=page,
        )
    ).parsed
