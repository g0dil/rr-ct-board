from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_songs_include_item import GetSongsIncludeItem
from ...models.get_songs_key_of_arrangement import GetSongsKeyOfArrangement
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    song_category_ids: list[int] | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    practice: bool | Unset = UNSET,
    key_of_arrangement: GetSongsKeyOfArrangement | Unset = UNSET,
    name: str | Unset = UNSET,
    query: str | Unset = UNSET,
    include: list[GetSongsIncludeItem] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_song_category_ids: list[int] | Unset = UNSET
    if not isinstance(song_category_ids, Unset):
        json_song_category_ids = song_category_ids

    params["song_category_ids[]"] = json_song_category_ids

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["practice"] = practice

    json_key_of_arrangement: str | Unset = UNSET
    if not isinstance(key_of_arrangement, Unset):
        json_key_of_arrangement = key_of_arrangement.value

    params["key_of_arrangement"] = json_key_of_arrangement

    params["name"] = name

    params["query"] = query

    json_include: list[str] | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = []
        for include_item_data in include:
            include_item = include_item_data.value
            json_include.append(include_item)

    params["include"] = json_include

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/songs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 400:
        return None

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
    *,
    client: AuthenticatedClient | Client,
    song_category_ids: list[int] | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    practice: bool | Unset = UNSET,
    key_of_arrangement: GetSongsKeyOfArrangement | Unset = UNSET,
    name: str | Unset = UNSET,
    query: str | Unset = UNSET,
    include: list[GetSongsIncludeItem] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> Response[Any]:
    """Get All Songs

     Get all Songs. Only those songs are returned that the user has permission to view.

    Args:
        song_category_ids (list[int] | Unset):
        ids (list[int] | Unset):
        practice (bool | Unset):
        key_of_arrangement (GetSongsKeyOfArrangement | Unset): Possible keys that the song is
            arranged in Example: F.
        name (str | Unset):
        query (str | Unset):
        include (list[GetSongsIncludeItem] | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        song_category_ids=song_category_ids,
        ids=ids,
        practice=practice,
        key_of_arrangement=key_of_arrangement,
        name=name,
        query=query,
        include=include,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    song_category_ids: list[int] | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    practice: bool | Unset = UNSET,
    key_of_arrangement: GetSongsKeyOfArrangement | Unset = UNSET,
    name: str | Unset = UNSET,
    query: str | Unset = UNSET,
    include: list[GetSongsIncludeItem] | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 10,
) -> Response[Any]:
    """Get All Songs

     Get all Songs. Only those songs are returned that the user has permission to view.

    Args:
        song_category_ids (list[int] | Unset):
        ids (list[int] | Unset):
        practice (bool | Unset):
        key_of_arrangement (GetSongsKeyOfArrangement | Unset): Possible keys that the song is
            arranged in Example: F.
        name (str | Unset):
        query (str | Unset):
        include (list[GetSongsIncludeItem] | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        song_category_ids=song_category_ids,
        ids=ids,
        practice=practice,
        key_of_arrangement=key_of_arrangement,
        name=name,
        query=query,
        include=include,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
