from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_groups_group_id_members_statistics_response_200 import (
    GetGroupsGroupIdMembersStatisticsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    group_type_role_ids: list[int],
    person_fields: list[str] | Unset = UNSET,
    group_member_fields: list[int] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_group_type_role_ids = group_type_role_ids

    params["group_type_role_ids[]"] = json_group_type_role_ids

    json_person_fields: list[str] | Unset = UNSET
    if not isinstance(person_fields, Unset):
        json_person_fields = person_fields

    params["personFields[]"] = json_person_fields

    json_group_member_fields: list[int] | Unset = UNSET
    if not isinstance(group_member_fields, Unset):
        json_group_member_fields = group_member_fields

    params["groupMemberFields[]"] = json_group_member_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/groups/{group_id}/members/statistics".format(
            group_id=group_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetGroupsGroupIdMembersStatisticsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetGroupsGroupIdMembersStatisticsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetGroupsGroupIdMembersStatisticsResponse200]:
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
    group_type_role_ids: list[int],
    person_fields: list[str] | Unset = UNSET,
    group_member_fields: list[int] | Unset = UNSET,
) -> Response[GetGroupsGroupIdMembersStatisticsResponse200]:
    """Get statistics for group members

     Gets statistics for the group members. The statistics are generated for the fields that are provided
    via query param personFields[] or groupMemberFields[].

    Args:
        group_id (int):  Example: 42.
        group_type_role_ids (list[int]):
        person_fields (list[str] | Unset):
        group_member_fields (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupsGroupIdMembersStatisticsResponse200]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        group_type_role_ids=group_type_role_ids,
        person_fields=person_fields,
        group_member_fields=group_member_fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    group_type_role_ids: list[int],
    person_fields: list[str] | Unset = UNSET,
    group_member_fields: list[int] | Unset = UNSET,
) -> GetGroupsGroupIdMembersStatisticsResponse200 | None:
    """Get statistics for group members

     Gets statistics for the group members. The statistics are generated for the fields that are provided
    via query param personFields[] or groupMemberFields[].

    Args:
        group_id (int):  Example: 42.
        group_type_role_ids (list[int]):
        person_fields (list[str] | Unset):
        group_member_fields (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupsGroupIdMembersStatisticsResponse200
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        group_type_role_ids=group_type_role_ids,
        person_fields=person_fields,
        group_member_fields=group_member_fields,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    group_type_role_ids: list[int],
    person_fields: list[str] | Unset = UNSET,
    group_member_fields: list[int] | Unset = UNSET,
) -> Response[GetGroupsGroupIdMembersStatisticsResponse200]:
    """Get statistics for group members

     Gets statistics for the group members. The statistics are generated for the fields that are provided
    via query param personFields[] or groupMemberFields[].

    Args:
        group_id (int):  Example: 42.
        group_type_role_ids (list[int]):
        person_fields (list[str] | Unset):
        group_member_fields (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupsGroupIdMembersStatisticsResponse200]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        group_type_role_ids=group_type_role_ids,
        person_fields=person_fields,
        group_member_fields=group_member_fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
    group_type_role_ids: list[int],
    person_fields: list[str] | Unset = UNSET,
    group_member_fields: list[int] | Unset = UNSET,
) -> GetGroupsGroupIdMembersStatisticsResponse200 | None:
    """Get statistics for group members

     Gets statistics for the group members. The statistics are generated for the fields that are provided
    via query param personFields[] or groupMemberFields[].

    Args:
        group_id (int):  Example: 42.
        group_type_role_ids (list[int]):
        person_fields (list[str] | Unset):
        group_member_fields (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupsGroupIdMembersStatisticsResponse200
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            group_type_role_ids=group_type_role_ids,
            person_fields=person_fields,
            group_member_fields=group_member_fields,
        )
    ).parsed
