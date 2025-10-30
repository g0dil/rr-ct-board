from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: int,
    *,
    show_overdue_groups: bool | Unset = False,
    show_inactive_groups: bool | Unset = False,
    show_to_delete_memberships: bool | Unset = False,
    show_requested_or_waiting_memberships: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["show_overdue_groups"] = show_overdue_groups

    params["show_inactive_groups"] = show_inactive_groups

    params["show_to_delete_memberships"] = show_to_delete_memberships

    params["show_requested_or_waiting_memberships"] = (
        show_requested_or_waiting_memberships
    )

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/persons/{person_id}/groups".format(
            person_id=person_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 401:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    show_overdue_groups: bool | Unset = False,
    show_inactive_groups: bool | Unset = False,
    show_to_delete_memberships: bool | Unset = False,
    show_requested_or_waiting_memberships: bool | Unset = False,
) -> Response[Any]:
    """Get all groups a member is in

     This endpoint returns an array with all groups the user is in.

    Args:
        person_id (int):  Example: 42.
        show_overdue_groups (bool | Unset):  Default: False. Example: True.
        show_inactive_groups (bool | Unset):  Default: False. Example: True.
        show_to_delete_memberships (bool | Unset):  Default: False. Example: True.
        show_requested_or_waiting_memberships (bool | Unset):  Default: False. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        show_overdue_groups=show_overdue_groups,
        show_inactive_groups=show_inactive_groups,
        show_to_delete_memberships=show_to_delete_memberships,
        show_requested_or_waiting_memberships=show_requested_or_waiting_memberships,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    person_id: int,
    *,
    client: AuthenticatedClient | Client,
    show_overdue_groups: bool | Unset = False,
    show_inactive_groups: bool | Unset = False,
    show_to_delete_memberships: bool | Unset = False,
    show_requested_or_waiting_memberships: bool | Unset = False,
) -> Response[Any]:
    """Get all groups a member is in

     This endpoint returns an array with all groups the user is in.

    Args:
        person_id (int):  Example: 42.
        show_overdue_groups (bool | Unset):  Default: False. Example: True.
        show_inactive_groups (bool | Unset):  Default: False. Example: True.
        show_to_delete_memberships (bool | Unset):  Default: False. Example: True.
        show_requested_or_waiting_memberships (bool | Unset):  Default: False. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        show_overdue_groups=show_overdue_groups,
        show_inactive_groups=show_inactive_groups,
        show_to_delete_memberships=show_to_delete_memberships,
        show_requested_or_waiting_memberships=show_requested_or_waiting_memberships,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
