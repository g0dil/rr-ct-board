from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_groups_group_id_meetings_meeting_id_members_member_id_body import (
    DeleteGroupsGroupIdMeetingsMeetingIdMembersMemberIdBody,
)
from ...types import Response


def _get_kwargs(
    group_id: int,
    meeting_id: int,
    member_id: int,
    *,
    body: DeleteGroupsGroupIdMeetingsMeetingIdMembersMemberIdBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/groups/{group_id}/meetings/{meeting_id}/members/{member_id}".format(
            group_id=group_id,
            meeting_id=meeting_id,
            member_id=member_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
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
    group_id: int,
    meeting_id: int,
    member_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: DeleteGroupsGroupIdMeetingsMeetingIdMembersMemberIdBody,
) -> Response[Any]:
    """Revoke checkin

     Revoke the checkin for a previously checked-in group member.

    Args:
        group_id (int):  Example: 42.
        meeting_id (int):
        member_id (int):
        body (DeleteGroupsGroupIdMeetingsMeetingIdMembersMemberIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        meeting_id=meeting_id,
        member_id=member_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    group_id: int,
    meeting_id: int,
    member_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: DeleteGroupsGroupIdMeetingsMeetingIdMembersMemberIdBody,
) -> Response[Any]:
    """Revoke checkin

     Revoke the checkin for a previously checked-in group member.

    Args:
        group_id (int):  Example: 42.
        meeting_id (int):
        member_id (int):
        body (DeleteGroupsGroupIdMeetingsMeetingIdMembersMemberIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        meeting_id=meeting_id,
        member_id=member_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
