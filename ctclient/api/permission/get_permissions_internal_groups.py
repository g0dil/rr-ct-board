from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_permissions_internal_groups_response_200 import (
    GetPermissionsInternalGroupsResponse200,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/permissions/internal/groups",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPermissionsInternalGroupsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetPermissionsInternalGroupsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPermissionsInternalGroupsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPermissionsInternalGroupsResponse200]:
    """Your GET endpoint

     Group internal permissions can affect different entities in ChurchTools such as `Group`. This
    endpoint calculates the result of all group internal permissions. That means, the response is the
    result for the current user, to find out if s/he can do certain actions based on group internal
    permissions.

    Example: The API response has `+add person: true`. This means, the current user can add persons to
    this group based on this group internal permissions on that group or superior groups through
    inheritance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPermissionsInternalGroupsResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetPermissionsInternalGroupsResponse200 | None:
    """Your GET endpoint

     Group internal permissions can affect different entities in ChurchTools such as `Group`. This
    endpoint calculates the result of all group internal permissions. That means, the response is the
    result for the current user, to find out if s/he can do certain actions based on group internal
    permissions.

    Example: The API response has `+add person: true`. This means, the current user can add persons to
    this group based on this group internal permissions on that group or superior groups through
    inheritance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPermissionsInternalGroupsResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPermissionsInternalGroupsResponse200]:
    """Your GET endpoint

     Group internal permissions can affect different entities in ChurchTools such as `Group`. This
    endpoint calculates the result of all group internal permissions. That means, the response is the
    result for the current user, to find out if s/he can do certain actions based on group internal
    permissions.

    Example: The API response has `+add person: true`. This means, the current user can add persons to
    this group based on this group internal permissions on that group or superior groups through
    inheritance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPermissionsInternalGroupsResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetPermissionsInternalGroupsResponse200 | None:
    """Your GET endpoint

     Group internal permissions can affect different entities in ChurchTools such as `Group`. This
    endpoint calculates the result of all group internal permissions. That means, the response is the
    result for the current user, to find out if s/he can do certain actions based on group internal
    permissions.

    Example: The API response has `+add person: true`. This means, the current user can add persons to
    this group based on this group internal permissions on that group or superior groups through
    inheritance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPermissionsInternalGroupsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
