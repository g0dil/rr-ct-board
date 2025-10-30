import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_bookings_include_item import GetBookingsIncludeItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: list[GetBookingsIncludeItem] | Unset = UNSET,
    resource_ids: list[int],
    query: str | Unset = UNSET,
    person_id: int | Unset = UNSET,
    status_ids: list[int] | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include: list[str] | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = []
        for include_item_data in include:
            include_item = include_item_data.value
            json_include.append(include_item)

    params["include[]"] = json_include

    json_resource_ids = resource_ids

    params["resource_ids[]"] = json_resource_ids

    params["query"] = query

    params["person_id"] = person_id

    json_status_ids: list[int] | Unset = UNSET
    if not isinstance(status_ids, Unset):
        json_status_ids = status_ids

    params["status_ids[]"] = json_status_ids

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/bookings",
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
    include: list[GetBookingsIncludeItem] | Unset = UNSET,
    resource_ids: list[int],
    query: str | Unset = UNSET,
    person_id: int | Unset = UNSET,
    status_ids: list[int] | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
) -> Response[Any | str]:
    """Your GET endpoint

     Get all bookings matching the specified conditions. (NB: The `to` parameter is here still
    *inclusive*, but will be *exclusive* at a future point in time.)

    Args:
        include (list[GetBookingsIncludeItem] | Unset):
        resource_ids (list[int]):
        query (str | Unset):
        person_id (int | Unset):
        status_ids (list[int] | Unset):
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        include=include,
        resource_ids=resource_ids,
        query=query,
        person_id=person_id,
        status_ids=status_ids,
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    include: list[GetBookingsIncludeItem] | Unset = UNSET,
    resource_ids: list[int],
    query: str | Unset = UNSET,
    person_id: int | Unset = UNSET,
    status_ids: list[int] | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
) -> Any | str | None:
    """Your GET endpoint

     Get all bookings matching the specified conditions. (NB: The `to` parameter is here still
    *inclusive*, but will be *exclusive* at a future point in time.)

    Args:
        include (list[GetBookingsIncludeItem] | Unset):
        resource_ids (list[int]):
        query (str | Unset):
        person_id (int | Unset):
        status_ids (list[int] | Unset):
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        client=client,
        include=include,
        resource_ids=resource_ids,
        query=query,
        person_id=person_id,
        status_ids=status_ids,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    include: list[GetBookingsIncludeItem] | Unset = UNSET,
    resource_ids: list[int],
    query: str | Unset = UNSET,
    person_id: int | Unset = UNSET,
    status_ids: list[int] | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
) -> Response[Any | str]:
    """Your GET endpoint

     Get all bookings matching the specified conditions. (NB: The `to` parameter is here still
    *inclusive*, but will be *exclusive* at a future point in time.)

    Args:
        include (list[GetBookingsIncludeItem] | Unset):
        resource_ids (list[int]):
        query (str | Unset):
        person_id (int | Unset):
        status_ids (list[int] | Unset):
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        include=include,
        resource_ids=resource_ids,
        query=query,
        person_id=person_id,
        status_ids=status_ids,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    include: list[GetBookingsIncludeItem] | Unset = UNSET,
    resource_ids: list[int],
    query: str | Unset = UNSET,
    person_id: int | Unset = UNSET,
    status_ids: list[int] | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
) -> Any | str | None:
    """Your GET endpoint

     Get all bookings matching the specified conditions. (NB: The `to` parameter is here still
    *inclusive*, but will be *exclusive* at a future point in time.)

    Args:
        include (list[GetBookingsIncludeItem] | Unset):
        resource_ids (list[int]):
        query (str | Unset):
        person_id (int | Unset):
        status_ids (list[int] | Unset):
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            resource_ids=resource_ids,
            query=query,
            person_id=person_id,
            status_ids=status_ids,
            from_=from_,
            to=to,
        )
    ).parsed
