from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_groups_group_id_meetings_meeting_id_response_200 import (
    GetGroupsGroupIdMeetingsMeetingIdResponse200,
)
from ...types import Response


def _get_kwargs(
    group_id: int,
    meeting_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/groups/{group_id}/meetings/{meeting_id}".format(
            group_id=group_id,
            meeting_id=meeting_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetGroupsGroupIdMeetingsMeetingIdResponse200 | None:
    if response.status_code == 200:
        response_200 = GetGroupsGroupIdMeetingsMeetingIdResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetGroupsGroupIdMeetingsMeetingIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    meeting_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetGroupsGroupIdMeetingsMeetingIdResponse200]:
    """Get group meeting

    Args:
        group_id (int):  Example: 42.
        meeting_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupsGroupIdMeetingsMeetingIdResponse200]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        meeting_id=meeting_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    meeting_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetGroupsGroupIdMeetingsMeetingIdResponse200 | None:
    """Get group meeting

    Args:
        group_id (int):  Example: 42.
        meeting_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupsGroupIdMeetingsMeetingIdResponse200
    """

    return sync_detailed(
        group_id=group_id,
        meeting_id=meeting_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    meeting_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetGroupsGroupIdMeetingsMeetingIdResponse200]:
    """Get group meeting

    Args:
        group_id (int):  Example: 42.
        meeting_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupsGroupIdMeetingsMeetingIdResponse200]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        meeting_id=meeting_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    meeting_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetGroupsGroupIdMeetingsMeetingIdResponse200 | None:
    """Get group meeting

    Args:
        group_id (int):  Example: 42.
        meeting_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupsGroupIdMeetingsMeetingIdResponse200
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            meeting_id=meeting_id,
            client=client,
        )
    ).parsed
