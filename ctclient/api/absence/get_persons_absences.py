import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_persons_absences_order_direction import (
    GetPersonsAbsencesOrderDirection,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: int,
    *,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    order_direction: GetPersonsAbsencesOrderDirection | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    json_order_direction: str | Unset = UNSET
    if not isinstance(order_direction, Unset):
        json_order_direction = order_direction.value

    params["order_direction"] = json_order_direction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/persons/{person_id}/absences".format(
            person_id=person_id,
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
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    order_direction: GetPersonsAbsencesOrderDirection | Unset = UNSET,
) -> Response[Any]:
    """Fetch all absences for a person

     This endpoint returns absences for a person. Absences are sorted by startDate that means, the newest
    absence is first.

    The endpoint uses a time window. If no query parameter are present only absences between two weeks
    ago and two weeks in the future are returned.

    Args:
        person_id (int):  Example: 42.
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        order_direction (GetPersonsAbsencesOrderDirection | Unset):  Example: DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        from_=from_,
        to=to,
        order_direction=order_direction,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    order_direction: GetPersonsAbsencesOrderDirection | Unset = UNSET,
) -> Response[Any]:
    """Fetch all absences for a person

     This endpoint returns absences for a person. Absences are sorted by startDate that means, the newest
    absence is first.

    The endpoint uses a time window. If no query parameter are present only absences between two weeks
    ago and two weeks in the future are returned.

    Args:
        person_id (int):  Example: 42.
        from_ (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        to (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        order_direction (GetPersonsAbsencesOrderDirection | Unset):  Example: DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        from_=from_,
        to=to,
        order_direction=order_direction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
