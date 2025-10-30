from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_externallogins_externalloginid_response_409 import (
    DeleteExternalloginsExternalloginidResponse409,
)
from ...types import Response


def _get_kwargs(
    external_login_id: float,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/externallogins/{external_login_id}".format(
            external_login_id=external_login_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteExternalloginsExternalloginidResponse409 | str | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = response.text
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 409:
        response_409 = DeleteExternalloginsExternalloginidResponse409.from_dict(
            response.json()
        )

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteExternalloginsExternalloginidResponse409 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    external_login_id: float,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteExternalloginsExternalloginidResponse409 | str]:
    """Delete external login

     Delete specified external login

    Args:
        external_login_id (float):  Example: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteExternalloginsExternalloginidResponse409 | str]
    """

    kwargs = _get_kwargs(
        external_login_id=external_login_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    external_login_id: float,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteExternalloginsExternalloginidResponse409 | str | None:
    """Delete external login

     Delete specified external login

    Args:
        external_login_id (float):  Example: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteExternalloginsExternalloginidResponse409 | str
    """

    return sync_detailed(
        external_login_id=external_login_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    external_login_id: float,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteExternalloginsExternalloginidResponse409 | str]:
    """Delete external login

     Delete specified external login

    Args:
        external_login_id (float):  Example: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteExternalloginsExternalloginidResponse409 | str]
    """

    kwargs = _get_kwargs(
        external_login_id=external_login_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    external_login_id: float,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteExternalloginsExternalloginidResponse409 | str | None:
    """Delete external login

     Delete specified external login

    Args:
        external_login_id (float):  Example: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteExternalloginsExternalloginidResponse409 | str
    """

    return (
        await asyncio_detailed(
            external_login_id=external_login_id,
            client=client,
        )
    ).parsed
