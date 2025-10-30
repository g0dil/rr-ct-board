from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_permissions_permission_domain_type_permission_domain_type import (
    GetPermissionsPermissionDomainTypePermissionDomainType,
)
from ...models.get_permissions_permission_domain_type_response_200 import (
    GetPermissionsPermissionDomainTypeResponse200,
)
from ...types import Response


def _get_kwargs(
    permission_domain_type: GetPermissionsPermissionDomainTypePermissionDomainType,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/permissions/{permission_domain_type}".format(
            permission_domain_type=permission_domain_type,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetPermissionsPermissionDomainTypeResponse200 | str | None:
    if response.status_code == 200:
        response_200 = GetPermissionsPermissionDomainTypeResponse200.from_dict(
            response.json()
        )

        return response_200

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
) -> Response[Any | GetPermissionsPermissionDomainTypeResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    permission_domain_type: GetPermissionsPermissionDomainTypePermissionDomainType,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetPermissionsPermissionDomainTypeResponse200 | str]:
    """
    Args:
        permission_domain_type (GetPermissionsPermissionDomainTypePermissionDomainType):  Example:
            person.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPermissionsPermissionDomainTypeResponse200 | str]
    """

    kwargs = _get_kwargs(
        permission_domain_type=permission_domain_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    permission_domain_type: GetPermissionsPermissionDomainTypePermissionDomainType,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetPermissionsPermissionDomainTypeResponse200 | str | None:
    """
    Args:
        permission_domain_type (GetPermissionsPermissionDomainTypePermissionDomainType):  Example:
            person.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPermissionsPermissionDomainTypeResponse200 | str
    """

    return sync_detailed(
        permission_domain_type=permission_domain_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    permission_domain_type: GetPermissionsPermissionDomainTypePermissionDomainType,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetPermissionsPermissionDomainTypeResponse200 | str]:
    """
    Args:
        permission_domain_type (GetPermissionsPermissionDomainTypePermissionDomainType):  Example:
            person.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPermissionsPermissionDomainTypeResponse200 | str]
    """

    kwargs = _get_kwargs(
        permission_domain_type=permission_domain_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    permission_domain_type: GetPermissionsPermissionDomainTypePermissionDomainType,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetPermissionsPermissionDomainTypeResponse200 | str | None:
    """
    Args:
        permission_domain_type (GetPermissionsPermissionDomainTypePermissionDomainType):  Example:
            person.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPermissionsPermissionDomainTypeResponse200 | str
    """

    return (
        await asyncio_detailed(
            permission_domain_type=permission_domain_type,
            client=client,
        )
    ).parsed
