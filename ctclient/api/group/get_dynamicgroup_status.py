from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_dynamicgroup_status_response_200 import (
    GetDynamicgroupStatusResponse200,
)
from ...types import Response


def _get_kwargs(
    group_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dynamicgroups/{group_id}/status".format(
            group_id=group_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetDynamicgroupStatusResponse200 | str | None:
    if response.status_code == 200:
        response_200 = GetDynamicgroupStatusResponse200.from_dict(response.json())

        return response_200

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
) -> Response[Any | GetDynamicgroupStatusResponse200 | str]:
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
) -> Response[Any | GetDynamicgroupStatusResponse200 | str]:
    """status of dynamic group

     > **Caution**: This is an preliminary API, and is subject to be changed.

    gets the refresh status of a dynamic group

    * `active` the group is atomatically refreshed on a regular baseis
    * `inactive` the group is not refrehes automatically - note that inactive groups cannot even be
    refreshed manually
    * `manual` the group is refreshed only manally
    * `none` the group is not a dynamic group

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDynamicgroupStatusResponse200 | str]
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
) -> Any | GetDynamicgroupStatusResponse200 | str | None:
    """status of dynamic group

     > **Caution**: This is an preliminary API, and is subject to be changed.

    gets the refresh status of a dynamic group

    * `active` the group is atomatically refreshed on a regular baseis
    * `inactive` the group is not refrehes automatically - note that inactive groups cannot even be
    refreshed manually
    * `manual` the group is refreshed only manally
    * `none` the group is not a dynamic group

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDynamicgroupStatusResponse200 | str
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetDynamicgroupStatusResponse200 | str]:
    """status of dynamic group

     > **Caution**: This is an preliminary API, and is subject to be changed.

    gets the refresh status of a dynamic group

    * `active` the group is atomatically refreshed on a regular baseis
    * `inactive` the group is not refrehes automatically - note that inactive groups cannot even be
    refreshed manually
    * `manual` the group is refreshed only manally
    * `none` the group is not a dynamic group

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDynamicgroupStatusResponse200 | str]
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
) -> Any | GetDynamicgroupStatusResponse200 | str | None:
    """status of dynamic group

     > **Caution**: This is an preliminary API, and is subject to be changed.

    gets the refresh status of a dynamic group

    * `active` the group is atomatically refreshed on a regular baseis
    * `inactive` the group is not refrehes automatically - note that inactive groups cannot even be
    refreshed manually
    * `manual` the group is refreshed only manally
    * `none` the group is not a dynamic group

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDynamicgroupStatusResponse200 | str
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
