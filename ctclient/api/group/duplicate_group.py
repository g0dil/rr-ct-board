from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.duplicate_group_response_201 import DuplicateGroupResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    new_name: str,
    copy_members: bool | Unset = UNSET,
    copy_permissions: bool | Unset = UNSET,
    copy_automatic_emails: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["newName"] = new_name

    params["copyMembers"] = copy_members

    params["copyPermissions"] = copy_permissions

    params["copyAutomaticEmails"] = copy_automatic_emails

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/groups/{group_id}/duplicate".format(
            group_id=group_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DuplicateGroupResponse201 | None:
    if response.status_code == 201:
        response_201 = DuplicateGroupResponse201.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DuplicateGroupResponse201]:
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
    new_name: str,
    copy_members: bool | Unset = UNSET,
    copy_permissions: bool | Unset = UNSET,
    copy_automatic_emails: bool | Unset = UNSET,
) -> Response[DuplicateGroupResponse201]:
    """Duplicate a group

    Args:
        group_id (int):  Example: 42.
        new_name (str):
        copy_members (bool | Unset):
        copy_permissions (bool | Unset):
        copy_automatic_emails (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DuplicateGroupResponse201]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        new_name=new_name,
        copy_members=copy_members,
        copy_permissions=copy_permissions,
        copy_automatic_emails=copy_automatic_emails,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    new_name: str,
    copy_members: bool | Unset = UNSET,
    copy_permissions: bool | Unset = UNSET,
    copy_automatic_emails: bool | Unset = UNSET,
) -> DuplicateGroupResponse201 | None:
    """Duplicate a group

    Args:
        group_id (int):  Example: 42.
        new_name (str):
        copy_members (bool | Unset):
        copy_permissions (bool | Unset):
        copy_automatic_emails (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DuplicateGroupResponse201
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        new_name=new_name,
        copy_members=copy_members,
        copy_permissions=copy_permissions,
        copy_automatic_emails=copy_automatic_emails,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    new_name: str,
    copy_members: bool | Unset = UNSET,
    copy_permissions: bool | Unset = UNSET,
    copy_automatic_emails: bool | Unset = UNSET,
) -> Response[DuplicateGroupResponse201]:
    """Duplicate a group

    Args:
        group_id (int):  Example: 42.
        new_name (str):
        copy_members (bool | Unset):
        copy_permissions (bool | Unset):
        copy_automatic_emails (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DuplicateGroupResponse201]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        new_name=new_name,
        copy_members=copy_members,
        copy_permissions=copy_permissions,
        copy_automatic_emails=copy_automatic_emails,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    new_name: str,
    copy_members: bool | Unset = UNSET,
    copy_permissions: bool | Unset = UNSET,
    copy_automatic_emails: bool | Unset = UNSET,
) -> DuplicateGroupResponse201 | None:
    """Duplicate a group

    Args:
        group_id (int):  Example: 42.
        new_name (str):
        copy_members (bool | Unset):
        copy_permissions (bool | Unset):
        copy_automatic_emails (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DuplicateGroupResponse201
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            new_name=new_name,
            copy_members=copy_members,
            copy_permissions=copy_permissions,
            copy_automatic_emails=copy_automatic_emails,
        )
    ).parsed
