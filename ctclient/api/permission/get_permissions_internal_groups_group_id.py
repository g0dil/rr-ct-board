from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_permissions_internal_groups_group_id_response_200 import (
    GetPermissionsInternalGroupsGroupIdResponse200,
)
from ...types import Response


def _get_kwargs(
    group_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/permissions/internal/groups/{group_id}".format(
            group_id=group_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPermissionsInternalGroupsGroupIdResponse200 | None:
    if response.status_code == 200:
        response_200 = GetPermissionsInternalGroupsGroupIdResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPermissionsInternalGroupsGroupIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPermissionsInternalGroupsGroupIdResponse200]:
    """Lookup Group-Related Group Internal Permissions

     Group internal permissions can affect different entities in ChurchTools such as `Group`. This
    endpoint calculates the result of all group internal permissions with regard to a group. That means,
    the response is the result for the current user, to find out if s/he can do certain actions based on
    group internal permissions.

    Example: The API response has `+add person: true`. This means, the current user can add persons to
    this group based on this group internal permissions on that group or superior groups through
    inheritance.

    Args:
        group_id (int):  Example: 42.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPermissionsInternalGroupsGroupIdResponse200]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetPermissionsInternalGroupsGroupIdResponse200 | None:
    """Lookup Group-Related Group Internal Permissions

     Group internal permissions can affect different entities in ChurchTools such as `Group`. This
    endpoint calculates the result of all group internal permissions with regard to a group. That means,
    the response is the result for the current user, to find out if s/he can do certain actions based on
    group internal permissions.

    Example: The API response has `+add person: true`. This means, the current user can add persons to
    this group based on this group internal permissions on that group or superior groups through
    inheritance.

    Args:
        group_id (int):  Example: 42.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPermissionsInternalGroupsGroupIdResponse200
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPermissionsInternalGroupsGroupIdResponse200]:
    """Lookup Group-Related Group Internal Permissions

     Group internal permissions can affect different entities in ChurchTools such as `Group`. This
    endpoint calculates the result of all group internal permissions with regard to a group. That means,
    the response is the result for the current user, to find out if s/he can do certain actions based on
    group internal permissions.

    Example: The API response has `+add person: true`. This means, the current user can add persons to
    this group based on this group internal permissions on that group or superior groups through
    inheritance.

    Args:
        group_id (int):  Example: 42.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPermissionsInternalGroupsGroupIdResponse200]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetPermissionsInternalGroupsGroupIdResponse200 | None:
    """Lookup Group-Related Group Internal Permissions

     Group internal permissions can affect different entities in ChurchTools such as `Group`. This
    endpoint calculates the result of all group internal permissions with regard to a group. That means,
    the response is the result for the current user, to find out if s/he can do certain actions based on
    group internal permissions.

    Example: The API response has `+add person: true`. This means, the current user can add persons to
    this group based on this group internal permissions on that group or superior groups through
    inheritance.

    Args:
        group_id (int):  Example: 42.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPermissionsInternalGroupsGroupIdResponse200
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
