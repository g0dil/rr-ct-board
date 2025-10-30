from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_persons_person_id_followups_filter_item import (
    GetPersonsPersonIdFollowupsFilterItem,
)
from ...models.get_persons_person_id_followups_response_200 import (
    GetPersonsPersonIdFollowupsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: int,
    *,
    filter_: list[GetPersonsPersonIdFollowupsFilterItem] | Unset = UNSET,
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
        "url": "/persons/{person_id}/followups".format(
            person_id=person_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetPersonsPersonIdFollowupsResponse200 | str | None:
    if response.status_code == 200:
        response_200 = GetPersonsPersonIdFollowupsResponse200.from_dict(response.json())

        return response_200

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
) -> Response[Any | GetPersonsPersonIdFollowupsResponse200 | str]:
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
    filter_: list[GetPersonsPersonIdFollowupsFilterItem] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> Response[Any | GetPersonsPersonIdFollowupsResponse200 | str]:
    """Get a person's follow-ups

     Returns all follow-ups pertaining to the specified person.

    Args:
        person_id (int):  Example: 42.
        filter_ (list[GetPersonsPersonIdFollowupsFilterItem] | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPersonsPersonIdFollowupsResponse200 | str]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        filter_=filter_,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    filter_: list[GetPersonsPersonIdFollowupsFilterItem] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> Any | GetPersonsPersonIdFollowupsResponse200 | str | None:
    """Get a person's follow-ups

     Returns all follow-ups pertaining to the specified person.

    Args:
        person_id (int):  Example: 42.
        filter_ (list[GetPersonsPersonIdFollowupsFilterItem] | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPersonsPersonIdFollowupsResponse200 | str
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
        filter_=filter_,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    filter_: list[GetPersonsPersonIdFollowupsFilterItem] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> Response[Any | GetPersonsPersonIdFollowupsResponse200 | str]:
    """Get a person's follow-ups

     Returns all follow-ups pertaining to the specified person.

    Args:
        person_id (int):  Example: 42.
        filter_ (list[GetPersonsPersonIdFollowupsFilterItem] | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPersonsPersonIdFollowupsResponse200 | str]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        filter_=filter_,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    filter_: list[GetPersonsPersonIdFollowupsFilterItem] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> Any | GetPersonsPersonIdFollowupsResponse200 | str | None:
    """Get a person's follow-ups

     Returns all follow-ups pertaining to the specified person.

    Args:
        person_id (int):  Example: 42.
        filter_ (list[GetPersonsPersonIdFollowupsFilterItem] | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPersonsPersonIdFollowupsResponse200 | str
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            filter_=filter_,
            page=page,
            limit=limit,
        )
    ).parsed
