import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_persons_person_id_posts_filter_item import (
    GetPersonsPersonIdPostsFilterItem,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: str,
    *,
    filter_: list[GetPersonsPersonIdPostsFilterItem] | Unset = UNSET,
    limit: int | Unset = 10,
    before: datetime.datetime | Unset = UNSET,
    last_post_indentifier: str | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_filter_: list[str] | Unset = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = []
        for filter_item_data in filter_:
            filter_item = filter_item_data.value
            json_filter_.append(filter_item)

    params["filter[]"] = json_filter_

    params["limit"] = limit

    json_before: str | Unset = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat()
    params["before"] = json_before

    params["last_post_indentifier"] = last_post_indentifier

    json_after: str | Unset = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat()
    params["after"] = json_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/persons/{person_id}/posts".format(
            person_id=person_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> str | None:
    if response.status_code == 401:
        response_401 = response.text
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
    filter_: list[GetPersonsPersonIdPostsFilterItem] | Unset = UNSET,
    limit: int | Unset = 10,
    before: datetime.datetime | Unset = UNSET,
    last_post_indentifier: str | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
) -> Response[str]:
    """Returns the posts authored by a person

    Args:
        person_id (str):
        filter_ (list[GetPersonsPersonIdPostsFilterItem] | Unset):
        limit (int | Unset):  Default: 10. Example: 10.
        before (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        last_post_indentifier (str | Unset):
        after (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        filter_=filter_,
        limit=limit,
        before=before,
        last_post_indentifier=last_post_indentifier,
        after=after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
    filter_: list[GetPersonsPersonIdPostsFilterItem] | Unset = UNSET,
    limit: int | Unset = 10,
    before: datetime.datetime | Unset = UNSET,
    last_post_indentifier: str | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
) -> str | None:
    """Returns the posts authored by a person

    Args:
        person_id (str):
        filter_ (list[GetPersonsPersonIdPostsFilterItem] | Unset):
        limit (int | Unset):  Default: 10. Example: 10.
        before (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        last_post_indentifier (str | Unset):
        after (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
        filter_=filter_,
        limit=limit,
        before=before,
        last_post_indentifier=last_post_indentifier,
        after=after,
    ).parsed


async def asyncio_detailed(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
    filter_: list[GetPersonsPersonIdPostsFilterItem] | Unset = UNSET,
    limit: int | Unset = 10,
    before: datetime.datetime | Unset = UNSET,
    last_post_indentifier: str | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
) -> Response[str]:
    """Returns the posts authored by a person

    Args:
        person_id (str):
        filter_ (list[GetPersonsPersonIdPostsFilterItem] | Unset):
        limit (int | Unset):  Default: 10. Example: 10.
        before (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        last_post_indentifier (str | Unset):
        after (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        filter_=filter_,
        limit=limit,
        before=before,
        last_post_indentifier=last_post_indentifier,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
    filter_: list[GetPersonsPersonIdPostsFilterItem] | Unset = UNSET,
    limit: int | Unset = 10,
    before: datetime.datetime | Unset = UNSET,
    last_post_indentifier: str | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
) -> str | None:
    """Returns the posts authored by a person

    Args:
        person_id (str):
        filter_ (list[GetPersonsPersonIdPostsFilterItem] | Unset):
        limit (int | Unset):  Default: 10. Example: 10.
        before (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        last_post_indentifier (str | Unset):
        after (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            filter_=filter_,
            limit=limit,
            before=before,
            last_post_indentifier=last_post_indentifier,
            after=after,
        )
    ).parsed
