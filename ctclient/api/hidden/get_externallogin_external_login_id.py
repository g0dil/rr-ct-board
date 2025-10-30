from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_externallogin_external_login_id_response_200 import (
    GetExternalloginExternalLoginIdResponse200,
)
from ...types import Response


def _get_kwargs(
    external_login_id: float,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/externallogins/{external_login_id}".format(
            external_login_id=external_login_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetExternalloginExternalLoginIdResponse200 | str | None:
    if response.status_code == 200:
        response_200 = GetExternalloginExternalLoginIdResponse200.from_dict(
            response.json()
        )

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
) -> Response[Any | GetExternalloginExternalLoginIdResponse200 | str]:
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
) -> Response[Any | GetExternalloginExternalLoginIdResponse200 | str]:
    """Get resource

     Get the specified external login.

    Args:
        external_login_id (float):  Example: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetExternalloginExternalLoginIdResponse200 | str]
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
) -> Any | GetExternalloginExternalLoginIdResponse200 | str | None:
    """Get resource

     Get the specified external login.

    Args:
        external_login_id (float):  Example: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetExternalloginExternalLoginIdResponse200 | str
    """

    return sync_detailed(
        external_login_id=external_login_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    external_login_id: float,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetExternalloginExternalLoginIdResponse200 | str]:
    """Get resource

     Get the specified external login.

    Args:
        external_login_id (float):  Example: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetExternalloginExternalLoginIdResponse200 | str]
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
) -> Any | GetExternalloginExternalLoginIdResponse200 | str | None:
    """Get resource

     Get the specified external login.

    Args:
        external_login_id (float):  Example: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetExternalloginExternalLoginIdResponse200 | str
    """

    return (
        await asyncio_detailed(
            external_login_id=external_login_id,
            client=client,
        )
    ).parsed
