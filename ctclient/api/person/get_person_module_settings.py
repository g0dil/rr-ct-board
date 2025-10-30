from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    person_id: int,
    module: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/persons/{person_id}/settings/{module}".format(
            person_id=person_id,
            module=module,
        ),
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
    person_id: int,
    module: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | str]:
    """Get all person settings of a module

     Person settings are grouped per module. This endpoint returns an array of all user settings for a
    person of this module.

    Args:
        person_id (int):  Example: 42.
        module (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        module=module,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: int,
    module: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | str | None:
    """Get all person settings of a module

     Person settings are grouped per module. This endpoint returns an array of all user settings for a
    person of this module.

    Args:
        person_id (int):  Example: 42.
        module (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        person_id=person_id,
        module=module,
        client=client,
    ).parsed


async def asyncio_detailed(
    person_id: int,
    module: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | str]:
    """Get all person settings of a module

     Person settings are grouped per module. This endpoint returns an array of all user settings for a
    person of this module.

    Args:
        person_id (int):  Example: 42.
        module (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        module=module,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: int,
    module: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | str | None:
    """Get all person settings of a module

     Person settings are grouped per module. This endpoint returns an array of all user settings for a
    person of this module.

    Args:
        person_id (int):  Example: 42.
        module (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            module=module,
            client=client,
        )
    ).parsed
