from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_groups_members_response_200 import GetGroupsMembersResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: list[int] | Unset = UNSET,
    with_deleted: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids[]"] = json_ids

    params["with_deleted"] = with_deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/groups/members",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetGroupsMembersResponse200 | str | None:
    if response.status_code == 200:
        response_200 = GetGroupsMembersResponse200.from_dict(response.json())

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
) -> Response[Any | GetGroupsMembersResponse200 | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    ids: list[int] | Unset = UNSET,
    with_deleted: bool | Unset = UNSET,
) -> Response[Any | GetGroupsMembersResponse200 | str]:
    r"""Get all group members

     Returns all group members. Only accessible for users with right \"administer persons\"

    Args:
        ids (list[int] | Unset):
        with_deleted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetGroupsMembersResponse200 | str]
    """

    kwargs = _get_kwargs(
        ids=ids,
        with_deleted=with_deleted,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    ids: list[int] | Unset = UNSET,
    with_deleted: bool | Unset = UNSET,
) -> Any | GetGroupsMembersResponse200 | str | None:
    r"""Get all group members

     Returns all group members. Only accessible for users with right \"administer persons\"

    Args:
        ids (list[int] | Unset):
        with_deleted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetGroupsMembersResponse200 | str
    """

    return sync_detailed(
        client=client,
        ids=ids,
        with_deleted=with_deleted,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    ids: list[int] | Unset = UNSET,
    with_deleted: bool | Unset = UNSET,
) -> Response[Any | GetGroupsMembersResponse200 | str]:
    r"""Get all group members

     Returns all group members. Only accessible for users with right \"administer persons\"

    Args:
        ids (list[int] | Unset):
        with_deleted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetGroupsMembersResponse200 | str]
    """

    kwargs = _get_kwargs(
        ids=ids,
        with_deleted=with_deleted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    ids: list[int] | Unset = UNSET,
    with_deleted: bool | Unset = UNSET,
) -> Any | GetGroupsMembersResponse200 | str | None:
    r"""Get all group members

     Returns all group members. Only accessible for users with right \"administer persons\"

    Args:
        ids (list[int] | Unset):
        with_deleted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetGroupsMembersResponse200 | str
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            with_deleted=with_deleted,
        )
    ).parsed
