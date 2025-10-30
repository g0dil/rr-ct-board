from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_songs_song_id_arrangements_body import (
    PostSongsSongIdArrangementsBody,
)
from ...types import Response


def _get_kwargs(
    song_id: int,
    *,
    body: PostSongsSongIdArrangementsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/songs/{song_id}/arrangements".format(
            song_id=song_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | str | None:
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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
    song_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostSongsSongIdArrangementsBody,
) -> Response[Any | str]:
    """Create new arrangement for song

     Create a new arrangement for the specified song.

    Args:
        song_id (int):  Example: 42.
        body (PostSongsSongIdArrangementsBody): Details about a song's arrangement.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        song_id=song_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    song_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostSongsSongIdArrangementsBody,
) -> Any | str | None:
    """Create new arrangement for song

     Create a new arrangement for the specified song.

    Args:
        song_id (int):  Example: 42.
        body (PostSongsSongIdArrangementsBody): Details about a song's arrangement.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        song_id=song_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    song_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostSongsSongIdArrangementsBody,
) -> Response[Any | str]:
    """Create new arrangement for song

     Create a new arrangement for the specified song.

    Args:
        song_id (int):  Example: 42.
        body (PostSongsSongIdArrangementsBody): Details about a song's arrangement.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        song_id=song_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    song_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostSongsSongIdArrangementsBody,
) -> Any | str | None:
    """Create new arrangement for song

     Create a new arrangement for the specified song.

    Args:
        song_id (int):  Example: 42.
        body (PostSongsSongIdArrangementsBody): Details about a song's arrangement.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            song_id=song_id,
            client=client,
            body=body,
        )
    ).parsed
