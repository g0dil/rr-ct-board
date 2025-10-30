from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_person_loginstring_response_200 import (
    GetPersonLoginstringResponse200,
)
from ...types import Response


def _get_kwargs(
    person_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/persons/{person_id}/loginstring".format(
            person_id=person_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetPersonLoginstringResponse200 | str | None:
    if response.status_code == 200:
        response_200 = GetPersonLoginstringResponse200.from_dict(response.json())

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
) -> Response[Any | GetPersonLoginstringResponse200 | str]:
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
) -> Response[Any | GetPersonLoginstringResponse200 | str]:
    """Get login string for a person

    Args:
        person_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPersonLoginstringResponse200 | str]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetPersonLoginstringResponse200 | str | None:
    """Get login string for a person

    Args:
        person_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPersonLoginstringResponse200 | str
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetPersonLoginstringResponse200 | str]:
    """Get login string for a person

    Args:
        person_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPersonLoginstringResponse200 | str]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetPersonLoginstringResponse200 | str | None:
    """Get login string for a person

    Args:
        person_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPersonLoginstringResponse200 | str
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
        )
    ).parsed
