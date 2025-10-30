import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_external_posts_include_item import GetExternalPostsIncludeItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    before: datetime.datetime | Unset = UNSET,
    last_post_indentifier: str | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    external_group_guid: list[str] | Unset = UNSET,
    external_instance_guid: list[str] | Unset = UNSET,
    include: list[GetExternalPostsIncludeItem] | Unset = UNSET,
    limit: int | Unset = 10,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_before: str | Unset = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat()
    params["before"] = json_before

    params["last_post_indentifier"] = last_post_indentifier

    json_after: str | Unset = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat()
    params["after"] = json_after

    json_external_group_guid: list[str] | Unset = UNSET
    if not isinstance(external_group_guid, Unset):
        json_external_group_guid = external_group_guid

    params["external_group_guid[]"] = json_external_group_guid

    json_external_instance_guid: list[str] | Unset = UNSET
    if not isinstance(external_instance_guid, Unset):
        json_external_instance_guid = external_instance_guid

    params["external_instance_guid[]"] = json_external_instance_guid

    json_include: list[str] | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = []
        for include_item_data in include:
            include_item = include_item_data.value
            json_include.append(include_item)

    params["include[]"] = json_include

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/externalposts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | str | None:
    if response.status_code == 401:
        response_401 = response.text
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

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
    *,
    client: AuthenticatedClient | Client,
    before: datetime.datetime | Unset = UNSET,
    last_post_indentifier: str | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    external_group_guid: list[str] | Unset = UNSET,
    external_instance_guid: list[str] | Unset = UNSET,
    include: list[GetExternalPostsIncludeItem] | Unset = UNSET,
    limit: int | Unset = 10,
) -> Response[Any | str]:
    """Get a list of external posts. The posts are sorted by the `createdDate` field descending.

    Args:
        before (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        last_post_indentifier (str | Unset):
        after (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        external_group_guid (list[str] | Unset):
        external_instance_guid (list[str] | Unset):
        include (list[GetExternalPostsIncludeItem] | Unset):
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        before=before,
        last_post_indentifier=last_post_indentifier,
        after=after,
        external_group_guid=external_group_guid,
        external_instance_guid=external_instance_guid,
        include=include,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    before: datetime.datetime | Unset = UNSET,
    last_post_indentifier: str | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    external_group_guid: list[str] | Unset = UNSET,
    external_instance_guid: list[str] | Unset = UNSET,
    include: list[GetExternalPostsIncludeItem] | Unset = UNSET,
    limit: int | Unset = 10,
) -> Any | str | None:
    """Get a list of external posts. The posts are sorted by the `createdDate` field descending.

    Args:
        before (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        last_post_indentifier (str | Unset):
        after (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        external_group_guid (list[str] | Unset):
        external_instance_guid (list[str] | Unset):
        include (list[GetExternalPostsIncludeItem] | Unset):
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        client=client,
        before=before,
        last_post_indentifier=last_post_indentifier,
        after=after,
        external_group_guid=external_group_guid,
        external_instance_guid=external_instance_guid,
        include=include,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    before: datetime.datetime | Unset = UNSET,
    last_post_indentifier: str | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    external_group_guid: list[str] | Unset = UNSET,
    external_instance_guid: list[str] | Unset = UNSET,
    include: list[GetExternalPostsIncludeItem] | Unset = UNSET,
    limit: int | Unset = 10,
) -> Response[Any | str]:
    """Get a list of external posts. The posts are sorted by the `createdDate` field descending.

    Args:
        before (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        last_post_indentifier (str | Unset):
        after (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        external_group_guid (list[str] | Unset):
        external_instance_guid (list[str] | Unset):
        include (list[GetExternalPostsIncludeItem] | Unset):
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        before=before,
        last_post_indentifier=last_post_indentifier,
        after=after,
        external_group_guid=external_group_guid,
        external_instance_guid=external_instance_guid,
        include=include,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    before: datetime.datetime | Unset = UNSET,
    last_post_indentifier: str | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    external_group_guid: list[str] | Unset = UNSET,
    external_instance_guid: list[str] | Unset = UNSET,
    include: list[GetExternalPostsIncludeItem] | Unset = UNSET,
    limit: int | Unset = 10,
) -> Any | str | None:
    """Get a list of external posts. The posts are sorted by the `createdDate` field descending.

    Args:
        before (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        last_post_indentifier (str | Unset):
        after (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        external_group_guid (list[str] | Unset):
        external_instance_guid (list[str] | Unset):
        include (list[GetExternalPostsIncludeItem] | Unset):
        limit (int | Unset):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            client=client,
            before=before,
            last_post_indentifier=last_post_indentifier,
            after=after,
            external_group_guid=external_group_guid,
            external_instance_guid=external_instance_guid,
            include=include,
            limit=limit,
        )
    ).parsed
