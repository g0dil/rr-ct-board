from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    key_id: int,
    language_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/translations/{key_id}/languages/{language_id}".format(
            key_id=key_id,
            language_id=language_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | str | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
    key_id: int,
    language_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | str]:
    """Delete translation language for key

     Delete language for translation key

    Args:
        key_id (int):
        language_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
        language_id=language_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key_id: int,
    language_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | str | None:
    """Delete translation language for key

     Delete language for translation key

    Args:
        key_id (int):
        language_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        key_id=key_id,
        language_id=language_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    key_id: int,
    language_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | str]:
    """Delete translation language for key

     Delete language for translation key

    Args:
        key_id (int):
        language_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
        language_id=language_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key_id: int,
    language_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | str | None:
    """Delete translation language for key

     Delete language for translation key

    Args:
        key_id (int):
        language_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            key_id=key_id,
            language_id=language_id,
            client=client,
        )
    ).parsed
