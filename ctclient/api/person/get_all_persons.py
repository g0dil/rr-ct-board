import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_persons_include_item import GetAllPersonsIncludeItem
from ...models.get_all_persons_response_200 import GetAllPersonsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    status_ids: list[int] | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    birthday_before: datetime.date | Unset = UNSET,
    birthday_after: datetime.date | Unset = UNSET,
    is_archived: bool | Unset = UNSET,
    is_account_locked: bool | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    include: list[GetAllPersonsIncludeItem] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    json_status_ids: list[int] | Unset = UNSET
    if not isinstance(status_ids, Unset):
        json_status_ids = status_ids

    params["status_ids[]"] = json_status_ids

    json_campus_ids: list[int] | Unset = UNSET
    if not isinstance(campus_ids, Unset):
        json_campus_ids = campus_ids

    params["campus_ids[]"] = json_campus_ids

    json_birthday_before: str | Unset = UNSET
    if not isinstance(birthday_before, Unset):
        json_birthday_before = birthday_before.isoformat()
    params["birthday_before"] = json_birthday_before

    json_birthday_after: str | Unset = UNSET
    if not isinstance(birthday_after, Unset):
        json_birthday_after = birthday_after.isoformat()
    params["birthday_after"] = json_birthday_after

    params["is_archived"] = is_archived

    params["is_account_locked"] = is_account_locked

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
        "url": "/persons",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetAllPersonsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetAllPersonsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
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
) -> Response[Any | GetAllPersonsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    ids: list[int] | Unset = UNSET,
    status_ids: list[int] | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    birthday_before: datetime.date | Unset = UNSET,
    birthday_after: datetime.date | Unset = UNSET,
    is_archived: bool | Unset = UNSET,
    is_account_locked: bool | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    include: list[GetAllPersonsIncludeItem] | Unset = UNSET,
) -> Response[Any | GetAllPersonsResponse200]:
    r"""Get all persons

     This endpoint gives you all the people you are allowed to see. Each person object holds only those
    fields you may see. You will get at least an empty array even if you cannot see any person. The
    results are sorted by lastname, firstname.<br><br> We distinguish between `date` and `date-time`
    fields. `date` is a ISO representation like `YYYY-MM-DD`. On the other hand, for `date-time` we
    return and accept a <a href=\"https://www.w3.org/TR/NOTE-datetime\">W3C Zulu date string</a>.
    Example `1994-11-05T08:15:30Z`

    Args:
        ids (list[int] | Unset):
        status_ids (list[int] | Unset):
        campus_ids (list[int] | Unset):
        birthday_before (datetime.date | Unset):
        birthday_after (datetime.date | Unset):
        is_archived (bool | Unset):
        is_account_locked (bool | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        include (list[GetAllPersonsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAllPersonsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        status_ids=status_ids,
        campus_ids=campus_ids,
        birthday_before=birthday_before,
        birthday_after=birthday_after,
        is_archived=is_archived,
        is_account_locked=is_account_locked,
        page=page,
        limit=limit,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    ids: list[int] | Unset = UNSET,
    status_ids: list[int] | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    birthday_before: datetime.date | Unset = UNSET,
    birthday_after: datetime.date | Unset = UNSET,
    is_archived: bool | Unset = UNSET,
    is_account_locked: bool | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    include: list[GetAllPersonsIncludeItem] | Unset = UNSET,
) -> Any | GetAllPersonsResponse200 | None:
    r"""Get all persons

     This endpoint gives you all the people you are allowed to see. Each person object holds only those
    fields you may see. You will get at least an empty array even if you cannot see any person. The
    results are sorted by lastname, firstname.<br><br> We distinguish between `date` and `date-time`
    fields. `date` is a ISO representation like `YYYY-MM-DD`. On the other hand, for `date-time` we
    return and accept a <a href=\"https://www.w3.org/TR/NOTE-datetime\">W3C Zulu date string</a>.
    Example `1994-11-05T08:15:30Z`

    Args:
        ids (list[int] | Unset):
        status_ids (list[int] | Unset):
        campus_ids (list[int] | Unset):
        birthday_before (datetime.date | Unset):
        birthday_after (datetime.date | Unset):
        is_archived (bool | Unset):
        is_account_locked (bool | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        include (list[GetAllPersonsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAllPersonsResponse200
    """

    return sync_detailed(
        client=client,
        ids=ids,
        status_ids=status_ids,
        campus_ids=campus_ids,
        birthday_before=birthday_before,
        birthday_after=birthday_after,
        is_archived=is_archived,
        is_account_locked=is_account_locked,
        page=page,
        limit=limit,
        include=include,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    ids: list[int] | Unset = UNSET,
    status_ids: list[int] | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    birthday_before: datetime.date | Unset = UNSET,
    birthday_after: datetime.date | Unset = UNSET,
    is_archived: bool | Unset = UNSET,
    is_account_locked: bool | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    include: list[GetAllPersonsIncludeItem] | Unset = UNSET,
) -> Response[Any | GetAllPersonsResponse200]:
    r"""Get all persons

     This endpoint gives you all the people you are allowed to see. Each person object holds only those
    fields you may see. You will get at least an empty array even if you cannot see any person. The
    results are sorted by lastname, firstname.<br><br> We distinguish between `date` and `date-time`
    fields. `date` is a ISO representation like `YYYY-MM-DD`. On the other hand, for `date-time` we
    return and accept a <a href=\"https://www.w3.org/TR/NOTE-datetime\">W3C Zulu date string</a>.
    Example `1994-11-05T08:15:30Z`

    Args:
        ids (list[int] | Unset):
        status_ids (list[int] | Unset):
        campus_ids (list[int] | Unset):
        birthday_before (datetime.date | Unset):
        birthday_after (datetime.date | Unset):
        is_archived (bool | Unset):
        is_account_locked (bool | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        include (list[GetAllPersonsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAllPersonsResponse200]
    """

    kwargs = _get_kwargs(
        ids=ids,
        status_ids=status_ids,
        campus_ids=campus_ids,
        birthday_before=birthday_before,
        birthday_after=birthday_after,
        is_archived=is_archived,
        is_account_locked=is_account_locked,
        page=page,
        limit=limit,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    ids: list[int] | Unset = UNSET,
    status_ids: list[int] | Unset = UNSET,
    campus_ids: list[int] | Unset = UNSET,
    birthday_before: datetime.date | Unset = UNSET,
    birthday_after: datetime.date | Unset = UNSET,
    is_archived: bool | Unset = UNSET,
    is_account_locked: bool | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    include: list[GetAllPersonsIncludeItem] | Unset = UNSET,
) -> Any | GetAllPersonsResponse200 | None:
    r"""Get all persons

     This endpoint gives you all the people you are allowed to see. Each person object holds only those
    fields you may see. You will get at least an empty array even if you cannot see any person. The
    results are sorted by lastname, firstname.<br><br> We distinguish between `date` and `date-time`
    fields. `date` is a ISO representation like `YYYY-MM-DD`. On the other hand, for `date-time` we
    return and accept a <a href=\"https://www.w3.org/TR/NOTE-datetime\">W3C Zulu date string</a>.
    Example `1994-11-05T08:15:30Z`

    Args:
        ids (list[int] | Unset):
        status_ids (list[int] | Unset):
        campus_ids (list[int] | Unset):
        birthday_before (datetime.date | Unset):
        birthday_after (datetime.date | Unset):
        is_archived (bool | Unset):
        is_account_locked (bool | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.
        include (list[GetAllPersonsIncludeItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAllPersonsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            status_ids=status_ids,
            campus_ids=campus_ids,
            birthday_before=birthday_before,
            birthday_after=birthday_after,
            is_archived=is_archived,
            is_account_locked=is_account_locked,
            page=page,
            limit=limit,
            include=include,
        )
    ).parsed
