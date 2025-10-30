from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_groups_group_id_members_routines_role_id_group_member_status_group_member_status import (
    DeleteGroupsGroupIdMembersRoutinesRoleIdGroupMemberStatusGroupMemberStatus,
)
from ...types import Response


def _get_kwargs(
    group_id: int,
    role_id: int,
    group_member_status: DeleteGroupsGroupIdMembersRoutinesRoleIdGroupMemberStatusGroupMemberStatus,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/groups/{group_id}/members/routines/{role_id}/{group_member_status}".format(
            group_id=group_id,
            role_id=role_id,
            group_member_status=group_member_status,
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
    group_id: int,
    role_id: int,
    group_member_status: DeleteGroupsGroupIdMembersRoutinesRoleIdGroupMemberStatusGroupMemberStatus,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | str]:
    """Delete membership routine

     Delete the membership routine for the specified group.

    Args:
        group_id (int):  Example: 42.
        role_id (int):  Example: 1.
        group_member_status
            (DeleteGroupsGroupIdMembersRoutinesRoleIdGroupMemberStatusGroupMemberStatus):  Example:
            active.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        role_id=role_id,
        group_member_status=group_member_status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    role_id: int,
    group_member_status: DeleteGroupsGroupIdMembersRoutinesRoleIdGroupMemberStatusGroupMemberStatus,
    *,
    client: AuthenticatedClient | Client,
) -> Any | str | None:
    """Delete membership routine

     Delete the membership routine for the specified group.

    Args:
        group_id (int):  Example: 42.
        role_id (int):  Example: 1.
        group_member_status
            (DeleteGroupsGroupIdMembersRoutinesRoleIdGroupMemberStatusGroupMemberStatus):  Example:
            active.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        group_id=group_id,
        role_id=role_id,
        group_member_status=group_member_status,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    role_id: int,
    group_member_status: DeleteGroupsGroupIdMembersRoutinesRoleIdGroupMemberStatusGroupMemberStatus,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | str]:
    """Delete membership routine

     Delete the membership routine for the specified group.

    Args:
        group_id (int):  Example: 42.
        role_id (int):  Example: 1.
        group_member_status
            (DeleteGroupsGroupIdMembersRoutinesRoleIdGroupMemberStatusGroupMemberStatus):  Example:
            active.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        role_id=role_id,
        group_member_status=group_member_status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    role_id: int,
    group_member_status: DeleteGroupsGroupIdMembersRoutinesRoleIdGroupMemberStatusGroupMemberStatus,
    *,
    client: AuthenticatedClient | Client,
) -> Any | str | None:
    """Delete membership routine

     Delete the membership routine for the specified group.

    Args:
        group_id (int):  Example: 42.
        role_id (int):  Example: 1.
        group_member_status
            (DeleteGroupsGroupIdMembersRoutinesRoleIdGroupMemberStatusGroupMemberStatus):  Example:
            active.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            role_id=role_id,
            group_member_status=group_member_status,
            client=client,
        )
    ).parsed
