import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_meetings_direction import GetAllMeetingsDirection
from ...models.get_all_meetings_include_item import GetAllMeetingsIncludeItem
from ...models.get_all_meetings_response_200 import GetAllMeetingsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    is_canceled: bool | Unset = UNSET,
    is_completed: bool | Unset = UNSET,
    direction: GetAllMeetingsDirection | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    include: list[GetAllMeetingsIncludeItem] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["is_canceled"] = is_canceled

    params["is_completed"] = is_completed

    json_direction: str | Unset = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value

    params["direction"] = json_direction

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["page"] = page

    params["limit"] = limit

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
        "url": "/groups/{group_id}/meetings".format(
            group_id=group_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetAllMeetingsResponse200 | str | None:
    if response.status_code == 200:
        response_200 = GetAllMeetingsResponse200.from_dict(response.json())

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
) -> Response[Any | GetAllMeetingsResponse200 | str]:
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
    is_canceled: bool | Unset = UNSET,
    is_completed: bool | Unset = UNSET,
    direction: GetAllMeetingsDirection | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    include: list[GetAllMeetingsIncludeItem] | Unset = UNSET,
) -> Response[Any | GetAllMeetingsResponse200 | str]:
    """Get all group meetings for a specific group

     Get all group meetings for a specific group matching the specified condition(s).

    Args:
        group_id (int):  Example: 42.
        is_canceled (bool | Unset):
        is_completed (bool | Unset):
        direction (GetAllMeetingsDirection | Unset):
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        include (list[GetAllMeetingsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAllMeetingsResponse200 | str]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        is_canceled=is_canceled,
        is_completed=is_completed,
        direction=direction,
        from_=from_,
        to=to,
        page=page,
        limit=limit,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    is_canceled: bool | Unset = UNSET,
    is_completed: bool | Unset = UNSET,
    direction: GetAllMeetingsDirection | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    include: list[GetAllMeetingsIncludeItem] | Unset = UNSET,
) -> Any | GetAllMeetingsResponse200 | str | None:
    """Get all group meetings for a specific group

     Get all group meetings for a specific group matching the specified condition(s).

    Args:
        group_id (int):  Example: 42.
        is_canceled (bool | Unset):
        is_completed (bool | Unset):
        direction (GetAllMeetingsDirection | Unset):
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        include (list[GetAllMeetingsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAllMeetingsResponse200 | str
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        is_canceled=is_canceled,
        is_completed=is_completed,
        direction=direction,
        from_=from_,
        to=to,
        page=page,
        limit=limit,
        include=include,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    is_canceled: bool | Unset = UNSET,
    is_completed: bool | Unset = UNSET,
    direction: GetAllMeetingsDirection | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    include: list[GetAllMeetingsIncludeItem] | Unset = UNSET,
) -> Response[Any | GetAllMeetingsResponse200 | str]:
    """Get all group meetings for a specific group

     Get all group meetings for a specific group matching the specified condition(s).

    Args:
        group_id (int):  Example: 42.
        is_canceled (bool | Unset):
        is_completed (bool | Unset):
        direction (GetAllMeetingsDirection | Unset):
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        include (list[GetAllMeetingsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAllMeetingsResponse200 | str]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        is_canceled=is_canceled,
        is_completed=is_completed,
        direction=direction,
        from_=from_,
        to=to,
        page=page,
        limit=limit,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    is_canceled: bool | Unset = UNSET,
    is_completed: bool | Unset = UNSET,
    direction: GetAllMeetingsDirection | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    include: list[GetAllMeetingsIncludeItem] | Unset = UNSET,
) -> Any | GetAllMeetingsResponse200 | str | None:
    """Get all group meetings for a specific group

     Get all group meetings for a specific group matching the specified condition(s).

    Args:
        group_id (int):  Example: 42.
        is_canceled (bool | Unset):
        is_completed (bool | Unset):
        direction (GetAllMeetingsDirection | Unset):
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        include (list[GetAllMeetingsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAllMeetingsResponse200 | str
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            is_canceled=is_canceled,
            is_completed=is_completed,
            direction=direction,
            from_=from_,
            to=to,
            page=page,
            limit=limit,
            include=include,
        )
    ).parsed
